#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import Gtk, Gdk, Gio, GObject, Pango

import logging
logger = logging.getLogger(__name__)

class PreferencesDialog(object):
    def __init__(self, application, *args, **kwargs):

        self.app = application
        builder = Gtk.Builder()
        builder.add_from_resource('/org/gge-em/MindEd/minded-preferences-dialog.ui')
        builder.connect_signals(self)
        
        self.window = builder.get_object("window1")
        self.window.set_application(application)
        
        # look for settings
        srcdir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) 
        logger.debug('srcdir: %s' % srcdir)
        if os.path.exists(os.path.join(srcdir, 'data')):
            logger.warn('Running from source tree, using local settings')
            schema_source=Gio.SettingsSchemaSource.new_from_directory(os.path.join(srcdir, 'data'), 
                Gio.SettingsSchemaSource.get_default(), False)
            schema=Gio.SettingsSchemaSource.lookup(schema_source, 'org.gge-em.MindEd', False)
            logger.debug('Gsettings schema: %s' % schema.get_path())
            if not schema:
                raise Exception("Cannot get GSettings schema")
            settings = Gio.Settings.new_full(schema, None, None)
        else:
            settings = Gio.Settings('org.gge-em.MindEd')
        
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
        settings.bind('highlightcurrentline', builder.get_object('highlight_current_line_checkbutton'),
                     'active', Gio.SettingsBindFlags.DEFAULT)
        settings.bind('highlightmatchingbrackets', builder.get_object('bracket_matching_checkbutton'),
                     'active', Gio.SettingsBindFlags.DEFAULT)
        #smartbackspace
        
        self.window.show_all()
        self.window.connect('delete-event', self.quit)

    def on_font_button_font_set(self, button):
        logger.debug('Font set: %s' % button.get_font_name())
        for pagecount in range(self.app.win.notebook.get_n_pages()-1, -1, -1):
            editor = self.app.win.notebook.get_nth_page(pagecount)
            editor.codeview.override_font(Pango.FontDescription(button.get_font_name()))
            
    def quit(self, *args):
        'Quit the program'
        self.window.destroy()
        # needed! Else Window disappears, but App lives still.
        return True
