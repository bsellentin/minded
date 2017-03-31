#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''MindEd - An Editor for programming LEGO Mindstorms Bricks
- NXT with NXC
- EV3 with EV3-Python
'''

import os
import sys
import argparse
import logging

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import GLib, Gio, Gtk

# for usbListener
gi.require_version('GUdev', '1.0')
from gi.repository import GUdev

from ev3 import ev3
import nxt.locator
from minded.mindedappwin import MindEdAppWin
from minded.preferences import PreferencesDialog

logger = logging.getLogger(__name__)

def make_option(long_name, short_name=None, flags=0, arg=GLib.OptionArg.NONE,
                arg_data=None, description=None, arg_description=None):
    
    option = GLib.OptionEntry()
    option.long_name = long_name
    option.short_name = 0 if not short_name else short_name
    option.flags = flags
    option.description = description
    option.arg = arg
    option.arg_description = arg_description
    option.arg_data = arg_data
    return option

class MindEdApp(Gtk.Application):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.gge-em.MindEd",
                         #flags=Gio.ApplicationFlags.FLAGS_NONE,            # argparse in main
                         flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE,   # do_commandline
                         **kwargs)
        #GLib.set_application_name("MindEd")
        #GLib.set_prgname('minded.py')
        
        # New in Gio.Application version 2.42. Older in Ubuntu Trusty
        #self.add_main_option("debug", ord("d"), GLib.OptionFlags.NONE,
        #                     GLib.OptionArg.NONE, "debugging info", None)
        
        # For Gio.Application 2.40 -> Trusty     
        self.win = None
        
        self.add_main_option_entries([
            make_option("debug", description="print a lot info")
            ])
        
    def do_startup(self):    
        Gtk.Application.do_startup(self)
        
        self.args = ()

        # look for ui-files
        srcdir = os.path.abspath(os.path.dirname(__file__))
        if os.path.exists(os.path.join(srcdir, 'data')):
            logger.warn('Running from source tree, using local ui-files')
            pkgdatadir = os.path.join(srcdir, 'data')
        else:
            pkgdatadir = '/usr/share/minded'
                
        resource_path = os.path.join(pkgdatadir, 'minded.gresource')
        resource = Gio.Resource.load(resource_path)
        Gio.Resource._register(resource)
        
        action = Gio.SimpleAction.new("preferences", None)
        action.connect("activate", self.on_preferences)
        self.add_action(action)
        
        action = Gio.SimpleAction.new("quit", None)
        action.connect("activate", self.on_quit)
        self.add_action(action)
        
        builder = Gtk.Builder()
        builder.add_from_resource('/org/gge-em/MindEd/app-menu.ui')
        self.set_app_menu(builder.get_object("appmenu"))
        
    def do_activate(self):    
        # Listen to uevent
        self.client = GUdev.Client(subsystems=["usb"])
        self.client.connect("uevent", self.on_uevent)

        # Look for brick
        for device in self.client.query_by_subsystem("usb"):
            # NXT
            if device.get_property('ID_VENDOR') == '0694' and device.get_property('ID_MODEL') == '0002':
                if logger.isEnabledFor(logging.DEBUG):
                    for device_key in device.get_property_keys():
                        logger.debug("   device property %s: %s"  % (device_key, 
                              device.get_property(device_key)))
                try:
                    #self.brick = nxt.locator.find_one_brick(keyword_arguments.get('host',None))
                    self.nxtbrick = nxt.locator.find_one_brick()
                except:
                    logger.warn('nxt-python failure')
            # EV3
            if device.get_property('ID_VENDOR_ID') == '0694' and device.get_property('ID_MODEL_ID') == '0005':
                if logger.isEnabledFor(logging.DEBUG):
                    for device_key in device.get_property_keys():
                        logger.debug("   device property %s: %s"  % (device_key, 
                              device.get_property(device_key)))
                try:
                    self.ev3brick = ev3.EV3()
                    self.ev3brick.do_nothing()
                except:
                    logger.warn('ev3-python failure')              
        
        if not self.win:
            logger.debug("NXT-lib: %s" % nxt.locator.__file__)
            self.win = MindEdAppWin(application=self)

    def do_command_line(self, command_line):

        options = command_line.get_options_dict()
        if options.contains("debug"):
            self.args += ("debug",)
            logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s', level=logging.DEBUG)
        else:
            logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s', level=logging.WARN)
       
        self.activate()
        return 0
    
    def on_uevent(self, client, action, device):
        ''' report plugin-event to application'''
        #for device_key in device.get_property_keys():
        #    print("   device property %s: %s"  % (device_key, device.get_property(device_key)))
        
        # only LEGO-devices
        if (device.get_property('ID_VENDOR') == '0694' or device.get_property('ID_VENDOR_ID') == '0694'):
            # NXT
            if device.get_property('ID_MODEL') == '0002':

                if action == "add":
                    logger.debug(' uevent: added NXT')
                    self.win.brick_status.push(self.win.brick_status_id, "NXT")
                    self.win.btn_transmit.set_sensitive(True)

                    try:
                        self.nxtbrick = nxt.locator.find_one_brick()
                    except:
                        logger.warn('nxt-python failure')

                    try:
                        self.win.nxt_filer.nxt_model.populate(self.brick, '*.*')
                    except AttributeError:
                        pass

                if action == "remove":
                    logger.debug(' uevent: removed NXT')
                    self.win.brick_status.pop(self.win.brick_status_id)
                    self.win.btn_transmit.set_sensitive(False)

                    try:
                        self.win.nxt_filer.nxt_model.clear()
                    except AttributeError:
                        pass    

            # EV3
            elif device.get_property('ID_MODEL_ID') == '0005':

                if action == "add":
                    logger.debug(' uevent: added EV3')
                    self.win.brick_status.push(self.win.brick_status_id, "EV3")
                    self.win.btn_transmit.set_sensitive(True)
                    try:
                        self.ev3brick = ev3.EV3()
                        self.ev3brick.do_nothing()
                    except:
                        logger.warn('ev3-python failure')

                if action == "remove":
                    logger.debug(' uevent: removed EV3')
                    self.win.brick_status.pop(self.win.brick_status_id)
                    self.win.btn_transmit.set_sensitive(False)
                    self.ev3brick.close()

    def on_preferences(self, action, param):
        dlg = PreferencesDialog(self.win.get_application())
        dlg.window.set_transient_for(self.win)
        dlg.window.set_modal(True)
        dlg.window.present()
        
    
    def on_quit(self, action, param):
        self.quit()
    
            
if __name__ == "__main__":
    app = MindEdApp()
    app.run(sys.argv)
