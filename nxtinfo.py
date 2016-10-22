#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import Gtk, Gdk, Gio, GObject

import nxt.locator
import nxt.brick

class NXTInfo(object):

    def __init__(self, application, *args, **kwargs):

        builder = Gtk.Builder()
        builder.add_from_file("nexttool.glade")
        builder.connect_signals(self)
        self.toolwin = builder.get_object("toolwin")
        self.toolwin.set_application(application)
        self.grid = builder.get_object("grid")
        #nameentry = builder.get_object("brickname")
        #message = builder.get_object("message")
        self.toolwin.show_all()
        self.toolwin.connect('delete-event', self.quit)
        
        self.widgetlist = self.grid.get_children()

        self.widgetlist[15].set_text('NXT brickname')
        self.widgetlist[15].set_xalign(0)
        self.widgetlist[13].set_text('Host address:')
        self.widgetlist[13].set_xalign(0)
        self.widgetlist[11].set_text('BT signal strength:')
        self.widgetlist[11].set_xalign(0)
        self.widgetlist[9].set_text('Free user flash:')
        self.widgetlist[9].set_xalign(0)
        self.widgetlist[7].set_text('Protocol version:')
        self.widgetlist[7].set_xalign(0)
        self.widgetlist[5].set_text('Firmware version:')
        self.widgetlist[5].set_xalign(0)
        self.widgetlist[3].set_text('Battery level:')
        self.widgetlist[3].set_xalign(0)
        
        self.nxt_filer_open = False
        try:
            self.brick = application.win.nxt_filer.brick
            print('got nxtfiler.brick')
            self.nxt_filer_open = True
        except:
            print('no nxtfiler.brick')    
            self.brick = nxt.locator.find_one_brick()
        # alternativ
        #for s in nxt.locator.find_bricks():
        #    print(s)
        #    self.brick = s.connect()
        self.get_brickinfo()

    def get_brickinfo(self):
        
        try:
            name, host, signal_strength, user_flash = self.brick.get_device_info()
            self.widgetlist[14].set_text(name)
            self.widgetlist[14].set_xalign(0)
            print ('NXT brick name: %s' % (name))
            self.widgetlist[12].set_text(host)
            self.widgetlist[12].set_xalign(0)
            print ('Host address: %s' % host)
            self.widgetlist[10].set_text(str(signal_strength))
            self.widgetlist[10].set_xalign(0)
            print ('Bluetooth signal strength: %s' % signal_strength)
            self.widgetlist[8].set_text(str(user_flash))
            self.widgetlist[8].set_xalign(0)
            print ('Free user flash: %s' % user_flash)
            prot_version, fw_version = self.brick.get_firmware_version()
            self.widgetlist[6].set_text(('%s.%s' % prot_version))
            self.widgetlist[6].set_xalign(0)
            print ('Protocol version %s.%s' % prot_version)
            self.widgetlist[4].set_text(('%s.%s' % fw_version))
            self.widgetlist[4].set_xalign(0)
            print ('Firmware version %s.%s' % fw_version)
            volts = self.brick.get_battery_level()/1000
            self.widgetlist[2].set_text(('%1.2f V' % volts))
            self.widgetlist[2].set_xalign(0)
            print ('Battery level %s V' % volts)
        except:
            print('error')
    
    def on_btn_brickname_clicked(self, button):
        
        dlg = Gtk.Dialog()
        dlg.set_title("Enter new brick name:")
        dlg.set_transient_for(self.toolwin)
        dlg.set_modal(True)
        dlg.add_button(button_text="Cancel", response_id=Gtk.ResponseType.CANCEL)
        dlg.add_button(button_text="OK", response_id=Gtk.ResponseType.OK)
        
        name = Gtk.Entry()
        name.set_max_length(15)
        name.set_activates_default(True)
        
        # make OK button the default
        okButton = dlg.get_widget_for_response(response_id=Gtk.ResponseType.OK)
        okButton.set_can_default(True)
        okButton.grab_default()
        
        content_area = dlg.get_content_area()
        content_area.add(name)
        
        dlg.connect("response", self.on_dlg_brickname_response, name)
        dlg.show_all()
        
    def on_dlg_brickname_response(self, widget, response, name):
        print("response is", response)
        if response == Gtk.ResponseType.OK:
            print(name.get_text())
            self.brick.set_brick_name(name.get_text())
            self.get_brickinfo()
            
        elif response == Gtk.ResponseType.CANCEL:
            pass
        elif response == Gtk.ResponseType.DELETE_EVENT:
            pass
        widget.destroy()
    
    def on_btn_firmware_clicked(self, button):
        pass

    def on_btn_refresh_clicked(self, button):
        print('refresh')
            
    def quit(self, *args):
        'Quit the program'
        if not self.nxt_filer_open:
            self.brick.sock.close()
        self.toolwin.destroy()
        # needed! Else Window disappears, but App lives still.
        return True
