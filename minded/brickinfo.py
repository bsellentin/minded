#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import Gtk, Gdk, Gio, GObject

import logging
logger = logging.getLogger(__name__)

import nxt.locator
import nxt.brick

class BrickInfo(object):

    def __init__(self, application, *args, **kwargs):

        self.app = application
        builder = Gtk.Builder()
        builder.add_from_resource('/org/gge-em/MindEd/brickinfo.ui')
        builder.connect_signals(self)
        self.window = builder.get_object("toolwin")
        self.window.set_application(application)
        self.grid = builder.get_object("grid")
        self.window.show_all()
        self.window.connect('delete-event', self.quit)

        self.widgetlist = self.grid.get_children()

        self.widgetlist[15].set_text('Brickname')
        self.widgetlist[15].set_xalign(0)
        self.widgetlist[13].set_text('Host address:')
        self.widgetlist[13].set_xalign(0)

        self.widgetlist[5].set_text('Battery level:')
        self.widgetlist[5].set_xalign(0)

        # Look for Brick
        self.brick_type = None
        try:
            brick = self.app.nxtbrick
            logger.debug('got app.nxtbrick')
            self.brick_type = 'nxt'
        except AttributeError:
            logger.debug('no app.nxtbrick')    

        try:
            brick = self.app.ev3brick
            logger.debug('got app.ev3brick')
            self.brick_type = 'ev3'
        except AttributeError:
            logger.debug('no app.ev3brick')

        self.get_brickinfo()

    def get_brickinfo(self):

        if self.brick_type == 'nxt':
            try:
                name, host, signal_strength, user_flash = self.app.nxtbrick.get_device_info()
                self.widgetlist[14].set_text(name)
                self.widgetlist[14].set_xalign(0)
                logger.debug('NXT brick name: %s' % (name))
                self.widgetlist[12].set_text(host)
                self.widgetlist[12].set_xalign(0)
                logger.debug('Host address: %s' % host)
                self.widgetlist[11].set_text('BT signal strength:')
                self.widgetlist[11].set_xalign(0)
                self.widgetlist[10].set_text(str(signal_strength))
                self.widgetlist[10].set_xalign(0)
                logger.debug('Bluetooth signal strength: %s' % signal_strength)
                self.widgetlist[9].set_text('Free user flash:')
                self.widgetlist[9].set_xalign(0)
                self.widgetlist[8].set_text(str(user_flash))
                self.widgetlist[8].set_xalign(0)
                logger.debug('Free user flash: %s' % user_flash)
                prot_version, fw_version = self.app.nxtbrick.get_firmware_version()
                self.widgetlist[7].set_text('Protocol version:')
                self.widgetlist[7].set_xalign(0)
                logger.debug('Protocol version %s.%s' % prot_version)
                self.widgetlist[6].set_text(('%s.%s' % prot_version))
                self.widgetlist[6].set_xalign(0)

                volts = self.app.nxtbrick.get_battery_level()/1000
                self.widgetlist[4].set_text(('%1.2f V' % volts))
                self.widgetlist[4].set_xalign(0)
                logger.debug('Battery level %s V' % volts)
                self.widgetlist[3].set_text('Firmware version:')
                self.widgetlist[3].set_xalign(0)
                self.widgetlist[2].set_text(('%s.%s' % fw_version))
                self.widgetlist[2].set_xalign(0)
                logger.debug('Firmware version %s.%s' % fw_version)

            except:
                logger.debug('error getting nxt-brick info')
        if self.brick_type == 'ev3':
            #try:
            self.app.ev3brick.usb_ready()
            name = self.app.ev3brick.get_brickname()
            (hw_version, fw_version, os_version, free_mem) = self.app.ev3brick.get_brickinfo()
            self.widgetlist[14].set_text(name)
            self.widgetlist[14].set_xalign(0)
            self.widgetlist[12].set_text('no WIFI')
            self.widgetlist[12].set_xalign(0)
            self.widgetlist[11].set_text('Brick Hardware:')
            self.widgetlist[11].set_xalign(0)
            self.widgetlist[10].set_text(hw_version)
            self.widgetlist[10].set_xalign(0)
            self.widgetlist[9].set_text('OS version:')
            self.widgetlist[9].set_xalign(0)
            self.widgetlist[8].set_text(os_version)
            self.widgetlist[8].set_xalign(0)
            self.widgetlist[7].set_text('Battery level:')
            self.widgetlist[7].set_xalign(0)
            self.widgetlist[6].set_text('%s V' % self.app.ev3brick.get_vbatt())
            self.widgetlist[6].set_xalign(0)
            self.widgetlist[5].set_text('Free user flash:')
            self.widgetlist[5].set_xalign(0)
            self.widgetlist[4].set_text('%d KB' % free_mem)
            self.widgetlist[4].set_xalign(0)
            self.widgetlist[3].set_text('Firmware version:')
            self.widgetlist[3].set_xalign(0)
            self.widgetlist[2].set_text(fw_version)
            self.widgetlist[2].set_xalign(0)

            #except: 
                #logger.debug('error getting ev3-brick info')

    def on_btn_brickname_clicked(self, button):

        dlg = Gtk.Dialog()
        dlg.set_title("Enter new brick name:")
        dlg.set_transient_for(self.window)
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
        logger.debug('response is %s' % response)
        if response == Gtk.ResponseType.OK:
            logger.debug(name.get_text())
            if self.brick_type == 'nxt':
                self.app.nxtbrick.set_brick_name(name.get_text())
            if self.brick_type == 'ev3':
                self.app.ev3brick.set_brickname(name.get_text())
            self.get_brickinfo()

        elif response == Gtk.ResponseType.CANCEL:
            pass
        elif response == Gtk.ResponseType.DELETE_EVENT:
            pass
        widget.destroy()

    def on_btn_firmware_clicked(self, button):
        pass

    def on_btn_refresh_clicked(self, button):
        logger.debug('refresh clicked')
        try:
            self.get_brickinfo()
        except:
            logger.warning('no app.brick')

    def quit(self, *args):
        'Quit the program'
        self.window.destroy()
        # needed! Else Window disappears, but App lives still.
        return True
