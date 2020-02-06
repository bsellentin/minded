#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from pathlib import Path

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Vte', '2.91')
from gi.repository import Gtk, Vte, Pango, GLib

LOGGER = logging.getLogger(__name__)

class NxtFirmwareUpdate():

    def __init__(self, application):

        builder = Gtk.Builder()
        builder.add_from_resource("/org/gge-em/MindEd/minded-fwupdate.ui")
        window = builder.get_object("fw_update_win")
        window.set_application(application)
        window.set_title('NXT Firmware Update')
        builder.connect_signals(self)

        self.terminal = Vte.Terminal()
        self.terminal.set_size(80, 23)
        fontdesc = Pango.FontDescription.from_string('monospace 8')
        self.terminal.set_font(fontdesc)

        vte_box = builder.get_object('hbox_vte')
        vte_box.pack_start(self.terminal, True, True, 0)

        upload = builder.get_object('btn_upload')
        '''
        fwflash. Initial Developer of that code is John Hansen.
        Software is distributed under Mozilla Public License Version 1.1
        svn co https://svn.code.sf.net/p/bricxcc/code/
        cd code
        make -f fwflash.mak
        see: https://wiki.ubuntuusers.de/Archiv/Mindstorms/
        '''
        if Path('/usr/local/bin/fwflash').is_file():
            self.flasher = '/usr/local/bin/fwflash'
        else:
            LOGGER.debug("fwflash not found")
            upload.set_sensitive(False)

        self.fw_file = ""
        self.flashproc = ""

        window.show_all()

    def on_fwfile_set(self, button):
        LOGGER.debug(button.get_filename())
        self.fw_file = button.get_filename()

    def on_btn_cancel_clicked(self, button):
        LOGGER.debug("Cancel clicked")

    def on_btn_upload_clicked(self, button):
        LOGGER.debug("Upload clicked")

        self.terminal.spawn_sync(Vte.PtyFlags.DEFAULT,
                            str(Path.home()),
                            [self.flasher, self.fw_file],
                            [],
                            GLib.SpawnFlags.DO_NOT_REAP_CHILD,
                            None,
                            None,
                            )

