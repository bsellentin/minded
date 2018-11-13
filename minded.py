#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''MindEd - An Editor for programming LEGO Mindstorms Bricks
- NXT with NXC
- EV3 with EVC - a fork of C4EV3
'''

# Copyright (C) 2017 Bernd Sellentin <sel@gge-em.org>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import sys
from pathlib import Path


# internationalization
import locale
import gettext

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

LOGGER = logging.getLogger(__name__)

APP_NAME = "minded"

def make_option(long_name, short_name=None, flags=0, arg=GLib.OptionArg.NONE,
                arg_data=None, description=None, arg_description=None):
    ''' create struct for commandline options '''
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
    ''' The main application '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.gge-em.MindEd",
                         #flags=Gio.ApplicationFlags.FLAGS_NONE,            # argparse in main
                         flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE,   # do_commandline
                         **kwargs)

        # For Gio.Application 2.40 -> Trusty
        self.win = None
        self.version = "0.7.11"

        self.args = ()
        self.filelist = []
        self.settings = ''
        # USB client
        self.client = None
        self.nxt_brick = None
        self.ev3_brick = None

        self.add_main_option_entries([
            make_option("debug", description="Show debug information on the console"),
            make_option("version", description="Print the version number and exit")
            ])

    def do_startup(self):
        Gtk.Application.do_startup(self)

        # where do we get started
        srcdir = Path(__file__).parent
        # local installation, for development
        if Path(srcdir, 'data').exists():
            LOGGER.warning('Running from source tree, using local ui-files')
            LOGGER.debug('srcdir: %s', srcdir)
            # look for ui-files
            pkgdatadir = Path(srcdir, 'data')
            # look for settings
            schema_source = Gio.SettingsSchemaSource.new_from_directory(
                str(Path(srcdir, 'data')),
                Gio.SettingsSchemaSource.get_default(), False)
            schema = Gio.SettingsSchemaSource.lookup(
                schema_source, 'org.gge-em.MindEd', False)
            LOGGER.debug('Gsettings schema: %s', schema.get_path())
            if not schema:
                raise Exception("Cannot get GSettings schema")
            self.settings = Gio.Settings.new_full(schema, None, None)
            # Translation stuff
            locale.bindtextdomain('minded', srcdir.resolve())
            locale.textdomain('minded')
            gettext.bindtextdomain('minded', srcdir.resolve())
            gettext.textdomain('minded')
        # systemwide installation
        else:
            pkgdatadir = '/usr/share/minded'
            self.settings = Gio.Settings('org.gge-em.MindEd')
            locale.bindtextdomain('minded', '/usr/share/locale')
            locale.textdomain('minded')
            gettext.bindtextdomain('minded')
            gettext.textdomain('minded')

        resource_path = Path(pkgdatadir, 'minded.gresource')
        resource = Gio.Resource.load(str(resource_path))
        Gio.Resource._register(resource)

        action = Gio.SimpleAction.new('preferences', None)
        action.connect("activate", self.on_preferences)
        self.add_action(action)

        action = Gio.SimpleAction.new('shortcuts', None)
        action.connect('activate', self.on_shortcuts)
        self.add_action(action)

        action = Gio.SimpleAction.new('about', None)
        action.connect('activate', self.on_about)
        self.add_action(action)

        action = Gio.SimpleAction.new('quit', None)
        action.connect("activate", self.on_quit)
        self.add_action(action)
        self.set_accels_for_action('app.quit', ['<Control>Q'])

        builder = Gtk.Builder()
        if Gtk.get_minor_version() > 18:
            # use GtkShortcutsWindow
            builder.add_from_resource('/org/gge-em/MindEd/app-menu.ui')
        else:
            builder.add_from_resource('/org/gge-em/MindEd/app-menu-traditional.ui')
        self.set_app_menu(builder.get_object("appmenu"))

    def do_activate(self):

        # Listen to uevent
        self.client = GUdev.Client(subsystems=["usb"])
        self.client.connect("uevent", self.on_uevent)

        for device in self.client.query_by_subsystem("usb"):
            if self.look_for_brick(device):
                break

        #self.look_for_settings(self.settings)
        look_for_settings(self.settings)

        if not self.win:
            self.win = MindEdAppWin(self.filelist, application=self)
        else:
            # MindEd already running, brick file in file browser clicked
            for nth_file in self.filelist[1:]:
                if Path(nth_file).is_file():
                    self.win.load_file_in_editor(Path(nth_file).resolve().as_uri())
        self.win.present()

    def do_command_line(self, command_line):

        options = command_line.get_options_dict()
        if options.contains("version"):
            print("MindEd {}".format(self.version))
            return 0
        if options.contains("debug"):
            self.args += ("debug",)
            logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s',
                                level=logging.DEBUG)
        else:
            logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s',
                                level=logging.WARN)

        self.filelist = command_line.get_arguments()
        LOGGER.debug("Filelist: %s", self.filelist)

        self.activate()
        return 0

    def look_for_brick(self, device):
        '''
        look for LEGO-brick and initialize it
        '''

        if '694/2' in device.get_property('PRODUCT'):
            LOGGER.debug('found NXT')
            #if LOGGER.isEnabledFor(logging.DEBUG):
            #    for device_key in device.get_property_keys():
            #        LOGGER.debug("   device property %s: %s", device_key,
            #                     device.get_property(device_key))
            try:
                #LOGGER.debug("NXT-lib: %s", nxt.locator.__file__)
                self.nxt_brick = nxt.locator.find_one_brick()
                return 'nxt'
            except Exception as e:
                LOGGER.warning('nxt-python failure: %s' % e)

        elif '694/5' in device.get_property('PRODUCT'):
            LOGGER.debug('found EV3')
            #if LOGGER.isEnabledFor(logging.DEBUG):
            #    for device_key in device.get_property_keys():
            #        LOGGER.debug("   device property %s: %s", device_key,
            #                     device.get_property(device_key))
            try:
                self.ev3_brick = ev3.EV3()
                #self.ev3_brick.do_nothing()
                return 'ev3'
            except Exception as e:
                LOGGER.warning('ev3-python failure: %s' % e)

        return None

    def on_uevent(self, client, action, device):
        ''' report plugin-event to application'''
        if LOGGER.isEnabledFor(logging.DEBUG):
            for device_key in device.get_property_keys():
                LOGGER.debug('   device property %s: %s',
                             device_key, device.get_property(device_key))

        if action == "add":
            # only LEGO-devices
            if self.look_for_brick(device) == 'nxt':
                LOGGER.debug(' uevent: added NXT')
                self.win.brick_status.push(self.win.brick_status_id, "NXT")
                self.win.transmit_action.set_enabled(True)
                #try:
                #    self.win.nxt_filer.nxt_model.populate(self.brick, '*.*')
                #except AttributeError:
                #    pass
            elif self.look_for_brick(device) == 'ev3':
                LOGGER.debug(' uevent: added EV3')
                self.win.brick_status.push(self.win.brick_status_id, "EV3")
                self.win.transmit_action.set_enabled(True)
            else:
                pass

        # newer libgudev returns on remove ID_VENDOR None
        if action == 'remove':
            if '694/5' in device.get_property('PRODUCT'):
                # EV3 PRODUCT 694/5/216
                LOGGER.debug(' uevent: removed EV3')
                self.win.brick_status.pop(self.win.brick_status_id)
                self.win.transmit_action.set_enabled(False)
                self.ev3_brick = None
            if '694/2' in device.get_property('PRODUCT'):
                # NXT PRODUCT 694/2/0
                LOGGER.debug(' uevent: removed NXT')
                self.win.brick_status.pop(self.win.brick_status_id)
                self.win.transmit_action.set_enabled(False)
                self.nxt_brick = None

    def on_preferences(self, action, param):
        ''' Gio.SimpleAction preferences '''
        dlg = PreferencesDialog(self.win.get_application())
        dlg.window.set_transient_for(self.win)
        dlg.window.set_modal(True)
        dlg.window.present()

    def on_shortcuts(self, action, param):
        ''' Gio.SimpleAction shortcuts '''
        builder = Gtk.Builder()
        builder.add_from_resource('/org/gge-em/MindEd/shortcuts.ui')
        shortcuts_win = builder.get_object('shortcuts-minded')
        shortcuts_win.set_transient_for(self.win)
        shortcuts_win.show_all()

    def on_about(self, action, param):
        ''' Gio.SimpleAction about '''
        builder = Gtk.Builder()
        builder.add_from_resource('/org/gge-em/MindEd/about.ui')
        about_win = builder.get_object('about-dlg')
        about_win.set_version(self.version)
        about_win.set_transient_for(self.win)
        about_win.show_all()

    def on_quit(self, action, param):
        '''
        quit application
        '''
        self.win.gtk_main_quit()

def look_for_settings(settings):
    '''
    look for settings, if none - set defaults
    '''
    # nbc compiler
    if not Path(settings.get_string('nbcpath')).is_file():
        if Path('/usr/bin/nbc').is_file():
            settings.set_string('nbcpath', '/usr/bin/nbc')
        elif Path('/usr/local/bin/nbc').is_file():
            settings.set_string('nbcpath', '/usr/local/bin/nbc')
        else:
            LOGGER.warning('no nbc executable found')
    # arm-c compiler
    if not Path(settings.get_string('armgcc')).is_file():
        # Debian-stretch
        if Path('/usr/bin/arm-linux-gnueabi-gcc-6').is_file():
            # package gcc-6-arm-linux-gnueabi
            settings.set_string('armgcc', 'arm-linux-gnueabi-gcc-6')
        # Ubuntu xenial
        elif Path('/usr/bin/arm-linux-gnueabi-gcc-5').is_file():
            settings.set_string('armgcc', 'arm-linux-gnueabi-gcc-5')
        else:
            LOGGER.warning('no arm-gcc executable found')
    # c++ compiler
    if not Path(settings.get_string('armgplusplus')).is_file():
        if Path('/usr/bin/arm-linux-gnueabi-g++-6').is_file():
            settings.set_string('armgplusplus', 'arm-linux-gnueabi-g++-6')
        # Ubuntu xenial
        elif Path('/usr/bin/arm-linux-gnueabi-g++-5').is_file():
            # package g++-5-arm-linux-gnueabi
            settings.set_string('armgplusplus', 'arm-linux-gnueabi-g++-5')
        else:
            LOGGER.warning('no arm-g++ executable found')
    # check for ev3-library, development first
    if Path('./EV3-API/API/libev3api.a').is_file():
        settings.set_string('ldflags', str(Path('./EV3-API/API').resolve()))
    # systemwide installation
    elif not Path(settings.get_string('ldflags')).is_file():
        if Path('/usr/lib/c4ev3/libev3api.a').is_file():
            settings.set_string('ldflags', '/usr/lib/c4ev3')
        else:
            LOGGER.warning('EV3 library not found')
    if Path('./EV3-API/API').is_dir():
        settings.set_string('incs', str(Path('./EV3-API/API').resolve()))
    elif not Path(settings.get_string('incs')).is_dir():
        if Path('/usr/lib/c4ev3').is_dir():
            settings.set_string('incs', '/usr/lib/c4ev3')
        else:
            LOGGER.warning('EV3 headers not found')

    if not settings.get_string('prjsstore'):
        settings.set_string('prjsstore', '/home/root/lms2012/prjs')
        #TODO: if SD-card, check avaibility

if __name__ == "__main__":
    APP = MindEdApp()
    APP.run(sys.argv)
