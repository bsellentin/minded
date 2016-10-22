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

import os
import urllib.request
import sys
import pathlib
from urllib.parse import urlparse, unquote

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


(COLUMN_PATH, COLUMN_PIXBUF, COLUMN_SIZE, COLUMN_ISDIR) = range(4)

DRAG_ACTION = Gdk.DragAction.COPY

debug = 0

def read_file(brick, file_uri):
    
    file_path = urlparse(unquote(file_uri))
    file_name = pathlib.Path(file_path.path).name
    
    with FileReader(brick, file_name) as r:
        with open(file_path.path, 'wb') as f:
            for data in r:
                f.write(data)

def write_file(brick, file_name, data):
    w = FileWriter(brick, file_name, len(data))
    if debug: print('Pushing %s (%d bytes) ...' % (file_name, w.size)) 
    sys.stdout.flush()
    w.write(data)
    if debug: print('wrote %d bytes' % len(data))
    w.close()
        
def write_files(brick, file_uris):
    wnames = []
    for file_uri in file_uris:
        if file_uri:
            if debug: print('File: %s Type %s' % (file_uri, type(file_uri)))
            file_path = urlparse(unquote(file_uri))
            file_name = pathlib.Path(file_path.path).name
            
            url = urllib.request.urlopen(file_uri)
            try:
                data = url.read()
            finally:
                url.close()
            if debug: print('name %s, size: %d ' % (file_name, len(data)))
            try:
                write_file(brick, file_name, data)
                wnames.append((file_name, str(len(data))))
            except:
                pass
    return wnames


class NXTListing(Gtk.ListStore):

    def __init__(self, brick):
        Gtk.ListStore.__init__(self, str, Pixbuf, str, bool)
        self.set_sort_column_id(0, 0)
        
        self.fileIcon = Gtk.IconTheme.get_default().load_icon('ascii', 64, 0)
        self.audioIcon = Gtk.IconTheme.get_default().load_icon('sound', 64, 0)
        self.graphicIcon = Gtk.IconTheme.get_default().load_icon('image', 64, 0)
        self.execIcon = Gtk.IconTheme.get_default().load_icon('exec', 64, 0)
        
        if brick:
            self.populate(brick, '*.*')

    def populate(self, brick, pattern):

        self.clear()
        
        f = FileFinder(brick, pattern)
        for (fname, size) in f:
            # exclude NVconfig.sys?
            if os.path.splitext(fname)[-1] == ".rso":
                treeiter = self.append((fname, self.audioIcon, str(size), False))
            elif os.path.splitext(fname)[-1] == ".ric":
                treeiter = self.append((fname, self.graphicIcon, str(size), False))
            elif os.path.splitext(fname)[-1] in [".rxe", ".rtm"]:
                treeiter = self.append((fname, self.execIcon, str(size), False))
            else:
                treeiter = self.append((fname, self.fileIcon, str(size), False))
        if debug:
            for row in self:
                print(row[COLUMN_PATH,COLUMN_SIZE])

class HostListing(Gtk.ListStore):

    def __init__(self, path):
        Gtk.ListStore.__init__(self, str, Pixbuf, str, bool)
        
        self.dirIcon = Gtk.IconTheme.get_default().load_icon('folder', 64, 0)
        self.fileIcon = Gtk.IconTheme.get_default().load_icon('ascii', 64, 0)
        self.audioIcon = Gtk.IconTheme.get_default().load_icon('sound', 64, 0)
        self.graphicIcon = Gtk.IconTheme.get_default().load_icon('image', 64, 0)
        self.execIcon = Gtk.IconTheme.get_default().load_icon('exec', 64, 0)
        
        self.populate(path)
        
    def populate(self, path):
        
        self.clear()
        
        dirlist = []
        filelist = []
        
        for fl in os.listdir(path):
            if not fl[0] == '.':
                if os.path.isdir(os.path.join(path, fl)):
                    dirlist.append([fl, self.dirIcon, 
                            str(len([name for name in os.listdir(os.path.join(path, fl))])), True])
                elif os.path.isfile(os.path.join(path, fl)):
                    if os.path.splitext(os.path.join(path, fl))[1] == '.rso':
                        filelist.append([fl, self.audioIcon,
                            str(os.stat(os.path.join(path, fl)).st_size), False])
                    elif os.path.splitext(os.path.join(path, fl))[1] == ".ric":
                        filelist.append([fl, self.graphicIcon,
                            str(os.stat(os.path.join(path, fl)).st_size), False])
                    elif os.path.splitext(os.path.join(path, fl))[1] == ".rxe":
                        filelist.append([fl, self.execIcon,
                            str(os.stat(os.path.join(path, fl)).st_size), False])
                    else:
                        filelist.append([fl, self.fileIcon, 
                            str(os.stat(os.path.join(path, fl)).st_size), False])
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
        infobox.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(1.0,1.0,1.0,1.0))
        
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

class NXT_Filer(object):
    TARGETS = []

    def __init__(self, application, *args, **kwargs):
        # args is tuple of tuples
        if any("debug" in arg for arg in args):
            global debug
            debug = True
        
        self.window = Gtk.Window(title = "NXT Filer")
        self.window.set_application(application)
        self.window.set_default_size(640,480)
        self.window.set_border_width(6)
        
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "NXT Filer"
        self.window.set_titlebar(hb)
        
        hpaned = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)
        hpaned.set_position(300)
                
        # Look for Brick
        found = False
        self.nxt_info_open = False
        for device in application.client.query_by_subsystem("usb"):
            # if device.get_property('ID_MODEL_FROM_DATABASE') == "Mindstorms NXT": # is 2x true!
            if device.get_property('ID_VENDOR') == '0694' and device.get_property('ID_MODEL') == '0002':
                if debug:
                    for device_key in device.get_property_keys():
                        print("   device property %s: %s"  % (device_key, 
                              device.get_property(device_key)))
                try:
                    #self.brick = nxt.locator.find_one_brick(keyword_arguments.get('host',None))
                    try:
                        self.brick = application.win.nxt_info.brick
                        print('got nxtinfo.brick')
                        self.nxt_info_open = True
                    except:
                        print('no nxtinfo.brick')    
                        self.brick = nxt.locator.find_one_brick()
                    found = True
                except:
                    print('nxt-python failure')
       
        if found:
            self.nxt_model = NXTListing(self.brick)
            hpaned.add1(self.make_nxtfile_panel(str(self.brick.sock), self.nxt_model))
        else:    
            self.nxt_model = NXTListing(None)
            hpaned.add1(self.make_nxtfile_panel('No brick', self.nxt_model))

        self.current_directory = os.path.expanduser("~")
        self.host_model = HostListing(self.current_directory)
        hpaned.add2(self.make_hostfile_panel(self.host_model))

        self.window.add(hpaned)
        self.window.show_all()
        self.hostinfoframe.hide()
        self.nxtinfoframe.hide()
        self.window.connect('delete-event', self.quit)
        
    def make_hostfile_list(self, model):
        
        host_view = FileIconView(model)
        host_view.connect("item-activated", self.on_item_activated)
        host_view.connect("selection-changed", self.on_host_selection_changed)
        
        host_view.drag_source_add_uri_targets()
        host_view.connect("drag_data_get", self.drag_data_get_hostdata)
        
        host_view.drag_dest_add_text_targets()
        host_view.connect("drag_data_received", self.drag_data_received_nxtdata)
        
        return host_view
        
    def make_nxtfile_list(self, model):

        nxt_view = FileIconView(model)
        nxt_view.connect("selection-changed", self.on_nxt_selection_changed)
        
        nxt_view.drag_source_add_text_targets()
        nxt_view.connect("drag_data_get", self.drag_data_get_data)
        
        nxt_view.drag_dest_add_uri_targets()
        nxt_view.connect("drag_data_received", self.drag_data_received_data)

        return nxt_view

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
    
    def make_nxtfile_panel(self, name, model):
        v = Gtk.VBox()
        #v.pack_start(Gtk.Label(name), False, False, 0)
        tool_bar = Gtk.Grid()
        button = Gtk.Button()
        icon = Gio.ThemedIcon(name="user-trash-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button.add(image)
        button.set_tooltip_text("delete")
        button.connect("clicked", self.on_delete_clicked)
        tool_bar.attach(button, 0, 0, 1, 1)
        v.pack_start(tool_bar, False, False, 0)
        
        self.nxt_view = self.make_nxtfile_list(model)
        
        overlay = Gtk.Overlay()
        s = Gtk.ScrolledWindow()
        s.set_border_width(2)
        s.add(self.nxt_view)
        overlay.add(s)
        
        self.nxtinfoframe = FileInfoBar(self.nxt_view)
        overlay.add_overlay(self.nxtinfoframe)
        v.pack_start(overlay, True, True, 0)
        
        return v

    def on_item_activated(self, widget, item):
        '''double click on directory opens it'''

        model = widget.get_model()
        path = model[item][COLUMN_PATH]
        isDir = model[item][COLUMN_ISDIR]
        
        if not isDir:
            return
            
        self.current_directory = os.path.join(self.current_directory, path)
        self.location.set_text(self.current_directory)
        self.host_model.populate(self.current_directory)
        self.upButton.set_sensitive(True)

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
            self.nxtinfoframe.update(widget)
            self.nxtinfoframe.show()
        except:
            self.nxtinfoframe.hide()        
            
    def on_prev_dir_clicked(self, widget):
        '''walk one directory higher'''

        self.current_directory = os.path.dirname(self.current_directory)
        self.location.set_text(self.current_directory)
        self.host_model.populate(self.current_directory)
        sensitive = True
        if self.current_directory == "/": sensitive = False
        self.upButton.set_sensitive(sensitive)
    
    def drag_data_get_data(self, iconview, context, selection, target_id,
        etime):
        '''set the selected NXT-file to copy to host'''
        
        selected_path = iconview.get_selected_items()[0]
        selected_iter = iconview.get_model().get_iter(selected_path)
        file_name = iconview.get_model().get_value(selected_iter, COLUMN_PATH)
        success = selection.set_text(file_name, -1)
        if debug:
            if success: 
                print(selection.get_text())
            else:
                print('selection set text NOT okay')
                
    def drag_data_get_hostdata(self, iconview, context, selection, target_id,
        etime):
        '''set the selected uri to copy to NXT-brick'''

        selected_path = iconview.get_selected_items()[0]
        selected_iter = iconview.get_model().get_iter(selected_path)
        name = iconview.get_model().get_value(selected_iter, COLUMN_PATH)
        file_name = os.path.join(self.current_directory, name)
        if debug: print(file_name)
        file_uris = [pathlib.Path(file_name).as_uri()]
        if debug: print('dragged: %s' % file_uris)
        success = selection.set_uris(file_uris)
        if debug:
            if success: 
                print('selection set uris okay')
            else:
                print('selection set uris NOT okay')
        
    def drag_data_received_data(self, iconview, context, x, y, selection,
        info, etime):
        '''write file to NXT-brick data from host '''
        file_uris = selection.get_uris()

        # Download files (File write)
        # Download firmware              *.rfw
        # Download user defined programs *.rxe
        # OnBrick programming            *.rpg
        # Try-Me programs                *.rtm
        # Sound                          *.rso
        # Graphics                       *.ric
        
        if context.get_actions() == DRAG_ACTION:
            if debug: print(context.get_actions())
        
            ext = ['.rxe', '.rso', '.ric', '.rtm', 'rpg']
            for f in file_uris:
                if f.endswith(tuple(ext)):
                    if debug: print('dropped: %s' % file_uris)
                    wnames = write_files(self.brick, file_uris) # returns ('fname', 'size')
                    self.nxt_model.populate(self.brick, '*.*')
                    # Gdk.DragContext.finish(success, del_, time)
                    context.finish(True, False, etime) 
                    return
                else:
                    if debug: print("don't want %s" % file_uris)
                    # TODO: Give feedback
                    #bar = gtk.InfoBar()
                    #vb.pack_start(bar, False, False)
                    #bar.set_message_type(gtk.MESSAGE_INFO)
                    #bar.get_content_area().pack_start(
                    #gtk.Label("What shall I do with this?"), False, False)
                    context.finish(False, False, etime) 
        else:
            if debug:
                print('what happend?')
                print(context.get_actions())
            context.finish(False, False, etime) 
    
    def drag_data_received_nxtdata(self, iconview, context, x, y, selection,
        info, etime):
        '''read file from NXT-brick and write to host '''
        file_name = selection.get_text()
        
        if context.get_actions() == DRAG_ACTION:
            if debug:
                print(context.get_actions())
                print(selection.get_text())
                print(self.current_directory)
            file_path = os.path.join(self.current_directory, file_name)
            file_uri = pathlib.Path(file_path).as_uri()
            nxtfile = read_file(self.brick, file_uri)
            self.host_model.populate(self.current_directory)
            context.finish(True, False, etime)
            return
        else:
            if debug:
                print('what happend?')
                print(context.get_actions())
            context.finish(False, False, etime)

    def on_delete_clicked(self, button):
        ''' delete file on NXT-brick'''
        if len(self.nxt_model) != 0:
            
            iter_path = self.nxt_view.get_selected_items()[0]
            model = self.nxt_view.get_model()
            selected_iter = model.get_iter(iter_path)
            #if iter_path is not None:
            if selected_iter is not None:
                file_name = model.get_value(selected_iter, 0)
                if debug: print('selected to delete: %s' % file_name)
                try:
                    self.brick.delete(file_name)
                    if debug: print('deleted: %s' % file_name)
                    model.remove(selected_iter)
                except:
                    print('File not deleted')
            else:
                print('No file selected')
        
    def quit(self, *args):
        'Quit the program'
        if not self.nxt_info_open:
            self.brick.sock.close()
        self.window.destroy()
        # needed! Else Window disappears, but App lives still.
        return True

