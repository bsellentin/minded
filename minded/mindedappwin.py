#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''MindEd - An Editor for programming LEGO Mindstorms Bricks
- NXT with NXC
- EV3 with EV3-Python
'''

import subprocess
# requires package python-pathlib
from pathlib import Path
from urllib.parse import urlparse, unquote
import shlex
import struct
import hashlib
import mmap
import re

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import GLib, Gtk, Gdk, Gio, GObject, Pango
gi.require_version('GtkSource', '3.0')
from gi.repository import GtkSource

import logging
logger = logging.getLogger(__name__)

from minded.editorapp import EditorApp
import minded.nxc_funcs as nxc_funcs
import minded.evc_funcs as evc_funcs
from minded.nxtinfo import NXTInfo
from minded.nxtfiler import NXTFiler

class MindEdAppWin(Gtk.ApplicationWindow):
    '''The Main Application Window'''

    def __init__(self, files, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #for key in kwargs:
        #    print("%s : %s" % (key, kwargs[key]))
        self.application = kwargs["application"]
        logger.debug("Filelist : %s" % files)
        
        # look for settings
        srcdir = Path(__file__).parents[1]
        logger.debug('srcdir: %s' % srcdir)
        if Path(srcdir, 'data').exists():
            logger.warn('Running from source tree, using local settings')
            schema_source = Gio.SettingsSchemaSource.new_from_directory(
                str(Path(srcdir, 'data')),
                Gio.SettingsSchemaSource.get_default(), False)
            schema = Gio.SettingsSchemaSource.lookup(
                schema_source, 'org.gge-em.MindEd', False)
            logger.debug('Gsettings schema: %s' % schema.get_path())
            if not schema:
                raise Exception("Cannot get GSettings schema")
            self.settings = Gio.Settings.new_full(schema, None, None)
        else:
            self.settings = Gio.Settings('org.gge-em.MindEd')

        if not self.settings.get_string('nbcpath'):
            if Path('/usr/bin/nbc').is_file():
                self.settings.set_string('nbcpath', '/usr/bin/nbc')
            elif Path('/usr/local/bin/nbc').is_file():
                self.settings.set_string('nbcpath','/usr/local/bin/nbc')
            else:
                logger.warn('no nbc executable found')

        if not self.settings.get_string('armgcc'):
            if Path('/usr/bin/arm-linux-gnueabi-gcc-6').is_file():              # Debian-stretch
                self.settings.set_string('armgcc', 'arm-linux-gnueabi-gcc-6')   # package gcc-6-arm-linux-gnueabi
            elif Path('/usr/bin/arm-linux-gnueabi-gcc').is_file():              # Ubuntu xenial
                self.settings.set_string('armgcc', 'arm-linux-gnueabi-gcc')
            else:
                logger.warn('no arm-gcc executable found')
        # check for development first
        if Path('./EV3-API/API/libev3api.a').is_file():
            self.settings.set_string('ldflags', ' -L' + str(Path('./EV3-API/API').resolve()))
        # systemwide installation
        elif not self.settings.get_string('ldflags'):
            if Path('/usr/lib/c4ev3/libev3api.a').is_file():
                self.settings.set_string('ldflags', ' -L/usr/lib/c4ev3')
            else:
                logger.warn('EV3 library not found')
        if Path('./EV3-API/API').is_dir():
            self.settings.set_string('incs', ' -I' + str(Path('./EV3-API/API').resolve()))
        elif not self.settings.get_string('incs'):
            if Path('/usr/lib/c4ev3').is_dir():
                self.settings.set_string('incs', ' -I/usr/lib/c4ev3')
            else:
                logger.warn('EV3 headers not found')

        builder = Gtk.Builder()
        GObject.type_register(GtkSource.View)
        builder.add_from_resource('/org/gge-em/MindEd/mindedappwin.ui')
        builder.connect_signals(self)
        self.window = builder.get_object("TopWin")
        self.window.set_application(self.application)

        self.notebook = builder.get_object("notebook")
        self.compilerview = builder.get_object("compilerview")
        self.headerbar = builder.get_object("header")
        self.menupop = builder.get_object("menumenu")
        self.btn_transmit = builder.get_object("btn_transmit")
        self.btn_transmit.set_sensitive(False)
        self.btn_save = builder.get_object("btn_save")
        self.btn_save.set_sensitive(False)
        self.btn_save_as = builder.get_object("btn_save_as")
        self.btn_save_as.set_sensitive(False)
        self.btn_print = builder.get_object("btn_print")
        self.btn_print.set_sensitive(False)
        self.brick_status = builder.get_object("brick_status")
        self.brick_status_id = self.brick_status.get_context_id("BrickStatus")
        self.btn_language = builder.get_object("btn_language")
        self.btn_language.set_sensitive(False)
        self.language_label = builder.get_object("language_label")
        self.languagemenu = builder.get_object("languagemenu")
        self.language_tree = builder.get_object("languagetree")
        self.language_store = Gtk.ListStore(str, str)
        self.language_store.append(["text", "Text"])
        self.language_store.append(["nxc", "NXC"])
        self.language_store.append(["evc", "EVC"])
        self.language_store.append(["python", "Python"])
        self.language_tree.set_model(self.language_store)
        self.cell = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Language", self.cell, text=1)
        self.language_tree.append_column(column)

        # Look for Brick
        for device in self.application.client.query_by_subsystem("usb"):
            if (device.get_property('ID_VENDOR') == '0694' and
                    device.get_property('ID_MODEL') == '0002'):
                self.brick_status.push(self.brick_status_id, "NXT")
                self.btn_transmit.set_sensitive(True)
            if (device.get_property('ID_VENDOR_ID') == '0694' and
                    device.get_property('ID_MODEL_ID') == '0005'):
                self.brick_status.push(self.brick_status_id, "EV3")
                self.btn_transmit.set_sensitive(True)

        self.window.show_all()

        self.untitledDocCount = 0
        loadedFiles = 0
        if len(files)>1:
            for nth_file in files[1:]:
                if Path(nth_file).is_file():
                    loadedFiles += self.load_file_in_editor(Path(nth_file).resolve().as_uri())
                    logger.debug("%d files loaded" % loadedFiles)
        if not loadedFiles:
            self.open_new()

    def gtk_main_quit(self, *args):
        '''
        TopWin CloseButton clicked, are there unsaved changes
        '''
        # get_n_pages from 0...n-1, remove reversed!
        realy_quit = False
        for pagecount in range(self.notebook.get_n_pages()-1, -1, -1):

            logger.debug("Window close clicked! Remove page %s" % pagecount)

            editor = self.notebook.get_nth_page(pagecount)
            if editor.get_buffer().get_modified():
                realy_quit = self.close_confirmation_dialog(editor)
                logger.debug("realy_quit %s" % realy_quit)
                # cancel close window
                if not realy_quit:
                    return True
            else:
                self.notebook.remove_page(pagecount)

        if self.notebook.get_n_pages() == 0:
            self.window.destroy()
            self.application.quit()

    def on_btn_new_clicked(self, button):

        self.open_new()

    def on_btn_open_clicked(self, button):

        open_dlg = Gtk.FileChooserDialog("Please choose a file", self.window,
                                         Gtk.FileChooserAction.OPEN,
                                         (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                          Gtk.STOCK_OPEN, Gtk.ResponseType.ACCEPT))
        open_dlg.set_local_only(False)
        self.add_filters(open_dlg)
        open_dlg.connect("response", self.open_dlg_response)
        open_dlg.show()

    def open_dlg_response(self, dialog, response):

        open_dlg = dialog
        if response == Gtk.ResponseType.ACCEPT:
            logger.debug("OpenDialog File selected: " + dialog.get_uri())
            # check if file already open
            for pagecount in range(self.notebook.get_n_pages()-1, -1, -1):
                editor = self.notebook.get_nth_page(pagecount)
                if editor.document.get_url() == open_dlg.get_uri():
                    self.notebook.set_current_page(pagecount)
                    break
            else:
                self.load_file_in_editor(open_dlg.get_uri())

        elif response == Gtk.ResponseType.CANCEL:
            logger.debug("OpenDialog Cancel clicked")

        dialog.destroy()

    def add_filters(self, dialog):
        filter_brickc = Gtk.FileFilter()
        filter_brickc.set_name("Brick files")
        filter_brickc.add_pattern("*.evc")
        filter_brickc.add_pattern("*.nxc")
        dialog.add_filter(filter_brickc)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

    def on_btn_save_clicked(self, button):

        page_num = self.notebook.get_current_page()
        editor = self.notebook.get_nth_page(page_num)
        # is_untitled(widget child, bool close_tab)
        self.is_untitled(editor, 0)

    def on_btn_save_as_clicked(self, button):

        if self.menupop.get_visible():
            self.menupop.hide()

        page_num = self.notebook.get_current_page()
        editor = self.notebook.get_nth_page(page_num)

        self.save_file_as(editor, 0)

        logger.debug("Save as: %s" % editor.document)

    def on_btn_close_tab_clicked(self, button, child):

        # widget must be child of page, that is scrolledwindow
        page_num = self.notebook.page_num(child)
        editor = self.notebook.get_nth_page(page_num)
        logger.debug("close tab %s" % page_num)

        if page_num != -1 and not editor.get_buffer().get_modified():
            self.notebook.remove_page(page_num)
            editor.destroy()
            child.destroy()
        else:
            logger.debug("file modified, save before closing")
            self.close_confirmation_dialog(child)

    def on_btn_compile_clicked(self, button):
        '''
        compile the saved file - a .rxe-file results
        '''

        page_num = self.notebook.get_current_page()
        editor = self.notebook.get_nth_page(page_num)
        if editor.get_buffer().get_modified():
            self.dlg_something_wrong(
                "You have to save first!",
                "The compiler works on the real file.")
        else:
            ext = Path(editor.document.get_shortname()).suffix
            if ext == '.nxc':
                nbcout = str(Path(editor.document.get_filepath(),
                                  Path(editor.document.get_shortname()).stem + ".rxe"))
                logger.debug("File to compile: %s" % editor.document.get_filename())
                nbc_opts = (' -O=%s %s' % (shlex.quote(nbcout),
                                           shlex.quote(editor.document.get_filename())))
                logger.debug("nbc optionen: %s" % nbc_opts)
                # change cursor
                watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
                self.window.get_window().set_cursor(watch_cursor)
                # don't starve the gui thread before it can change the cursor,
                # call the time consuming in an idle callback
                GObject.idle_add(self.idle_nbc_proc, self.window, nbc_opts)
            elif ext == '.evc':
                watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
                self.window.get_window().set_cursor(watch_cursor)
                GObject.idle_add(self.idle_evc_proc, self.window, editor.document)
            else:
                msg = self.compilerview.get_buffer()
                end_iter = msg.get_end_iter()
                red = msg.create_tag(None, foreground = "red", background="yellow")
                msg.insert_with_tags(end_iter, 'ERROR:', red)
                end_iter = msg.get_end_iter()
                msg.insert(end_iter, (' unknown file extension, expected: .nxc or .evc'))

    def on_btn_transmit_clicked(self, button):
        '''
        transmit compiled file to brick
        '''
        page_num = self.notebook.get_current_page()
        editor = self.notebook.get_nth_page(page_num)
        if editor.get_buffer().get_modified():
            self.dlg_something_wrong(
                "You have to save first!",
                "The compiler works on the real file.")
        else:
            ext = Path(editor.document.get_shortname()).suffix
            if ext == '.nxc':
                nbc_opts = (' -d %s' % (shlex.quote(editor.document.get_filename())))
                logger.debug('Transmit: %s' % nbc_opts)
                # change cursor
                watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
                self.window.get_window().set_cursor(watch_cursor)
                # don't starve the gui thread before it can change the cursor,
                # call the time consuming in an idle callback
                GObject.idle_add(self.idle_nbc_proc, self.window, nbc_opts)
            elif ext == '.evc':
                watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
                self.window.get_window().set_cursor(watch_cursor)
                GObject.idle_add(self.idle_evc_proc, self.window, editor.document, True)
            else:
                msg = self.compilerview.get_buffer()
                end_iter = msg.get_end_iter()
                red = msg.create_tag(None, foreground = "red", background="yellow")
                msg.insert_with_tags(end_iter, 'ERROR:', red)
                end_iter = msg.get_end_iter()
                msg.insert(end_iter, (' unknown file extension, expected: .nxc or .evc'))

    def mkstarter(self, document):
        '''
        build rbf-file, store local, upload later
        '''
        logger.debug('building starter for: %s' % document.get_filename())

        prjname = Path(document.get_shortname()).stem
        prjsstore = '/home/root/lms2012/prjs'
        prjpath = str(Path(prjsstore, prjname, prjname))
        logger.debug('EV3-path: %s' % prjpath)

        magic = b'LEGO'
        before = b'\x68\x00\x01\x00\x00\x00\x00\x00\x1C\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x60\x80'
        after = b'\x44\x85\x82\xE8\x03\x40\x86\x40\x0A'

        size = len(magic) + 4 + len(before) + len(prjpath)+1 + len(after)

        cmd = b''.join([
            magic,
            struct.pack('I', size),
            before,
            str.encode(prjpath)+b'\x00',
            after
            ])

        starter  = Path(document.get_filepath(), prjname + '.rbf')
        starter.write_bytes(cmd)

        msg = self.compilerview.get_buffer()
        enditer = msg.get_end_iter()
        msg.insert(enditer, 'Build starter successfull\n')

        return 1

    def dlg_something_wrong(self, what, why):

        dlg = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.INFO,
                                Gtk.ButtonsType.OK, what)
        dlg.format_secondary_text(why)

        dlg.run()
        dlg.destroy()

    def idle_nbc_proc(self, window, nbc_opts):
        '''
        compile and upload file to NXT brick
        '''
        nbc_exec = self.settings.get_string('nbcpath')
        enhancedfw = self.settings.get_boolean('enhancedfw')
        if enhancedfw:
            nbc_exec = nbc_exec + ' -EF'
        logger.debug('use enhancedfw: %s' % enhancedfw)

        if not nbc_exec:
            dlg_something_wrong(
                'No NBC-executable found!',
                'not in /usr/bin, not in /usr/local/bin')
        else:
            nbc_proc = subprocess.Popen(('%s %s' % (nbc_exec, nbc_opts)),
                                        shell=True, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)

            nbc_data = nbc_proc.communicate()
            if nbc_proc.returncode:  # Error
                self.compilerview.get_buffer().set_text(nbc_data[1].decode())
            else:  # OK
                # nur die letzten 5 Zeilen ausgeben
                msg = '\n'.join([str(i) for i in nbc_data[0].decode().split('\n')[-5:]])
                self.compilerview.get_buffer().set_text(msg)

            self.window.get_window().set_cursor(None)

    def idle_evc_proc(self, window, document, upload=False):       
        '''
        compile and upload file to EV3 brick
        '''
        prjname = Path(document.get_shortname()).stem

        compiled = 0
        starter = 0

        compiled = self.cross_compile(document)
        if upload:
            if compiled:
                starter = self.mkstarter(document)
            if starter:
                suca = self.ev3_upload(Path(document.get_filepath(), prjname + '.rbf'))
                sucb = self.ev3_upload(Path(document.get_filepath(), prjname))
                if suca and sucb:
                    self.window.get_application().ev3brick.play_sound('./ui/DownloadSucces')

        self.window.get_window().set_cursor(None)

    def cross_compile(self, document):
        '''
        cross-compile evc-file for EV3-brick, store local, upload later
        '''
        infile = document.get_filename()
        logger.debug('file to compile: %s' % infile)

        # check for non-alphanumeric characters in filename, won't run on bricks
        if re.match('^[a-zA-Z0-9_.]+$', Path(infile).name) is not None:
            outfile = str(Path(document.get_filepath(), Path(document.get_shortname()).stem))
            logger.debug('executable to write: %s' % outfile)

            arm_exec = self.settings.get_string('armgcc')

            ldflags = self.settings.get_string('ldflags')
            incs = self.settings.get_string('incs')

            gcc_exec = arm_exec + ldflags + incs + ' -Os'
            gcc_opts = (' -o %s -x c %s -lev3api' % (shlex.quote(outfile), shlex.quote(infile)))

            # is multithreading?
            with open(infile,  'rb', 0) as file, \
                mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
                if s.find(b'pthread.h') != -1:
                    gcc_opts += ' -lpthread'
            logger.debug('command: %s' % (gcc_exec + gcc_opts))

            gcc_proc = subprocess.Popen(('%s %s' % (gcc_exec, gcc_opts)),
                                            shell=True, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)

            gcc_data = gcc_proc.communicate()
            if gcc_proc.returncode:  # Error
                self.compilerview.get_buffer().set_text(gcc_data[1].decode())
                return 0
            else:  # OK
                self.compilerview.get_buffer().set_text('Compile successfull\n')
                return 1
        else:
            msg = self.compilerview.get_buffer()
            end_iter = msg.get_end_iter()
            red = msg.create_tag(None, foreground = "red", background="yellow")
            msg.insert_with_tags(end_iter, 'ERROR:', red)
            end_iter = msg.get_end_iter()
            msg.insert(end_iter, (' filename contains non-alphanumeric characters\n'))
            return 0

    def ev3_upload(self, infile):
        '''
        upload file to EV3 brick
        '''
        try:
            brick = self.window.get_application().ev3brick
            logger.info('got app.ev3brick')
            upload = True
        except AttributeError:
            logger.info('no app.ev3brick')
            upload = False

        if upload:
            if brick.usb_ready():

                prjname = infile.stem
                prjsstore = '/home/root/lms2012/prjs'
                outfile = str(Path(prjsstore, prjname, infile.name))

                data = infile.read_bytes()
                brick.write_file(outfile, data)

                content = brick.list_dir(str(Path(prjsstore, prjname)))

                success = 0
                for afile in content['files']:
                    if afile['name'] == infile.name:
                        if afile['md5'] == hashlib.md5(data).hexdigest().upper():
                            success = 1
                            msg = self.compilerview.get_buffer()
                            enditer = msg.get_end_iter()
                            msg.insert(enditer, ('Upload of %s successfull\n' % afile['name']))
                return success
            else:
                msg = self.compilerview.get_buffer()
                end_iter = msg.get_end_iter()
                red = msg.create_tag(None, foreground = "red", background="yellow")
                msg.insert_with_tags(end_iter, 'ERROR:', red)
                end_iter = msg.get_end_iter()
                msg.insert(end_iter, (' Failed to upload %s, try again\n' % filename))
                return 0

    def on_btn_menu_clicked(self, button):

        #Toggl
        if self.menupop.get_visible():
            self.menupop.hide()
        else:
            self.menupop.show_all()

    def on_btn_print_clicked(self, button):

        if self.menupop.get_visible():
            self.menupop.hide()

        page_num = self.notebook.get_current_page()
        editor = self.notebook.get_nth_page(page_num)

        printer = PrintingApp(editor)
        printer.run()

    def on_btn_about_clicked(self, button):

        if self.menupop.get_visible():
            self.menupop.hide()

        aboutdlg = Gtk.AboutDialog(transient_for=self.window, modal=True)

        authors = ["Bernd Sellentin"]
        #documenters = []

        aboutdlg.set_program_name("MindEd")
        aboutdlg.set_comments("An Editor for LEGO Mindstorms Bricks")
        aboutdlg.set_authors(authors)
        aboutdlg.set_version(self.application.version)
        #image = GdkPixbuf.Pixbuf()
        #image.new_from_file("/home/selles/pyGtk/minded/minded.png")
        #aboutdlg.set_logo_icon_name(image)
        aboutdlg.set_logo_icon_name()
        aboutdlg.set_copyright("2017")
        aboutdlg.set_website("http://github.com/bsellentin/minded")
        aboutdlg.set_website_label("MindEd Website")

        aboutdlg.present()

    def open_new(self):

        self.untitledDocCount += 1

        dirname = Path.home()
        filename = 'untitled' + str(self.untitledDocCount)
        newfile = Path(dirname, filename)

        # make empty file to avoid error on loading
        try:
            newfile.touch(exist_ok=True)
        except OSError:
            logger.debug('Could not make node for new file')
            pass

        self.load_file_in_editor(Path(newfile).as_uri())

    def load_file_in_editor(self, file):

        #logger.debug('Buffersize: %s ' % len(self.buffer.props.text))
        try:
            editor = EditorApp(self, file)
        except:
            logger.warn("Something went terrible wrong")

        self.create_tab_label(editor)
        self.notebook.append_page(editor, self.box)
        self.notebook.set_current_page(-1)

        buffer = editor.get_buffer()
        buffer.connect("modified_changed", self.on_buffer_modified)
        editor.codeview.grab_focus()

        if not self.btn_save.get_sensitive():
            self.btn_save.set_sensitive(True)
        if not self.btn_save_as.get_sensitive():
            self.btn_save_as.set_sensitive(True)
        if not self.btn_print.get_sensitive():
            self.btn_print.set_sensitive(True)
        if not self.btn_language.get_sensitive():
            self.btn_language.set_sensitive(True)

        self.change_language_selection(editor)

        logger.debug("file %s loaded in buffer, modified %s" % (file, buffer.get_modified()))
        return 1

    def is_untitled(self, editor, close_tab):
        """looks if file is new with default name
        called by on_btn_save_clicked
                  close_confirmation_dialog_response
                  called by gtk_main_quit
                            on_btn_close_tab
        """
        if 'untitled' in editor.document.get_shortname():
            logger.debug("Found untitled file: %s" % editor.document.get_url())
            self.save_file_as(editor, close_tab)
        else:
            self.save_file(editor, close_tab)

    def save_file_as(self, editor, close_tab):

        logger.debug("function save_file_as: %s" % editor.document.get_url())

        save_dialog = Gtk.FileChooserDialog("Pick a file", self.window,
                                            Gtk.FileChooserAction.SAVE,
                                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                             Gtk.STOCK_SAVE, Gtk.ResponseType.ACCEPT))
        save_dialog.set_do_overwrite_confirmation(True)
        save_dialog.set_local_only(False)
        try:
            if 'untitled' in editor.document.get_shortname():
                save_dialog.set_current_name(editor.document.get_shortname())
            else:
                save_dialog.set_uri(editor.document.get_url())
        except GObject.GError as e:
            logger.error("Error: " + e.message)

        save_dialog.connect("response", self.save_file_as_response, editor, close_tab)
        save_dialog.show()

    def save_file_as_response(self, dialog, response, editor, close_tab):

        save_dialog = dialog
        if response == Gtk.ResponseType.ACCEPT:
            # check for valid filename
            testname = Path(save_dialog.get_filename()).stem
            valid = re.match('^[a-zA-Z0-9_.]+$', testname) is not None
            logger.debug("%s is valid: %s" % (testname, valid))
            if valid:
                editor.document.set_url(save_dialog.get_uri())
                if logger.isEnabledFor(logging.DEBUG):
                    page_num = self.notebook.page_num(editor)
                    logger.debug("func save_file_as_response: %s on tab %s, " % (editor.document.get_url(), page_num))
                self.save_file(editor, close_tab)
            else:
                self.dlg_something_wrong(
                    "Filename unvalid!",
                    "Filename contains non-alphanumeric characters.")
        elif response == Gtk.ResponseType.CANCEL:
            logger.debug("cancelled: SAVE AS")
        dialog.destroy()

    def save_file(self, editor, close_tab):

        buffer = editor.get_buffer()

        # save file form GtkSourceBuffer as GtkSource.File
        file = GtkSource.File()
        file.set_location(Gio.File.new_for_uri(editor.document.get_url()))
        try:
            saver = GtkSource.FileSaver.new(buffer, file)
            saver.save_async(1, None, None, None, self.on_save_finish, editor, close_tab)
        except GObject.GError as e:
            logger.error("Error: " + e.message)

    def on_save_finish(self, source, result, editor, close_tab):

        try:
            success = source.save_finish(result)
            if close_tab:
                page_num = self.notebook.page_num(editor)
                logger.debug("remove tab %s" % page_num)
                # async saving, we have to wait for finish before removing
                self.notebook.get_nth_page(page_num).get_child().destroy()
                self.notebook.get_nth_page(page_num).destroy()
                self.notebook.remove_page(page_num)
            logger.debug("file %s saved %s" % (editor.document.get_url(), success))
            logger.debug("saved buffer, modified %s" % editor.get_buffer().get_modified())
            if editor.get_buffer().get_modified():
                editor.get_buffer().set_modified(False)
                logger.debug("set buffer modified %s" % editor.get_buffer().get_modified())
            # change language according file extension, e.g. new created files
            editor.this_lang = editor.lm.guess_language(editor.document.get_shortname(), None)
            if editor.this_lang:
                editor.get_buffer().set_highlight_syntax(True)
                editor.get_buffer().set_language(editor.this_lang)
                self.language_label.set_text(editor.this_lang.get_name())
            # change tab label
            self.change_tab_label(editor, editor.document.get_shortname())
            # change headerbar
            self.set_title(editor.document)

        except GObject.GError as e:
            logger.error("problem saving file " + e.message)
            return

    def close_confirmation_dialog(self, editor):

        filename = editor.document.get_shortname()

        dlg = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.WARNING,
                                Gtk.ButtonsType.NONE,
                                "Save changes to document '%s' before closing?" % filename)
        dlg.add_buttons("Close without Saving", Gtk.ResponseType.NO,
                        "Cancel", Gtk.ResponseType.CANCEL,
                        "Save", Gtk.ResponseType.YES)
        dlg.format_secondary_text("Changes to document '%s' will be permanently lost." % filename)
        dlg.set_default_response(Gtk.ResponseType.YES)

        response = dlg.run()

        if response == Gtk.ResponseType.NO:
            logger.debug("Close tab without saving")
            # click perhaps not on current page
            page_num = self.notebook.page_num(editor)
            self.notebook.remove_page(page_num)
            editor.destroy()

        elif response == Gtk.ResponseType.CANCEL:
            logger.debug("Cancel closing tab")
            dlg.destroy()
            return False

        elif response == Gtk.ResponseType.YES:
            logger.debug("Save file before closing")

            close_tab = 1
            self.is_untitled(editor, close_tab)

        # if the messagedialog is destroyed (by pressing ESC)
        elif response == Gtk.ResponseType.DELETE_EVENT:
            logger.debug("dialog closed or cancelled")
        # finally, destroy the messagedialog
        dlg.destroy()

        return True

    def create_tab_label(self, editor):

        # create tab header with close button
        self.box = Gtk.HBox()
        closebtn = Gtk.Button()
        icon = Gio.ThemedIcon(name="window-close")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        closebtn.set_image(image)
        closebtn.set_relief(Gtk.ReliefStyle.NONE)
        closebtn.connect("clicked", self.on_btn_close_tab_clicked, editor)

        # change headerbar
        self.set_title(editor.document)

        self.box.pack_start(Gtk.Label(editor.document.get_shortname()), True, True, 0)
        self.box.pack_end(closebtn, False, False, 0)
        self.box.show_all()

    def on_buffer_modified(self, widget):

        page_num = self.notebook.get_current_page()
        editor = self.notebook.get_nth_page(page_num)
        logger.debug("modified tab %s %s" % (page_num, editor.get_buffer().get_modified()))

        filename = editor.document.get_shortname()

        if editor.get_buffer().get_modified(): 
            filename = "*"+filename
        else:
            if filename.startswith('*'):
                filename = filename[1:]

        self.change_tab_label(editor, filename)

    def change_tab_label(self, editor, filename):
        thisbox = self.notebook.get_tab_label(editor)
        widglist = thisbox.get_children()
        widglist[0].set_text(filename)

    def on_languageselect_changed(self, selection):
        ''' single click, language changed '''
        model, treeiter = selection.get_selected()
        self.change_language(model, treeiter)

    def on_languagetree_row_activated(self, treeview, path, column):
        '''double click'''
        selection = treeview.get_selection()
        model, treeiter = selection.get_selected()
        self.change_language(model, treeiter)

    def change_language(self, model, treeiter):
        '''change language for current document'''
        if treeiter != None:
            logger.debug("Language selected %s", model[treeiter][0])

            self.language_label.set_text(model[treeiter][1])

            page_num = self.notebook.get_current_page()
            editor = self.notebook.get_nth_page(page_num)

            root = Path(editor.document.get_shortname()).stem

            this_lang = editor.lm.get_language(model[treeiter][0])
            buffer = editor.get_buffer()
            if this_lang:
                if not buffer.get_highlight_syntax():
                    buffer.set_highlight_syntax(True)
                buffer.set_language(this_lang)
                if this_lang.get_name() == 'NXC':
                    editor.custom_completion_provider.funcs = nxc_funcs.nxc_funcs
                    editor.custom_completion_provider.consts = nxc_funcs.nxc_consts
                    editor.custom_completion_provider.lang = 'NXC'
                    editor.document.set_shortname(root + '.nxc')
                if this_lang.get_name() == 'EVC':
                    editor.custom_completion_provider.funcs = evc_funcs.evc_funcs
                    editor.custom_completion_provider.consts = evc_funcs.evc_consts
                    editor.custom_completion_provider.lang = 'EVC'
                    editor.document.set_shortname(root + '.evc')
                logger.debug("changed extension: " + editor.document.get_url())
                buffer.set_modified(True)
                self.set_title(editor.document)
            else:
                if buffer.get_highlight_syntax():
                    buffer.set_highlight_syntax(False)
                buffer.set_language(None)

            editor.codeview.grab_focus()
            self.languagemenu.hide()

    def change_language_selection(self, editor):     
        '''changes language_label and language_tree on load file and on switch page'''
        editor.this_lang = editor.lm.guess_language(editor.document.get_shortname(), None)

        if editor.this_lang:
            self.language_label.set_text(editor.this_lang.get_name())
            for i, row in enumerate(self.language_store):
                if row[1] == editor.this_lang.get_name():
                    path = Gtk.TreePath(i)
        else:
            self.language_label.set_text('Text')
            path = Gtk.TreePath(0)

        select = self.language_tree.get_selection()
        select.disconnect_by_func(self.on_languageselect_changed)
        self.language_tree.set_cursor(path, None, False)    # emits changed-signal
        select.connect("changed", self.on_languageselect_changed)    

    def on_notebook_switch_page(self, notebook, page, page_num):
        '''change headerbar and language selection accordingly'''
        editor = self.notebook.get_nth_page(page_num)
        self.change_language_selection(editor)    
        self.set_title(editor.document)

    def set_title(self, document):
        self.headerbar.set_title(document.get_shortname())
        self.headerbar.set_subtitle(document.get_filepath())

    def on_btn_nxtinfo_clicked(self, button):
        '''open new window with brick information like name, firmware...'''
        if self.menupop.get_visible():
            self.menupop.hide()
        self.nxt_info = NXTInfo(self.window.get_application())

    def on_btn_nxtfiler_clicked(self, button):
        '''open new window with brick file browser...'''
        if self.menupop.get_visible():
            self.menupop.hide()
        self.nxt_filer = NXTFiler(self.window.get_application())

class PrintingApp:
    '''
    Print with syntax highlightning
    '''

    def __init__(self, textview):
        self.operation = Gtk.PrintOperation.new()
        self.compositor = GtkSource.PrintCompositor.new_from_view(textview.codeview)

        self.compositor.set_header_format(True, textview.file, None, None)
        self.compositor.set_print_header(True)
        self.compositor.set_body_font_name("Monospace 10")

        self.operation.connect('begin-print', self.begin_print, self.compositor)
        self.operation.connect('draw-page', self.draw_page, self.compositor)
        self.operation.connect('end_print', self.end_print)

    def run(self, parent=None):

        result = self.operation.run(Gtk.PrintOperationAction.PRINT_DIALOG,
                                    parent)

        if result == Gtk.PrintOperationResult.ERROR:
            message = self.operation.get_error()

            dialog = Gtk.MessageDialog(parent,
                                       0,
                                       Gtk.MessageType.ERROR,
                                       Gtk.ButtonsType.CLOSE,
                                       message)
            dialog.run()
            dialog.destroy()

    def begin_print(self, operation, context, compositor):

        logger.debug("Initializing printing process...")

        while not compositor.paginate(context):
            pass
        n_pages = compositor.get_n_pages()
        operation.set_n_pages(n_pages)

        logger.debug("Sending %s pages to printer", n_pages)

    def draw_page(self, operation, context, page_num, compositor):

        logger.debug("Sending page: %s", (page_num+1))

        compositor.draw_page(context, page_num)

    def end_print(self, operation, context):

        logger.debug("Document sent to printer")

