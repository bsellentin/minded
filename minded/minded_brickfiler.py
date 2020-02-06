#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# brick_filer program -- Simple GUI to manage files on a LEGO Mindstorms P-Bricks
# Copyright (C) 2006  Douglas P Lau
# Copyright (C) 2010  rhn
# Copyright (C) 2016  selles
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.


import sys
from pathlib import Path
import urllib.request
from urllib.parse import urlparse, unquote
import logging

from typing import List, Dict, Tuple, Any, Union

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import Gtk, Gdk, Gio, Pango
from gi.repository.GdkPixbuf import Pixbuf

from nxt.brick import FileFinder, FileReader, FileWriter

logger = logging.getLogger(__name__)

(COLUMN_PATH, COLUMN_PIXBUF, COLUMN_SIZE, COLUMN_ISDIR) = range(4)

DRAG_ACTION = Gdk.DragAction.COPY

def read_file(brick, file_uri):
    '''read file from NXT brick'''
    # TODO use Gio.File
    file_path = urlparse(unquote(file_uri))
    file_name = Path(file_path.path).name

    with FileReader(brick, file_name) as reader:
        with open(file_path.path, 'wb') as file:
            for data in reader:
                file.write(data)

def write_file(brick, file_name, data):
    '''write one file to NXT brick'''
    writer = FileWriter(brick, file_name, len(data))
    logger.debug('Pushing {} ({} bytes) ...'.format(file_name, writer.size))
    sys.stdout.flush()
    writer.write(data)
    logger.debug('wrote %d bytes' % len(data))
    writer.close()

def write_files(brick, file_uris):
    '''write multiple files to NXT brick
    returns wnames[str name, str len], what is this good for?
    '''
    wnames = []  # type: List[Tuple[str, str]]
    for file_uri in file_uris:
        if file_uri:
            logger.debug('File: {} Type {}'.format(file_uri, type(file_uri)))
            #TODO use Gio.File
            file_path = urlparse(unquote(file_uri))
            file_name = Path(file_path.path).name

            url = urllib.request.urlopen(file_uri)
            try:
                data = url.read()
            finally:
                url.close()
            logger.debug('name {}, size: {}'.format(file_name, len(data)))
            try:
                write_file(brick, file_name, data)
                wnames.append((file_name, str(len(data))))
            except:
                pass
    return wnames

class BrickListing(Gtk.ListStore):
    '''
    get files and directories of given path from brick and
    put them into a liststore
    '''
    def __init__(self, brick=None, path=None):
        Gtk.ListStore.__init__(self, str, Pixbuf, int, bool)
        #self.set_sort_column_id(0, 0)

        if brick:
            self.populate(brick, path)

    def populate(self, brick, path):

        filelist = []

        if brick.__class__.__name__ == 'Brick':
            self.clear()

            finder = FileFinder(brick, path)
            for (fname, size) in finder:
                # exclude NVconfig.sys?
                if Path(fname).suffix == ".rso":
                    filelist.append((fname, AUDIOICON, size, False))
                elif Path(fname).suffix == ".ric":
                    filelist.append((fname, GRAPHICICON, size, False))
                elif Path(fname).suffix in [".rxe", ".rtm"]:
                    filelist.append((fname, EXECICON, size, False))
                else:
                    filelist.append((fname, FILEICON, size, False))

            filelist.sort()
            for file in filelist:
                self.append(file)

            if logger.isEnabledFor(logging.DEBUG):
                for row in self:
                    logger.debug('{} {}'.format(row[COLUMN_PATH], row[COLUMN_SIZE]))

        elif brick.__class__.__name__ == 'EV3':
            self.clear()
            dirlist = []

            '''
            #define   vmEXT_SOUND                   ".rsf"     //!< Robot Sound File
            #define   vmEXT_GRAPHICS                ".rgf"     //!< Robot Graphics File
            #define   vmEXT_BYTECODE                ".rbf"     //!< Robot Byte code File
            #define   vmEXT_TEXT                    ".rtf"     //!< Robot Text File
            #define   vmEXT_DATALOG                 ".rdf"     //!< Robot Datalog File
            #define   vmEXT_PROGRAM                 ".rpf"     //!< Robot Program File
            #define   vmEXT_CONFIG                  ".rcf"     //!< Robot Configuration File
            #define   vmEXT_ARCHIVE                 ".raf"     //!< Robot Archive File
            '''
            if brick.usb_ready():
                content = brick.list_dir(path)
                for folder in content['folders']:
                    if folder in ['.', '..',]:
                        pass
                    else:
                        dirlist.append((folder, DIRICON, 2, True))  # TODO: get number of objects
                for file in content['files']:
                    logger.debug('{}'.format(file))
                    if Path(file['name']).suffix == ".rgf":
                        filelist.append((file['name'], GRAPHICICON, file['size'], False))
                    elif Path(file['name']).suffix in [".rsf", ".rmd", ".wav", ".rso"]:
                        filelist.append((file['name'], AUDIOICON, file['size'], False))
                    else:
                        filelist.append((file['name'], FILEICON, file['size'], False))

                # store sorted directories first
                dirlist.sort()
                for directory in dirlist:
                    self.append(directory)
                # store sorted files
                filelist.sort()
                for file in filelist:
                    self.append(file)
            else:
                self.append(['Error', ERRORICON, 0, False])
        else:
            self.clear()

class HostListing(Gtk.ListStore):

    def __init__(self, path):
        Gtk.ListStore.__init__(self, str, Pixbuf, int, bool)

        self.populate(path)

    def populate(self, path):

        self.clear()

        dirlist = []
        filelist = []

        for entry in Path(path).iterdir():
            # don't list hidden files
            if not str(entry.stem)[0] == '.':
                try:
                    if entry.is_dir():
                        try:
                            dirlist.append([str(entry.name), DIRICON,
                                            len([name for name in entry.iterdir()]), True])
                        except PermissionError:
                            dirlist.append([str(entry.name), ERRORICON, 0, False])
                    elif entry.is_file():
                        if entry.suffix in [".rsf", ".rmd", ".wav", ".rso"]:
                            filelist.append([str(entry.name), AUDIOICON,
                                             entry.stat().st_size, False])
                        elif entry.suffix == '.ric':
                            filelist.append([str(entry.name), GRAPHICICON,
                                             entry.stat().st_size, False])
                        elif entry.suffix == ".rxe":
                            filelist.append([str(entry.name), EXECICON,
                                             entry.stat().st_size, False])
                        else:
                            filelist.append([str(entry.name), FILEICON,
                                             entry.stat().st_size, False])
                    else:
                        pass
                except PermissionError:
                    pass

        # store sorted directories first
        dirlist.sort()
        for directory in dirlist:
            self.append(directory)
        # store sorted files
        filelist.sort()
        for file in filelist:
            self.append(file)

class FileIconView(Gtk.IconView):

    def __init__(self, model):
        Gtk.IconView.__init__(self, model)

        self.props.column_spacing = 2
        self.props.item_padding = 0
        self.props.row_spacing = 2
        self.props.item_width = 70
        self.props.selection_mode = Gtk.SelectionMode.MULTIPLE
        self.set_model(model)
        self.set_pixbuf_column(COLUMN_PIXBUF)
        self.set_text_column(COLUMN_PATH)

        self.enable_model_drag_source(Gdk.ModifierType.BUTTON1_MASK,
                                      [],
                                      DRAG_ACTION)
        
        targets = Gtk.TargetEntry.new('text/uri-list', 8, 0)
        self.enable_model_drag_dest([targets], DRAG_ACTION)
        '''
        self.iconview.add_events(Gdk.EventMask.POINTER_MOTION_MASK)
        self.iconview.connect("item-activated", self.iv_icon_activated)
        self.iconview.connect("button-press-event", self.on_mouse_click)
        self.iconview.connect("motion-notify-event", self.on_pointer_motion)

    def on_pointer_motion(self, widget, event):
        path= self.iconview.get_path_at_pos(event.x, event.y)
        if path !=None:
                self.iconview.select_path(path)
        #If we're outside of an item, deselect all items (turn off highlighting)
        if path == None:
            self.iconview.unselect_all()

    def on_mouse_click(self,widget, event):
        if event.type == Gdk.EventType.BUTTON_PRESS:
            path=self.iconview.get_selected_items()[0]
           #if right click activate a pop-up menu
            if event.button == 3 and path != None:
                self.popup.popup(None, None, None, None, event.button, event.time)
           #if left click, activate the item to execute
            if event.button == 1 and path != None:
                self.iv_icon_activated(widget, path)
            '''

class FileInfoBar(Gtk.Frame):
    ''' Show information about selection in lower right corner '''
    def __init__(self, view):
        Gtk.Frame.__init__(self)

        self.set_valign(Gtk.Align.END)
        self.set_halign(Gtk.Align.END)
        infobox = Gtk.Box()
        infobox.override_background_color(Gtk.StateType.NORMAL,
                                          Gdk.RGBA(1.0, 1.0, 1.0, 1.0))

        self.selected = Gtk.Label("selected")
        self.selected.set_ellipsize(Pango.EllipsizeMode.MIDDLE)
        infobox.pack_start(self.selected, False, False, 5)

        self.sizeinfo = Gtk.Label("size")
        infobox.pack_start(self.sizeinfo, False, False, 5)

        self.add(infobox)

    def update(self, view):

        selected_path = view.get_selected_items()[0]
        selected_iter = view.get_model().get_iter(selected_path)
        file_name = view.get_model().get_value(selected_iter, COLUMN_PATH)
        file_size = view.get_model().get_value(selected_iter, COLUMN_SIZE)
        self.selected.set_text("\u00BB" + file_name + "\u00AB selected")
        if view.get_model().get_value(selected_iter, COLUMN_ISDIR):
            self.sizeinfo.set_text("(" + str(file_size) + " Objects)")
        else:
            self.sizeinfo.set_text("(" + self.human_readable_size(file_size) + ")")

    def human_readable_size(self, size, precision=1):
        if size:
            suffixes = ['Bytes', 'kB', 'MB', 'GB', 'TB']
            suffix_index = 0
            while size > 1024 and suffix_index < 4:
                suffix_index += 1
                size = size/1024.0
            return '{:.{prec}f} {}'.format(size, suffixes[suffix_index], prec=precision)
        else:
            return 'not readable'

class BrickFiler():
    '''
    file explorer for NXT- and EV3-bricks
    '''
    #TARGETS = []

    def __init__(self, application):

        self.app = application

        self.window = Gtk.Window(title="Brick-Filer")
        self.window.set_application(application)
        self.window.set_default_size(640, 480)
        self.window.set_border_width(6)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Brick-Filer"
        self.window.set_titlebar(hb)

        hpaned = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)
        hpaned.set_position(300)

        # Look for Brick
        if self.app.nxt_brick:
            logger.info('got app.nxt_brick')
            self.nxt_model = BrickListing(self.app.nxt_brick,
                                          '*.*')
            hpaned.add1(self.make_brickfile_panel(str(self.app.nxt_brick.sock),
                                                  self.nxt_model))
        elif self.app.ev3_brick:
            logger.info('got app.ev3_brick')
            self.current_ev3_directory = self.app.settings.get_string('prjsstore')
            self.ev3_model = BrickListing(self.app.ev3_brick,
                                          self.current_ev3_directory)
            hpaned.add1(self.make_brickfile_panel('EV3', self.ev3_model))
        else:
            self.nxt_model = BrickListing(None, None)
            hpaned.add1(self.make_brickfile_panel('No brick', self.nxt_model))

        self.current_directory = str(Path.home())
        self.host_model = HostListing(self.current_directory)
        hpaned.add2(self.make_hostfile_panel(self.host_model))

        self.window.add(hpaned)
        self.window.show_all()
        self.hostinfoframe.hide()
        self.brickinfoframe.hide()
        self.window.connect('delete-event', self.quit)

    def make_hostfile_list(self, model):

        host_view = FileIconView(model)
        host_view.connect("item-activated", self.on_host_item_activated)
        host_view.connect("selection-changed", self.on_host_selection_changed)
        #host_view.connect('key-press-event', self.on_key_pressed)

        host_view.drag_source_add_uri_targets()
        host_view.connect("drag_data_get", self.drag_data_get_host_data)

        host_view.drag_dest_add_text_targets()
        host_view.connect("drag_data_received", self.drag_data_received_brick_data)

        return host_view

    def make_brickfile_list(self, model):

        brick_view = FileIconView(model)
        brick_view.connect("item-activated", self.on_brick_item_activated)
        brick_view.connect("selection-changed", self.on_brick_selection_changed)
        brick_view.connect('key-press-event', self.on_key_pressed)

        brick_view.drag_source_add_uri_targets()
        brick_view.connect("drag_data_get", self.drag_data_get_brick_data)

        brick_view.drag_dest_add_uri_targets()
        brick_view.connect("drag_data_received", self.drag_data_received_data)

        return brick_view

    def make_hostfile_panel(self, model):
        vbox = Gtk.VBox()

        # Location bar
        location_bar = Gtk.Grid()
        self.up_button = Gtk.Button()
        icon = Gio.ThemedIcon(name="go-previous-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        self.up_button.add(image)
        self.up_button.connect("clicked", self.on_prev_dir_clicked)
        location_bar.attach(self.up_button, 0, 0, 1, 1,)
        self.location = Gtk.Entry()
        self.location.set_hexpand(True)
        self.location.set_text(self.current_directory)
        self.location.set_icon_from_icon_name(0, 'folder-symbolic')
        location_bar.attach(self.location, 1, 0, 1, 1)
        vbox.pack_start(location_bar, False, False, 0)

        self.host_view = self.make_hostfile_list(model)

        overlay = Gtk.Overlay()
        scroller = Gtk.ScrolledWindow()
        scroller.set_border_width(2)
        scroller.add(self.host_view)
        overlay.add(scroller)

        self.hostinfoframe = FileInfoBar(self.host_view)
        overlay.add_overlay(self.hostinfoframe)
        vbox.pack_start(overlay, True, True, 0)

        return vbox

    def make_brickfile_panel(self, name, model):
        vbox = Gtk.VBox()
        #v.pack_start(Gtk.Label(name), False, False, 0)
        tool_bar = Gtk.Grid()
        self.del_button = Gtk.Button()
        icon = Gio.ThemedIcon(name="user-trash-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        self.del_button.add(image)
        self.del_button.set_tooltip_text("delete")
        self.del_button.connect("clicked", self.on_delete_btn_clicked)
        self.del_button.drag_dest_set(Gtk.DestDefaults.ALL, [], DRAG_ACTION)
        self.del_button.drag_dest_add_uri_targets()
        self.del_button.connect("drag_data_received", self.drag_data_received_brick_deldata)
        tool_bar.attach(self.del_button, 0, 0, 1, 1)

        if self.app.ev3_brick:
            self.ev3_up_button = Gtk.Button()
            icon = Gio.ThemedIcon(name="go-previous-symbolic")
            image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
            self.ev3_up_button.add(image)
            self.ev3_up_button.connect("clicked", self.on_ev3_prev_dir_clicked)
            tool_bar.attach(self.ev3_up_button, 1, 0, 1, 1,)
            self.ev3location = Gtk.Entry()
            self.ev3location.set_hexpand(True)
            self.ev3location.set_text(self.current_ev3_directory)
            self.ev3location.set_icon_from_icon_name(0, 'folder-symbolic')
            tool_bar.attach(self.ev3location, 2, 0, 1, 1)
        vbox.pack_start(tool_bar, False, False, 0)

        self.brick_view = self.make_brickfile_list(model)

        overlay = Gtk.Overlay()
        scroller = Gtk.ScrolledWindow()
        scroller.set_border_width(2)
        scroller.add(self.brick_view)
        overlay.add(scroller)

        self.brickinfoframe = FileInfoBar(self.brick_view)
        overlay.add_overlay(self.brickinfoframe)
        vbox.pack_start(overlay, True, True, 0)

        return vbox

    def on_host_item_activated(self, widget, item):
        '''double click on directory opens it'''

        model = widget.get_model()
        path = model[item][COLUMN_PATH]
        is_dir = model[item][COLUMN_ISDIR]

        if not is_dir:
            return

        self.current_directory = str(Path(self.current_directory, path))
        self.location.set_text(self.current_directory)
        self.host_model.populate(self.current_directory)
        self.up_button.set_sensitive(True)

    def on_brick_item_activated(self, widget, item):
        '''double click on EV3 directory opens it'''
        model = widget.get_model()
        path = model[item][COLUMN_PATH]
        is_dir = model[item][COLUMN_ISDIR]
        logger.debug('double click on {}, is_dir {}'.format(path, is_dir))

        if self.app.ev3_brick and is_dir:
            self.current_ev3_directory = str(Path(self.current_ev3_directory, path))
            self.ev3_model.populate(self.app.ev3_brick, self.current_ev3_directory)
            self.ev3location.set_text(self.current_ev3_directory)
            if not self.ev3_up_button.get_sensitive():
                self.ev3_up_button.set_sensitive(True)
            if self.current_ev3_directory.startswith('/home/root/lms2012/prjs'):
                if not self.del_button.get_sensitive():
                    self.del_button.set_sensitive(True)
        # NXT has no directories

    def on_host_selection_changed(self, widget):
        try:
            #iter_path = widget.get_selected_items()[0]
            self.hostinfoframe.update(widget)
            self.hostinfoframe.show()
        except:
            self.hostinfoframe.hide()

    def on_brick_selection_changed(self, widget):
        try:
            #iter_path = widget.get_selected_items()[0]
            self.brickinfoframe.update(widget)
            self.brickinfoframe.show()
        except:
            self.brickinfoframe.hide()

    def on_prev_dir_clicked(self, widget):
        '''walk one host directory higher'''
        self.current_directory = str(Path(self.current_directory).parent)
        self.location.set_text(self.current_directory)
        self.host_model.populate(self.current_directory)
        sensitive = True
        if self.current_directory == "/":
            sensitive = False
        self.up_button.set_sensitive(sensitive)

    def on_ev3_prev_dir_clicked(self, widget):
        '''walk one EV3 directory higher'''
        self.current_ev3_directory = str(Path(self.current_ev3_directory).parent)
        self.ev3_model.populate(self.app.ev3_brick, self.current_ev3_directory)
        self.ev3location.set_text(self.current_ev3_directory)
        sensitive = True
        if self.current_ev3_directory == "/":
            sensitive = False
        self.ev3_up_button.set_sensitive(sensitive)
        if not self.current_ev3_directory.startswith('/home/root/lms2012/prjs'):
            if self.del_button.get_sensitive():
                self.del_button.set_sensitive(False)

    def on_key_pressed(self, widget, event):
        if event.keyval == Gdk.KEY_Delete:
            self.on_delete_btn_clicked(widget)

    def drag_data_get_brick_data(self, iconview, context, selection, target_id,
                           etime):
        '''
        brick is drag source
        select NXT-file(s) to copy to host or to delete
        '''
        file_uris = []
        for item in iconview.get_selected_items():
            selected_iter = iconview.get_model().get_iter(item)
            file_uri = iconview.get_model().get_value(selected_iter, COLUMN_PATH)
            file_uris.append(file_uri)
        logger.debug(file_uris)
        success = selection.set_uris(file_uris)
        if logger.isEnabledFor(logging.DEBUG):
            if success:
                logger.debug(selection.get_uris())
            else:
                logger.debug('selection set uri(s) NOT okay')

    def drag_data_get_host_data(self, iconview, context, selection, target_id,
                               etime):
        '''
        host is drag source
        set the selected uri(s) to copy to brick
        '''
        file_uris = []
        for item in iconview.get_selected_items():
            selected_iter = iconview.get_model().get_iter(item)
            uri = iconview.get_model().get_value(selected_iter, COLUMN_PATH)
            name = iconview.get_model().get_value(selected_iter, COLUMN_PATH)
            file_uris.append(Path(self.current_directory, name).as_uri())
        logger.debug('dragged: {}'.format(file_uris))
        success = selection.set_uris(file_uris)
        if logger.isEnabledFor(logging.DEBUG):
            if success:
                logger.debug('selection set uris okay')
            else:
                logger.debug('selection set uris NOT okay')

    def drag_data_received_data(self, iconview, context, x, y, selection,
                                info, etime):
        '''
        brick is drag destination
        write file to brick from host 
        '''
        file_uris = selection.get_uris()

        if context.get_actions() == DRAG_ACTION:

            if self.app.nxt_brick:
                # Accept only these files (File write)
                # Download firmware              *.rfw
                # Download user defined programs *.rxe
                # OnBrick programming            *.rpg
                # Try-Me programs                *.rtm
                # Sound                          *.rso
                # Graphics                       *.ric
                ext = ['.rxe', '.rso', '.ric', '.rtm', 'rpg']
                for file in file_uris:
                    if file.endswith(tuple(ext)):
                        logger.debug('dropped: {}'.format(file_uris))
                        wnames = write_files(self.app.nxt_brick, file_uris) # returns ('fname', 'size')
                        self.nxt_model.populate(self.app.nxt_brick, '*.*')
                        context.finish(True, False, etime)
                    else:
                        logger.debug("don't want {}".format(file_uris))
                        # TODO: Give feedback
                        #bar = gtk.InfoBar()
                        #vb.pack_start(bar, False, False)
                        #bar.set_message_type(gtk.MESSAGE_INFO)
                        #bar.get_content_area().pack_start(
                        #gtk.Label("What shall I do with this?"), False, False)
                        context.finish(False, False, etime)
            if (self.app.ev3_brick and
                    self.current_ev3_directory.startswith('/home/root/lms2012/prjs')):
                for file in file_uris:
                    # TODO: which files will we accept?
                    gfile = Gio.File.new_for_uri(file)
                    info = gfile.query_file_type(Gio.FileQueryInfoFlags.NONE, None)
                    if info == Gio.FileType.DIRECTORY:
                        prj = gfile.get_basename()
                        logger.debug('URI is directory')
                        infos = gfile.enumerate_children('standard::name',
                                                         Gio.FileQueryInfoFlags.NOFOLLOW_SYMLINKS,
                                                         None)
                        for info in infos:
                            child = infos.get_child(info)
                            infile = str(Path(self.current_ev3_directory,
                                         prj, child.get_basename()))
                            outfile = child.get_parse_name()
                            logger.debug('dropped: {}'.format(outfile))
                            logger.debug('write to: {}'.format(infile))
                            data = open(outfile, 'rb').read()
                            self.app.ev3_brick.write_file(infile, data)
                    else:
                        infile = str(Path(self.current_ev3_directory, gfile.get_basename()))
                        outfile = gfile.get_parse_name()
                        logger.debug('dropped: {}'.format(outfile))
                        logger.debug('write to: {}'.format(infile))
                        data = open(outfile, 'rb').read()
                        #data = gfile.read()
                        self.app.ev3_brick.write_file(infile, data)
                        #TypeError: object of type 'GLocalFileInputStream' has no len()

                    self.ev3_model.populate(self.app.ev3_brick, self.current_ev3_directory)
                    context.finish(True, False, etime)
        else:
            logger.debug('what happend?')
            logger.debug(context.get_actions())
            context.finish(False, False, etime)

    def drag_data_received_brick_data(self, iconview, context, x, y, selection,
                                   info, etime):
        '''
        host is drag destination
        read file from brick and write to host
        '''
        file_uris = selection.get_uris()

        if context.get_actions() == DRAG_ACTION:

            if self.app.nxt_brick:
                logger.debug(context.get_actions())
                logger.debug(selection.get_uris())
                logger.debug(self.current_directory)
                for uri in file_uris:
                    host_uri = Path(self.current_directory, uri).as_uri()
                    nxtfile = read_file(self.app.nxt_brick, host_uri)

            if self.app.ev3_brick:
                for uri in file_uris:
                    for row in self.ev3_model:
                        if row[COLUMN_PATH] == uri:
                            logger.debug('{} is directory: {}'.format(uri, row[COLUMN_ISDIR]))
                            if row[COLUMN_ISDIR]:

                                gfile = Gio.File.new_for_path(str(Path(self.current_directory, uri)))
                                gfile.make_directory(None)

                                content = self.app.ev3_brick.list_dir(str(Path(self.current_ev3_directory, uri)))
                                for file in content['files']:
                                    logger.debug(file['name'])
                                    host_uri = str(Path(self.current_directory, uri, file['name']))
                                    gfile = Gio.File.new_for_path(host_uri)
                                    ev3_uri = str(Path(self.current_ev3_directory, uri, file['name']))
                                    data = self.app.ev3_brick.read_file(ev3_uri)
                                    gfile.replace_contents(data, None, False,
                                                           Gio.FileCreateFlags.NONE, None)
                            else:
                                host_uri = str(Path(self.current_directory, uri))
                                gfile = Gio.File.new_for_path(host_uri)
                                logger.debug(host_uri)
                                ev3_uri = str(Path(self.current_ev3_directory, uri))
                                data = self.app.ev3_brick.read_file(ev3_uri)
                                gfile.replace_contents(data, None, False,
                                                       Gio.FileCreateFlags.NONE, None)
                            break
            self.host_model.populate(self.current_directory)
            context.finish(True, False, etime)
        else:
            logger.debug('what happend?')
            logger.debug(context.get_actions())
            context.finish(False, False, etime)

    def drag_data_received_brick_deldata(self, iconview, context, x, y, selection,
                                      info, etime):
        '''
        delete button as drag destination
        '''
        file_uris = selection.get_uris()
        logger.debug('selected to delete: {}'.format(file_uris))

        if context.get_actions() == DRAG_ACTION:
            if self.app.nxt_brick:
                for uri in selection.get_uris():
                    try:
                        self.app.nxt_brick.delete(uri)
                        logger.debug('deleted {}'.format(uri))
                    except:
                        logger.debug('uri {} not deleted'.format(uri))
                self.nxt_model.populate(self.app.nxt_brick, '*.*')
                context.finish(True, False, etime)

            if self.app.ev3_brick:
                for uri in selection.get_uris():
                    for row in self.ev3_model:
                        if row[COLUMN_PATH] == uri:
                            logger.debug('{} is directory: {}'.format(uri, row[COLUMN_ISDIR]))
                            file_name = str(Path(self.current_ev3_directory,
                                                 row[COLUMN_PATH]))
                            if row[COLUMN_ISDIR]:
                                self.app.ev3_brick.del_dir(file_name)
                            else:
                                self.app.ev3_brick.del_file(file_name)
                            break
                self.ev3_model.populate(self.app.ev3_brick, self.current_ev3_directory)
                context.finish(True, False, etime)
        else:
            context.finish(False, False, etime)

    def on_delete_btn_clicked(self, button):
        '''delete file on brick'''
        if self.app.nxt_brick:
            self.delete_nxt_file()
        if self.app.ev3_brick:
            self.delete_ev3_file()

    def delete_nxt_file(self):
        '''delete file(s) on nxt-brick'''
        if self.nxt_model:
            blacklist = ['! Startup.rso', '! Click.rso', 'NVConfig.sys', 'RPGReader.sys']

            for item in self.brick_view.get_selected_items():
                logger.debug('{}'.format(item))

                selected_iter = self.nxt_model.get_iter(item)
                if selected_iter is not None:
                    file_name = self.nxt_model.get_value(selected_iter, 0)
                    logger.debug('selected to delete: {}'.format(file_name))
                    if file_name in blacklist:
                        continue
                    try:
                        self.app.nxt_brick.delete(file_name)
                        logger.debug('deleted: {}'.format(file_name))
                        self.nxt_model.remove(selected_iter)
                    except:
                        logger.debug('File not deleted')

    def delete_ev3_file(self):
        '''delete file(s) on ev3-brick'''
        if self.ev3_model:
            blacklist = ['BrkDL_SAVE', 'BrkProg_SAVE', 'SD_Card']

            for item in  self.brick_view.get_selected_items():
                logger.debug('item {}'.format(item))
                selected_iter = self.ev3_model.get_iter(item)
                if selected_iter is not None:
                    name = self.ev3_model.get_value(selected_iter, COLUMN_PATH)
                    file_name = str(Path(self.current_ev3_directory, name))
                    logger.debug('selected to delete: {}'.format(file_name))
                    if name in blacklist:
                        continue
                    if self.ev3_model.get_value(selected_iter, COLUMN_ISDIR):
                        # is Dir
                        try:
                            self.app.ev3_brick.del_dir(file_name)
                            logger.debug('Directory {} deleted'.format(file_name))
                            self.ev3_model.remove(selected_iter)
                        except:
                            logger.debug('Directory not deleted')
                    else:
                        # is File
                        try:
                            self.app.ev3_brick.del_file(file_name)
                            logger.debug('deleted: {}'.format(file_name))
                            self.ev3_model.remove(selected_iter)
                        except:
                            logger.debug('File not deleted')
                else:
                    logger.debug('No file selected')

    def quit(self, *args):
        '''Quit brickfiler'''
        self.window.destroy()
        return True

DIRICON = Gtk.IconTheme.get_default().load_icon('folder', 48, 0)
FILEICON = Gtk.IconTheme.get_default().load_icon('ascii', 48, 0)
AUDIOICON = Gtk.IconTheme.get_default().load_icon('sound', 48, 0)
GRAPHICICON = Gtk.IconTheme.get_default().load_icon('image', 48, 0)
if Gtk.IconTheme.get_default().has_icon('exec'):
    EXECICON = Gtk.IconTheme.get_default().load_icon('exec', 48, 0)
else:
    EXECICON = Gtk.IconTheme.get_default().load_icon('application-x-executable', 48, 0)
ERRORICON = Gtk.IconTheme.get_default().load_icon('error', 48, 0)
