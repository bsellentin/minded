#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Preferences Dialog for MindEd'''

import os
import logging

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import Gtk, Gio, Pango

LOGGER = logging.getLogger(__name__)

class PreferencesDialog():

    def __init__(self, application):

        self.app = application
        builder = Gtk.Builder()
        builder.add_from_resource('/org/gge-em/MindEd/minded-preferences-dialog.ui')
        builder.connect_signals(self)

        self.window = builder.get_object("window1")
        self.window.set_application(application)

        # look for settings
        srcdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        LOGGER.debug('srcdir: {}'.format(srcdir))
        if os.path.exists(os.path.join(srcdir, 'data')):
            LOGGER.warning('Running from source tree, using local settings')
            schema_source = Gio.SettingsSchemaSource.new_from_directory(
                os.path.join(srcdir, 'data'), Gio.SettingsSchemaSource.get_default(), False)
            schema = Gio.SettingsSchemaSource.lookup(
                schema_source, 'org.gge-em.MindEd', False)
            LOGGER.debug('Gsettings schema: {}'.format(schema.get_path()))
            if not schema:
                raise Exception("Cannot get GSettings schema")
            settings = Gio.Settings.new_full(schema, None, None)
        else:
            settings = Gio.Settings('org.gge-em.MindEd')

        # Editor
        settings.bind('fontname', builder.get_object('font_button'),
                      'font-name', Gio.SettingsBindFlags.DEFAULT)
        settings.bind('linenumbers', builder.get_object('display_line_numbers_checkbutton'),
                      'active', Gio.SettingsBindFlags.DEFAULT)
        settings.bind('showrightmargin', builder.get_object('right_margin_checkbutton'),
                      'active', Gio.SettingsBindFlags.DEFAULT)
        settings.bind('setrightmargin', builder.get_object('right_margin_position_spinbutton'),
                      'value', Gio.SettingsBindFlags.DEFAULT)
        settings.bind('autoindent', builder.get_object('auto_indent_checkbutton'),
                      'active', Gio.SettingsBindFlags.DEFAULT)
        settings.bind('indentontab', builder.get_object('indent_on_tab_checkbutton'),
                      'active', Gio.SettingsBindFlags.DEFAULT)
        settings.bind('tabwidth', builder.get_object('tabs_width_spinbutton'),
                      'value', Gio.SettingsBindFlags.DEFAULT)
        settings.bind('spacesinsteadtab', builder.get_object('insert_spaces_checkbutton'),
                      'active', Gio.SettingsBindFlags.DEFAULT)
        settings.bind('highlightcurrentline', builder.get_object('highlight_current_line_checkbutton'),
                      'active', Gio.SettingsBindFlags.DEFAULT)
        settings.bind('highlightmatchingbrackets', builder.get_object('bracket_matching_checkbutton'),
                      'active', Gio.SettingsBindFlags.DEFAULT)
        #smartbackspace

        wrap_mode_checkbutton = builder.get_object('line_wrap_mode_checkbutton')
        wrap_mode_checkbutton.connect('toggled', self.on_wrap_mode_toggled, settings)
        if settings.get_enum('linewrapmode'):
            wrap_mode_checkbutton.set_active(True)

        # EVC
        cchooser = builder.get_object('choosec')
        cchooser.set_current_folder('/usr/bin/')
        settings.bind('armgcc', builder.get_object('cexecfile'),
                      'text', Gio.SettingsBindFlags.DEFAULT)
        settings.bind('armgplusplus', builder.get_object('cplusexecfile'),
                      'text', Gio.SettingsBindFlags.DEFAULT)
        settings.bind('cplusplus', builder.get_object('c++-compiler'),
                      'active', Gio.SettingsBindFlags.DEFAULT)

        # NXC
        settings.bind('enhancedfw', builder.get_object('use_enhanced_firmware_checkbutton'),
                      'active', Gio.SettingsBindFlags.DEFAULT)

        self.window.show_all()
        self.window.connect('delete-event', self.quit)

    def on_font_button_font_set(self, button):
        LOGGER.debug('Font set: {}'.format(button.get_font_name()))
        for pagecount in range(self.app.win.notebook.get_n_pages()-1, -1, -1):
            editor = self.app.win.notebook.get_nth_page(pagecount)
            editor.codeview.override_font(Pango.FontDescription(button.get_font_name()))

    def on_wrap_mode_toggled(self, button, settings):
        if button.get_active():
            settings.set_string('linewrapmode', 'word')
        else:
            settings.set_string('linewrapmode', 'none')


    def on_compiler_toggled(self, button):
        if button.get_active():
            state = "on"
            #if(button.get_label()=='C++-compiler'):
        else:
            state = "off"
        LOGGER.debug("Button {} was turned {}".format(button.get_label(), state))


    def quit(self, *args):
        '''Close preferences-dialog'''
        self.window.destroy()
        # needed! Else Window disappears, but App lives still.
        return True
