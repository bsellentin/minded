#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# nxt_filer program -- Simple GUI to manage files on a LEGO Mindstorms NXT
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

import urllib.request
import sys
from pathlib import Path
from urllib.parse import urlparse, unquote
import logging

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import Gtk, Gdk, Gio, GObject, Pango
from gi.repository.GdkPixbuf import Pixbuf

# for usbListener
gi.require_version('GUdev', '1.0')
from gi.repository import GUdev

import nxt.locator
from nxt.brick import FileFinder, FileReader, FileWriter

logger = logging.getLogger(__name__)

(COLUMN_PATH, COLUMN_PIXBUF, COLUMN_SIZE, COLUMN_ISDIR) = range(4)

DRAG_ACTION = Gdk.DragAction.COPY

def read_file(brick, file_uri):
    '''read file from NXT brick'''
    file_path = urlparse(unquote(file_uri))
    file_name = Path(file_path.path).name

    with FileReader(brick, file_name) as r:
        with open(file_path.path, 'wb') as f:
            for data in r:
                f.write(data)

def write_file(brick, file_name, data):
    '''write one file to NXT brick'''
    w = FileWriter(brick, file_name, len(data))
    logger.debug('Pushing %s (%d bytes) ...' % (file_name, w.size)) 
    sys.stdout.flush()
    w.write(data)
    logger.debug('wrote %d bytes' % len(data))
    w.close()

def write_files(brick, file_uris):
    '''write multiple files to NXT brick'''
    wnames = []
    for file_uri in file_uris:
        if file_uri:
            logger.debug('File: %s Type %s' % (file_uri, type(file_uri)))
            file_path = urlparse(unquote(file_uri))
            file_name = Path(file_path.path).name

            url = urllib.request.urlopen(file_uri)
            try:
                data = url.read()
            finally:
                url.close()
            logger.debug('name %s, size: %d ' % (file_name, len(data)))
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
    def __init__(self, brick = None, brick_type = None, path = None):
        Gtk.ListStore.__init__(self, str, Pixbuf, str, bool)
        #self.set_sort_column_id(0, 0)
        
        self.brick_type = brick_type
        
        if brick:
            self.populate(brick, path)

    def populate(self, brick, path):

        if self.brick_type == 'nxt':
            self.clear()
            filelist = []

            f = FileFinder(brick, path)
            for (fname, size) in f:
                # exclude NVconfig.sys?
                if Path(fname).suffix == ".rso":
                    filelist.append([fname, AUDIOICON, str(size), False])
                elif Path(fname).suffix == ".ric":
                    filelist.append([fname, GRAPHICICON, str(size), False])
                elif Path(fname).suffix in [".rxe", ".rtm"]:
                    filelist.append([fname, EXECICON, str(size), False])
                else:
                    filelist.append([fname, FILEICON, str(size), False])

            filelist.sort()
            for f in filelist:
                self.append(f)

            if logger.isEnabledFor(logging.DEBUG):
                for row in self:
                    logger.debug(row[COLUMN_PATH,COLUMN_SIZE])

        elif self.brick_type == 'ev3':
            self.clear()
            dirlist = []
            filelist = []
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
                        dirlist.append([folder, DIRICON, '0', True])
                for file in content['files']:
                    if Path(file['name']).suffix == ".rgf":
                        filelist.append([file['name'], GRAPHICICON, str(file['size']), False])
                    elif Path(file['name']).suffix in [".rsf", ".rmd", ".wav", ".rso"]:
                        filelist.append([file['name'], AUDIOICON, str(file['size']), False])
                    else:
                        filelist.append([file['name'], FILEICON, str(file['size']), False])

                # store sorted directories first
                dirlist.sort()
                for d in dirlist:
                    self.append(d)
                # store sorted files
                filelist.sort()
                for f in filelist:
                    self.append(f)
            else:
                self.append(['Error', ERRORICON, str(0), False])
        else:
            self.clear()

class HostListing(Gtk.ListStore):

    def __init__(self, path):
        Gtk.ListStore.__init__(self, str, Pixbuf, str, bool)

        self.populate(path)

    def populate(self, path):

        self.clear()

        dirlist = []
        filelist = []

        for fl in Path(path).iterdir():
            # don't list hidden files
            if not str(fl.stem)[0] == '.':
                if fl.is_dir():
                    dirlist.append([str(fl.name), DIRICON, 
                                    str(len([name for name in fl.iterdir()])), True])
                elif fl.is_file():
                    if fl.suffix == '.rso':
                        filelist.append([str(fl.name), AUDIOICON,
                                         str(fl.stat().st_size), False])
                    elif fl.suffix == '.ric':
                        filelist.append([str(fl.name), GRAPHICICON,
                                         str(fl.stat().st_size), False])
                    elif fl.suffix == ".rxe":
                        filelist.append([str(fl.name), EXECICON,
                                         str(fl.stat().st_size), False])
                    else:
                        filelist.append([str(fl.name), FILEICON, 
                                         str(fl.stat().st_size), False])
                else:
                    pass

        # store sorted directories first
        dirlist.sort()
        for d in dirlist:
            self.append(d)
        # store sorted files
        filelist.sort()
        for f in filelist:
            self.append(f)

class FileIconView(Gtk.IconView):

    def __init__(self, model):
        Gtk.IconView.__init__(self, model)

        self.props.column_spacing = 2
        self.props.item_padding = 0
        self.props.row_spacing = 2
        self.props.item_width = 70
        self.set_model(model)
        self.set_pixbuf_column(COLUMN_PIXBUF)
        self.set_text_column(COLUMN_PATH)

        self.enable_model_drag_source(Gdk.ModifierType.BUTTON1_MASK,
                                    [],
                                    DRAG_ACTION)
        self.enable_model_drag_dest([], DRAG_ACTION)

class FileInfoBar(Gtk.Frame):
    ''' Show information about selection in lower right corner '''
    def __init__(self, view):
        Gtk.Frame.__init__(self)

        self.set_valign(Gtk.Align.END)
        self.set_halign(Gtk.Align.END)
        infobox = Gtk.Box()
        infobox.override_background_color(Gtk.StateType.NORMAL,
                                          Gdk.RGBA(1.0,1.0,1.0,1.0))

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
            self.sizeinfo.set_text("(" + file_size + " Objects)")
        else:
            self.sizeinfo.set_text("(" + self.human_readable_size(int(file_size)) + ")")

    def human_readable_size(self, size, precision=1):
        
        suffixes=['Bytes','kB','MB','GB','TB']
        suffixIndex = 0
        while size > 1024 and suffixIndex < 4:
            suffixIndex += 1
            size = size/1024.0
        return "%.*f %s"%(precision, size, suffixes[suffixIndex])

class BrickFiler(object):
    '''
    file explorer for NXT- and EV3-bricks
    '''
    TARGETS = []

    def __init__(self, application, *args, **kwargs):

        self.app = application

        self.window = Gtk.Window(title = "Brick-Filer")
        self.window.set_application(application)
        self.window.set_default_size(640,480)
        self.window.set_border_width(6)

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Brick-Filer"
        self.window.set_titlebar(hb)

        hpaned = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)
        hpaned.set_position(300)

        # Look for Brick
        self.brick_type = None
        if self.app.nxtbrick:
            logger.info('got app.nxtbrick')
            self.brick_type = 'nxt'
        else:
            logger.info('no app.nxtbrick')

        if self.app.ev3brick:
            logger.info('got app.ev3brick')
            self.brick_type = 'ev3'
        else:
            logger.info('no app.ev3brick')

        if self.brick_type == 'nxt':
            self.nxt_model = BrickListing(self.app.nxtbrick, self.brick_type,
                                          '*.*')
            hpaned.add1(self.make_brickfile_panel(str(self.app.nxtbrick.sock),
                                                  self.nxt_model))
        elif self.brick_type == 'ev3':
            self.current_ev3_directory = self.app.settings.get_string('prjsstore')
            #self.current_ev3_directory = self.window.get_application().settings.get_string('prjsstore')
            #AttributeError: 'MindEdApp' object has no attribute 'settings'
            #self.current_ev3_directory = '/home/root/lms2012/prjs'
            self.ev3_model = BrickListing(self.app.ev3brick, self.brick_type,
                                          self.current_ev3_directory)
            hpaned.add1(self.make_brickfile_panel('EV3', self.ev3_model))
        else:
            self.nxt_model = BrickListing(None, None, None)
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

        host_view.drag_source_add_uri_targets()
        host_view.connect("drag_data_get", self.drag_data_get_hostdata)

        host_view.drag_dest_add_text_targets()
        host_view.connect("drag_data_received", self.drag_data_received_nxtdata)

        return host_view

    def make_brickfile_list(self, model):

        brick_view = FileIconView(model)
        brick_view.connect("item-activated", self.on_brick_item_activated)
        brick_view.connect("selection-changed", self.on_nxt_selection_changed)
        
        brick_view.drag_source_add_text_targets()
        brick_view.connect("drag_data_get", self.drag_data_get_data)
        
        brick_view.drag_dest_add_uri_targets()
        brick_view.connect("drag_data_received", self.drag_data_received_data)

        return brick_view

    def make_hostfile_panel(self, model):
        v = Gtk.VBox()

        # Location bar
        location_bar = Gtk.Grid()
        self.upButton = Gtk.Button()
        icon = Gio.ThemedIcon(name="go-previous-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        self.upButton.add(image)
        self.upButton.connect("clicked", self.on_prev_dir_clicked)
        location_bar.attach(self.upButton, 0, 0, 1, 1,)
        self.location = Gtk.Entry()
        self.location.set_hexpand(True)
        self.location.set_text(self.current_directory)
        self.location.set_icon_from_icon_name(0, 'folder-symbolic')
        location_bar.attach(self.location, 1, 0, 1, 1)
        v.pack_start(location_bar, False, False, 0)

        self.host_view = self.make_hostfile_list(model)

        overlay = Gtk.Overlay()
        s = Gtk.ScrolledWindow()
        s.set_border_width(2)
        s.add(self.host_view)
        overlay.add(s)

        self.hostinfoframe = FileInfoBar(self.host_view)
        overlay.add_overlay(self.hostinfoframe)
        v.pack_start(overlay, True, True, 0)

        return v

    def make_brickfile_panel(self, name, model):
        v = Gtk.VBox()
        #v.pack_start(Gtk.Label(name), False, False, 0)
        tool_bar = Gtk.Grid()
        self.delButton = Gtk.Button()
        icon = Gio.ThemedIcon(name="user-trash-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        self.delButton.add(image)
        self.delButton.set_tooltip_text("delete")
        self.delButton.connect("clicked", self.on_delete_clicked)
        self.delButton.drag_dest_set(Gtk.DestDefaults.ALL, [], DRAG_ACTION)
        self.delButton.drag_dest_add_text_targets()
        self.delButton.connect("drag_data_received", self.drag_data_received_nxtdeldata)
        tool_bar.attach(self.delButton, 0, 0, 1, 1)

        if self.brick_type == 'ev3':
            self.EV3upButton = Gtk.Button()
            icon = Gio.ThemedIcon(name="go-previous-symbolic")
            image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
            self.EV3upButton.add(image)
            self.EV3upButton.connect("clicked", self.on_EV3_prev_dir_clicked)
            tool_bar.attach(self.EV3upButton, 1, 0, 1, 1,)
            self.ev3location = Gtk.Entry()
            self.ev3location.set_hexpand(True)
            self.ev3location.set_text(self.current_ev3_directory)
            self.ev3location.set_icon_from_icon_name(0, 'folder-symbolic')
            tool_bar.attach(self.ev3location,2 , 0, 1, 1)
        v.pack_start(tool_bar, False, False, 0)

        self.brick_view = self.make_brickfile_list(model)

        overlay = Gtk.Overlay()
        s = Gtk.ScrolledWindow()
        s.set_border_width(2)
        s.add(self.brick_view)
        overlay.add(s)

        self.brickinfoframe = FileInfoBar(self.brick_view)
        overlay.add_overlay(self.brickinfoframe)
        v.pack_start(overlay, True, True, 0)

        return v

    def on_host_item_activated(self, widget, item):
        '''double click on directory opens it'''

        model = widget.get_model()
        path = model[item][COLUMN_PATH]
        isDir = model[item][COLUMN_ISDIR]

        if not isDir:
            return

        self.current_directory = str(Path(self.current_directory, path))
        self.location.set_text(self.current_directory)
        self.host_model.populate(self.current_directory)
        self.upButton.set_sensitive(True)

    def on_brick_item_activated(self, widget, item):
        '''double click on EV3 directory opens it'''
        model = widget.get_model()
        path = model[item][COLUMN_PATH]
        isDir = model[item][COLUMN_ISDIR]
        logger.debug('double click on {}, isDir {}'.format(path, isDir))
        if self.brick_type == 'ev3' and isDir:
            self.current_ev3_directory = str(Path(self.current_ev3_directory, path))
            self.ev3_model.populate(self.app.ev3brick, self.current_ev3_directory)
            self.ev3location.set_text(self.current_ev3_directory)
            if not self.EV3upButton.get_sensitive():
                self.EV3upButton.set_sensitive(True)
            if self.current_ev3_directory.startswith('/home/root/lms2012/prjs'):
                if not self.delButton.get_sensitive():
                    self.delButton.set_sensitive(True)
        # NXT has no directories

    def on_host_selection_changed(self, widget):
        try:
            iter_path = widget.get_selected_items()[0]
            self.hostinfoframe.update(widget)
            self.hostinfoframe.show()
        except:
            self.hostinfoframe.hide()

    def on_nxt_selection_changed(self, widget):
        try:
            iter_path = widget.get_selected_items()[0]
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
        if self.current_directory == "/": sensitive = False
        self.upButton.set_sensitive(sensitive)

    def on_EV3_prev_dir_clicked(self, widget):
        '''walk one EV3 directory higher'''
        self.current_ev3_directory = str(Path(self.current_ev3_directory).parent)
        self.ev3_model.populate(self.app.ev3brick, self.current_ev3_directory)
        self.ev3location.set_text(self.current_ev3_directory)
        sensitive = True
        if self.current_ev3_directory == "/": sensitive = False
        self.EV3upButton.set_sensitive(sensitive)
        if not self.current_ev3_directory.startswith('/home/root/lms2012/prjs'):
            if self.delButton.get_sensitive():
                self.delButton.set_sensitive(False)

    def drag_data_get_data(self, iconview, context, selection, target_id,
                           etime):
        '''set the selected NXT-file to copy to host'''
        
        selected_path = iconview.get_selected_items()[0]
        selected_iter = iconview.get_model().get_iter(selected_path)
        file_name = iconview.get_model().get_value(selected_iter, COLUMN_PATH)
        success = selection.set_text(file_name, -1)
        if logger.isEnabledFor(logging.DEBUG):
            if success: 
                logger.debug(selection.get_text())
            else:
                logger.debug('selection set text NOT okay')

    def drag_data_get_hostdata(self, iconview, context, selection, target_id,
                               etime):
        '''set the selected uri to copy to NXT-brick'''

        selected_path = iconview.get_selected_items()[0]
        selected_iter = iconview.get_model().get_iter(selected_path)
        name = iconview.get_model().get_value(selected_iter, COLUMN_PATH)
        file_uris = [Path(self.current_directory, name).as_uri()]
        logger.debug('dragged: %s' % file_uris)
        success = selection.set_uris(file_uris)
        if logger.isEnabledFor(logging.DEBUG):
            if success: 
                logger.debug('selection set uris okay')
            else:
                logger.debug('selection set uris NOT okay')

    def drag_data_received_data(self, iconview, context, x, y, selection,
                                info, etime):
        '''write file to brick from host '''
        file_uris = selection.get_uris()

        if context.get_actions() == DRAG_ACTION:
            logger.debug(context.get_actions())
            if self.brick_type == 'nxt':
                # Accept only these files (File write)
                # Download firmware              *.rfw
                # Download user defined programs *.rxe
                # OnBrick programming            *.rpg
                # Try-Me programs                *.rtm
                # Sound                          *.rso
                # Graphics                       *.ric
                ext = ['.rxe', '.rso', '.ric', '.rtm', 'rpg']
                for f in file_uris:
                    if f.endswith(tuple(ext)):
                        logger.debug('dropped: %s' % file_uris)
                        wnames = write_files(self.app.nxtbrick, file_uris) # returns ('fname', 'size')
                        self.nxt_model.populate(self.app.nxtbrick, '*.*')
                        context.finish(True, False, etime) 
                        return
                    else:
                        logger.debug("don't want %s" % file_uris)
                        # TODO: Give feedback
                        #bar = gtk.InfoBar()
                        #vb.pack_start(bar, False, False)
                        #bar.set_message_type(gtk.MESSAGE_INFO)
                        #bar.get_content_area().pack_start(
                        #gtk.Label("What shall I do with this?"), False, False)
                        context.finish(False, False, etime)
                        return
            if (self.brick_type == 'ev3' and
                self.current_ev3_directory.startswith('/home/root/lms2012/prjs')):
                for f in file_uris:
                    # TODO: which files will we accept?
                    file_path = urlparse(unquote(f))
                    file_name = Path(file_path.path).name
                    infile = str(Path(self.current_ev3_directory, Path(file_path.path).name))
                    outfile = file_path.path
                    logger.debug('dropped: %s' % outfile)
                    logger.debug('write to: %s' % infile)
                    data = open(outfile, 'rb').read()
                    self.app.ev3brick.write_file(infile, data)
                    self.ev3_model.populate(self.app.ev3brick, self.current_ev3_directory)
                    context.finish(True, False, etime) 
                    return
        else:
            logger.debug('what happend?')
            logger.debug(context.get_actions())
            context.finish(False, False, etime)
            return

    def drag_data_received_nxtdata(self, iconview, context, x, y, selection,
        info, etime):
        '''read file from NXT-brick and write to host '''
        file_name = selection.get_text()

        if context.get_actions() == DRAG_ACTION:
            logger.debug(context.get_actions())
            logger.debug(selection.get_text())
            logger.debug(self.current_directory)
            file_uri = Path(self.current_directory, file_name).as_uri()
            nxtfile = read_file(self.app.nxtbrick, file_uri)
            self.host_model.populate(self.current_directory)
            context.finish(True, False, etime)
            return
        else:
            logger.debug('what happend?')
            logger.debug(context.get_actions())
            context.finish(False, False, etime)

    def drag_data_received_nxtdeldata(self, iconview, context, x, y, selection,
        info, etime):
        '''delete button as drag target'''
        file_name = selection.get_text()
        logger.debug('selected to delete: %s' % file_name)

        if self.brick_type == 'nxt':
            if context.get_actions() == DRAG_ACTION:
                try:
                    self.app.nxtbrick.delete(file_name)
                    logger.debug('deleted: %s' % file_name)
                    self.nxt_model.populate(self.app.nxtbrick, '*.*')
                    context.finish(True, False, etime)
                    return
                except:
                    logger.debug('File not deleted')
            else:
                context.finish(False, False, etime)

        if self.brick_type == 'ev3':
            logger.debug('Drag del EV3 TODO')

    def on_delete_clicked(self, button):
        ''' delete file on brick'''
        if self.brick_type == 'nxt':
            if len(self.nxt_model) != 0:
                iter_path = self.brick_view.get_selected_items()[0]
                model = self.brick_view.get_model()
                selected_iter = model.get_iter(iter_path)
                if selected_iter is not None:
                    file_name = model.get_value(selected_iter, 0)
                    logger.debug('selected to delete: %s' % file_name)
                    try:
                        self.app.nxtbrick.delete(file_name)
                        logger.debug('deleted: %s' % file_name)
                        model.remove(selected_iter)
                    except:
                        logger.debug('File not deleted')
                else:
                    logger.debug('No file selected')

        if self.brick_type == 'ev3':
            if len(self.ev3_model) != 0 and self.brick_view.get_selected_items():
                iter_path = self.brick_view.get_selected_items()[0]
                model = self.brick_view.get_model()
                selected_iter = model.get_iter(iter_path)
                if selected_iter is not None:
                    file_name = str(Path(self.current_ev3_directory,
                                         model.get_value(selected_iter, COLUMN_PATH)))
                    logger.debug('selected to delete: {}'.format(file_name))
                    if model.get_value(selected_iter, COLUMN_ISDIR):
                        # is Dir
                        try:
                            self.app.ev3brick.del_dir(file_name)
                            logger.debug('Directory {} deleted'.format(file_name))
                            model.remove(selected_iter)
                        except:
                            logger.debug('Directory not deleted')
                    else:
                        # is File
                        try:
                            self.app.ev3brick.del_file(file_name)
                            logger.debug('deleted: %s' % file_name)
                            model.remove(selected_iter)
                        except:
                            logger.debug('File not deleted')
                else:
                    logger.debug('No file selected')

    def quit(self, *args):
        'Quit the program'
        self.window.destroy()
        # needed! Else Window disappears, but App lives still.
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
