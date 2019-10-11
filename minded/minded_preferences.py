# -*- coding: utf-8 -*-

'''
Preferences Dialog for MindEd
'''

from gettext import gettext as _
import logging

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import Gtk, Gio, Pango

LOGGER = logging.getLogger(__name__)

class PreferencesDialog():
    '''
    The preferences dialog window
    '''
    def __init__(self, application):

        self.app = application
        builder = Gtk.Builder()
        builder.add_from_resource('/org/gge-em/MindEd/minded-preferences-dialog.ui')
        builder.connect_signals(self)

        self.window = builder.get_object("window1")
        self.window.set_application(application)

        # look for settings
        setters = [
            # Editor
            ['fontname', 'font_button', 'font-name'],
            ['linenumbers', 'display_line_numbers_checkbutton', 'active'],
            ['showrightmargin', 'right_margin_checkbutton', 'active'],
            ['setrightmargin', 'right_margin_position_spinbutton', 'value'],
            ['autoindent', 'auto_indent_checkbutton', 'active'],
            ['indentontab', 'indent_on_tab_checkbutton', 'active'],
            ['tabwidth', 'tabs_width_spinbutton', 'value'],
            ['spacesinsteadtab', 'insert_spaces_checkbutton', 'active'],
            ['highlightcurrentline', 'highlight_current_line_checkbutton', 'active'],
            ['highlightmatchingbrackets', 'bracket_matching_checkbutton', 'active'],
            #smartbackspace
            # EVC
            ['armgcc', 'gccfile', 'text'],
            ['ldflags', 'ldflagsfile', 'text'],
            ['incs', 'incsfile', 'text'],
            ['armgplusplus', 'cplusfile', 'text'],
            ['cplusplus', 'c++-compiler', 'active'],
            # NXC
            ['nbcpath', 'nbcexecfile', 'text'],
            ['enhancedfw', 'use_enhanced_firmware_checkbutton', 'active']
        ]
        for setter in setters:
            self.app.settings.bind(setter[0], builder.get_object(setter[1]),
                                   setter[2], Gio.SettingsBindFlags.DEFAULT)

        wrap_mode_checkbutton = builder.get_object('line_wrap_mode_checkbutton')
        wrap_mode_checkbutton.connect('toggled', self.on_wrap_mode_toggled, self.app.settings)
        if self.app.settings.get_enum('linewrapmode'):
            wrap_mode_checkbutton.set_active(True)

        # NXC
        nbcfile = Gio.File.new_for_path(self.app.settings.get_string('nbcpath'))
        if nbcfile.query_exists():
            builder.get_object('choosenbc').set_file(nbcfile)
        builder.get_object('choosenbc').set_current_folder_file(nbcfile)
        builder.get_object('choosenbc').set_title(_('choose NBC-file'))

        #EVC
        gccfile = Gio.File.new_for_path(self.app.settings.get_string('armgcc'))
        if gccfile.query_exists():
            builder.get_object('choosegcc').set_file(gccfile)
        builder.get_object('choosegcc').set_current_folder_file(gccfile)
        builder.get_object('choosegcc').set_title(_('choose gcc-file'))

        cplusfile = Gio.File.new_for_path(self.app.settings.get_string('armgplusplus'))
        if cplusfile.query_exists():
            builder.get_object('choosecplus').set_file(cplusfile)
        builder.get_object('choosecplus').set_current_folder_file(cplusfile)
        builder.get_object('choosecplus').set_title(_('choose C++-file'))

        libev3file = Gio.File.new_for_path(self.app.settings.get_string('ldflags') + '/libev3api.a')
        if libev3file.query_exists():
            builder.get_object('chooseldflags').set_file(libev3file)
        builder.get_object('chooseldflags').set_current_folder_file(libev3file)
        builder.get_object('chooseldflags').set_title(_('choose libev3api-file'))

        headerfile = Gio.File.new_for_path(self.app.settings.get_string('incs') + '/ev3.h')
        if headerfile.query_exists():
            builder.get_object('chooseincs').set_file(headerfile)
        builder.get_object('chooseincs').set_current_folder_file(headerfile)
        builder.get_object('chooseincs').set_title(_('choose ev3-header'))


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

    def on_cplusfile_set(self, widget):
        LOGGER.debug('C++-compiler: {}'.format(widget.get_file().get_path()))
        self.app.settings.set_string('armgplusplus', widget.get_file().get_path())

    def on_incfolder_set(self, widget):
        LOGGER.debug('header: {}'.format(widget.get_file().get_parent().get_path()))
        self.app.settings.set_string('incs', widget.get_file().get_parent().get_path())

    def on_ldfile_set(self, widget):
        LOGGER.debug('libev3: {}'.format(widget.get_file().get_parent().get_path()))
        self.app.settings.set_string('ldflags', widget.get_file().get_parent().get_path())

    def on_cfile_set(self, widget):
        LOGGER.debug('arm-gcc: {}'.format(widget.get_file().get_path()))
        self.app.settings.set_string('armgcc', widget.get_file().get_path())

    def on_nbcfile_set(self, widget):
        self.app.settings.set_string('nbcpath', widget.get_file().get_path())

    def quit(self, *args):
        '''Close preferences-dialog'''
        self.window.destroy()
        # needed! Else Window disappears, but App lives still.
        return True
