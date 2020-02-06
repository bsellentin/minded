#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Show information available from brick '''

import logging

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import Gtk

from minded.minded_fwupdate import NxtFirmwareUpdate

LOGGER = logging.getLogger(__name__)


class BrickInfo():

    def __init__(self, application):

        self.app = application
        builder = Gtk.Builder()
        builder.add_from_resource('/org/gge-em/MindEd/minded-brickinfo.ui')
        builder.connect_signals(self)
        self.window = builder.get_object("toolwin")
        self.window.set_application(application)
        self.grid = builder.get_object("grid")
        self.window.show_all()
        self.window.connect('delete-event', self.quit)

        self.widgetlist = self.grid.get_children()

        # Look for Brick
        self.brick_type = None
        if self.app.nxt_brick:
            LOGGER.debug('got app.nxt_brick')
            self.brick_type = 'nxt'
        else:
            LOGGER.debug('no app.nxt_brick')

        if self.app.ev3_brick:
            LOGGER.debug('got app.ev3_brick')
            self.brick_type = 'ev3'
        else:
            LOGGER.debug('no app.ev3_brick')

        self.get_brickinfo()

    def get_brickinfo(self):
        ''' get name, fimware-version, free memory etc. '''
        if self.brick_type == 'nxt':
            #try:
            name, host, signal_strength, user_flash = self.app.nxt_brick.get_device_info()
            prot_version, fw_version = self.app.nxt_brick.get_firmware_version()
            volts = self.app.nxt_brick.get_battery_level()/1000

            nxclist = [('%s.%s' % fw_version), 'Firmware version:',
                       ('%1.2f V' % volts), 'Battery level:',
                       ('%s.%s' % prot_version), 'Protocol version:',
                       ('%s' % user_flash), 'Free user flash:',
                       ('%s' % signal_strength), 'BT signal strength:',
                       host, 'Host address:',
                       name, 'Brickname']
            for x in range(2, 15):
                self.widgetlist[x].set_text(nxclist[x-2])

            #except:
                #LOGGER.debug('error getting nxt-brick info')

        if self.brick_type == 'ev3':
            #try:
            self.app.ev3_brick.usb_ready()
            name = self.app.ev3_brick.get_brickname()
            (hw_version, fw_version, os_version, free_mem) = self.app.ev3_brick.get_brickinfo()
            volts = self.app.ev3_brick.get_vbatt()

            evclist = [fw_version, 'Firmware version:',
                       ('%d KB' % free_mem), 'Free user flash:',
                       ('%s V' % volts), 'Battery level:',
                       os_version, 'OS version:',
                       hw_version, 'Brick Hardware:',
                       'no WIFI', 'Host address:',
                       name, 'Brickname']
            for x in range(2, 15):
                self.widgetlist[x].set_text(evclist[x-2])

            #except:
                #LOGGER.debug('error getting ev3-brick info')

    def on_btn_brickname_clicked(self, button):
        ''' rename brick '''
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
        ok_button = dlg.get_widget_for_response(response_id=Gtk.ResponseType.OK)
        ok_button.set_can_default(True)
        ok_button.grab_default()

        content_area = dlg.get_content_area()
        content_area.add(name)

        dlg.connect("response", self.on_dlg_brickname_response, name)
        dlg.show_all()

    def on_dlg_brickname_response(self, widget, response, name):
        LOGGER.debug('response is %s' % response)
        if response == Gtk.ResponseType.OK:
            LOGGER.debug(name.get_text())
            if self.brick_type == 'nxt':
                self.app.nxt_brick.set_brick_name(name.get_text())
            if self.brick_type == 'ev3':
                self.app.ev3_brick.set_brickname(name.get_text())
            self.get_brickinfo()

        elif response == Gtk.ResponseType.CANCEL:
            pass
        elif response == Gtk.ResponseType.DELETE_EVENT:
            pass
        widget.destroy()

    def on_btn_firmware_clicked(self, button):
        if self.brick_type == 'nxt':
            dlg = NxtFirmwareUpdate(self.app)
        else:
            pass

    def on_btn_refresh_clicked(self, button):
        ''' reload brick-info '''
        LOGGER.debug('refresh clicked')
        try:
            self.get_brickinfo()
        except:
            LOGGER.warning('no app.brick')

    def quit(self, *args):
        'Quit the program'
        self.window.destroy()
        # needed! Else Window disappears, but App lives still.
        return True
