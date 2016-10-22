#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''MindEd - An Editor for programming LEGO Mindstorms Bricks
- NXT with NXC
- EV3 with EV3-Python
'''

import sys

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import GLib, Gio, Gtk

# for usbListener
gi.require_version('GUdev', '1.0')
from gi.repository import GUdev

import editor
import nxt.locator

DEBUGLEVEL = 1

class MindEdApp(Gtk.Application):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.brickx.minded",
                         flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE,
                         **kwargs)
        GLib.set_application_name("MindEd")
        GLib.set_prgname('minded.py')
        self.add_main_option("debug", ord("d"), GLib.OptionFlags.NONE,
                             GLib.OptionArg.NONE, "debugging info", None)
        
        self.args = ()
        self.connect("activate", self.new_window)
        
    def new_window(self, app):
        
        self.client = GUdev.Client(subsystems=["usb"])
        self.client.connect("uevent", self.on_uevent)
        
        self.win = editor.MindEdAppWin(self)
    
    def do_command_line(self, command_line):

        global debug
        options = command_line.get_options_dict()
        if options.contains("debug"):
            self.args += ("debug",)
            debug = True
        
        self.activate()
        return 0
    
    def on_uevent(self, client, action, device):

        if DEBUGLEVEL > 0:
            print("action " + action +
                  " on device " + device.get_property('ID_MODEL_FROM_DATABASE'))
            #for device_key in device.get_property_keys():
            #    print "   device property %s: %s"  % (device_key, device.get_property(device_key))
        if (action == "add" and device.get_property('ID_VENDOR') == '0694'
                            and device.get_property('ID_MODEL') == '0002'):
            self.win.brick_status.push(self.win.brick_status_id, "NXT")
            self.win.btn_transmit.set_sensitive(True)
            try:
                self.win.nxt_filer.brick = nxt.locator.find_one_brick()
                self.win.nxt_filer.nxt_model.populate(self.win.nxtfiler.brick, '*.*')
            except AttributeError:
                pass
        if (action == "remove" and device.get_property('ID_VENDOR') == '0694'
                               and device.get_property('ID_MODEL') == '0002'):
            self.win.brick_status.pop(self.win.brick_status_id)
            self.win.btn_transmit.set_sensitive(False)
            try:
                self.win.nxt_filer.nxt_model.clear()
                self.win.nxt_filer.brick.sock.close()
            except AttributeError:
                pass
                
if __name__ == "__main__":
    app = MindEdApp()
    app.run(sys.argv)
