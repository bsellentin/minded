#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
MindEd - A IDE for programming LEGO Mindstorms Bricks
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

from pathlib import Path
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
from minded.brickhelper import BrickHelper
from minded.brickinfo import BrickInfo
from minded.brickfiler import BrickFiler
from minded.apiviewer import ApiViewer


class MindEdAppWin(Gtk.ApplicationWindow):
    '''The Main Application Window'''

    def __init__(self, files, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #for key in kwargs:
        #    print("%s : %s" % (key, kwargs[key]))
        self.application = kwargs['application']
        logger.debug('Filelist : %s' % files)

        builder = Gtk.Builder()
        GObject.type_register(GtkSource.View)
        builder.add_from_resource('/org/gge-em/MindEd/mindedappwin.ui')
        builder.connect_signals(self)
        self.window = builder.get_object('TopWin')
        self.window.set_application(self.application)

        self.notebook = builder.get_object('notebook')
        self.headerbar = builder.get_object('header')
        self.menupop = builder.get_object('menumenu')
        self.btn_transmit = builder.get_object('btn_transmit')
        self.btn_transmit.set_sensitive(False)
        self.btn_save = builder.get_object('btn_save')
        self.btn_save.set_sensitive(False)
        self.btn_save_as = builder.get_object('btn_save_as')
        self.btn_save_as.set_sensitive(False)
        self.btn_print = builder.get_object('btn_print')
        self.btn_print.set_sensitive(False)
        self.brick_status = builder.get_object('brick_status')
        self.brick_status_id = self.brick_status.get_context_id('BrickStatus')
        self.cursor_location = builder.get_object('colln_status')
        self.cursor_location_id = self.cursor_location.get_context_id('ColLn')
        self.btn_language = builder.get_object('btn_language')
        self.btn_language.set_sensitive(False)
        self.language_label = builder.get_object('language_label')
        self.languagemenu = builder.get_object('languagemenu')
        self.language_tree = builder.get_object('languagetree')
        self.language_store = Gtk.ListStore(str, str)
        self.language_store.append(['text', 'Text'])
        self.language_store.append(['nxc', 'NXC'])
        self.language_store.append(['evc', 'EVC'])
        self.language_store.append(['python', 'Python'])
        self.language_tree.set_model(self.language_store)
        self.cell = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn('Language', self.cell, text=1)
        self.language_tree.append_column(column)

        compilerview = builder.get_object('compilerview')
        self.log_buffer = compilerview.get_buffer()
        self.log_buffer.create_tag('warning', foreground='red', background='yellow')

        # Look for Brick
        if self.application.nxtbrick:
            self.brick_status.push(self.brick_status_id, 'NXT')
            self.btn_transmit.set_sensitive(True)
        elif self.application.ev3brick:
            self.brick_status.push(self.brick_status_id, 'EV3')
            self.btn_transmit.set_sensitive(True)

        self.window.show_all()

        self.untitledDocCount = 0
        # bricks don't want prognames with non-alphanumeric characters
        # returns None if non-alphanumeric character found
        self.forbiddenchar = re.compile('^[a-zA-Z0-9_.]+$')

        loadedFiles = 0
        if len(files)>1:
            for nth_file in files[1:]:
                if Path(nth_file).is_file():
                    loadedFiles += self.load_file_in_editor(Path(nth_file).resolve().as_uri())
                    logger.debug('%d files loaded' % loadedFiles)
        if not loadedFiles:
            self.open_new()

    def gtk_main_quit(self, *args):
        '''
        TopWin CloseButton clicked, are there unsaved changes
        '''
        # get_n_pages from 0...n-1, remove reversed!
        realy_quit = False
        for pagecount in range(self.notebook.get_n_pages()-1, -1, -1):

            logger.debug('Window close clicked! Remove page %s' % pagecount)

            editor = self.notebook.get_nth_page(pagecount)
            buf = editor.get_buffer()
            if buf.get_modified():
                self.dlg_close_confirmation(editor)
            else:
                self.notebook.remove_page(pagecount)

        if self.notebook.get_n_pages() == 0:
            logger.debug('No more pages - destroy win')
            self.application.quit()

    def on_btn_new_clicked(self, button):

        self.open_new()

    def on_btn_open_clicked(self, button):

        if self.notebook.get_n_pages():
            editor = self.get_editor()
            path = editor.document.get_parent()
        else:
            path = str(Path.home())

        dialog = FileOpenDialog(self, path)
        response = dialog.run()

        if response == Gtk.ResponseType.ACCEPT:
            logger.debug('FileOpenDialog File selected: ' + dialog.get_uri())
            # check if file already open
            for pagecount in range(self.notebook.get_n_pages()-1, -1, -1):
                editor = self.notebook.get_nth_page(pagecount)
                if editor.document.get_uri() == dialog.get_uri():
                    self.notebook.set_current_page(pagecount)
                    break
            else:
                self.load_file_in_editor(dialog.get_uri())

        elif response == Gtk.ResponseType.CANCEL:
            logger.debug('FileOpenDialog Cancel clicked')

        dialog.destroy()

    def on_btn_save_clicked(self, button):

        self.save_file_async(self.get_editor())

    def on_btn_save_as_clicked(self, button):

        if self.menupop.get_visible():
            self.menupop.hide()

        editor = self.get_editor()
        self.save_file_as(editor)

    def on_btn_close_tab_clicked(self, button, child):

        # widget must be child of page, that is scrolledwindow
        page_num = self.notebook.page_num(child)
        editor = self.notebook.get_nth_page(page_num)
        logger.debug('close tab %s' % page_num)

        if page_num != -1 and not editor.get_buffer().get_modified():
            self.notebook.remove_page(page_num)
            editor.destroy()
            child.destroy()
        else:
            logger.debug('file modified, save before closing')
            self.dlg_close_confirmation(child)

    def on_btn_compile_clicked(self, button):
        '''
        compile the saved file
        '''
        editor = self.get_editor()
        if editor.get_buffer().get_modified():
            self.dlg_something_wrong(
                'You have to save first!',
                'The compiler works on the real file.')
        else:
            ext = Path(editor.document.get_basename()).suffix
            if ext == '.nxc':
                # change cursor
                watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
                self.window.get_window().set_cursor(watch_cursor)
                # don't starve the gui thread before it can change the cursor,
                # call the time consuming in an idle callback
                GObject.idle_add(self.idle_nbc_proc, self.window, editor.document, False)
            elif ext == '.evc':
                watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
                self.window.get_window().set_cursor(watch_cursor)
                GObject.idle_add(self.idle_evc_proc, self.window, editor.document)
            else:
                self.log_buffer.set_text('# Error: unknown file extension, expected: .nxc or .evc')
                self.format_log(self.log_buffer.get_start_iter())

    def on_btn_transmit_clicked(self, button):
        '''
        transmit compiled file to brick
        '''
        editor = self.get_editor()
        if editor.get_buffer().get_modified():
            self.dlg_something_wrong(
                'You have to save first!',
                'The compiler works on the real file.')
        else:
            ext = Path(editor.document.get_basename()).suffix
            if ext == '.nxc':
                # change cursor
                watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
                self.window.get_window().set_cursor(watch_cursor)
                # don't starve the gui thread before it can change the cursor,
                # call the time consuming in an idle callback
                GObject.idle_add(self.idle_nbc_proc, self.window, editor.document, True)
            elif ext == '.evc':
                watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
                self.window.get_window().set_cursor(watch_cursor)
                GObject.idle_add(self.idle_evc_proc, self.window, editor.document, True)
            else:
                self.log_buffer.set_text('# Error: unknown file extension, expected: .nxc or .evc')
                self.format_log(self.log_buffer.get_start_iter())

    def on_btn_menu_clicked(self, button):

        #Toggl
        if self.menupop.get_visible():
            self.menupop.hide()
        else:
            self.menupop.show_all()

    def on_btn_print_clicked(self, button):

        if self.menupop.get_visible():
            self.menupop.hide()

        printer = PrintingApp(self.get_editor())
        printer.run()

    def on_btn_about_clicked(self, button):

        if self.menupop.get_visible():
            self.menupop.hide()

        aboutdlg = Gtk.AboutDialog(transient_for=self.window, modal=True)

        authors = ['Bernd Sellentin']
        #documenters = []

        aboutdlg.set_program_name('MindEd')
        aboutdlg.set_comments('An Editor for LEGO Mindstorms Bricks')
        aboutdlg.set_authors(authors)
        aboutdlg.set_version(self.application.version)
        #image = GdkPixbuf.Pixbuf()
        #image.new_from_file("/home/selles/pyGtk/minded/minded.png")
        #aboutdlg.set_logo_icon_name(image)
        aboutdlg.set_logo_icon_name()
        aboutdlg.set_copyright('2017')
        aboutdlg.set_website('http://github.com/bsellentin/minded')
        aboutdlg.set_website_label('MindEd Website')

        aboutdlg.present()

    def on_btn_brickinfo_clicked(self, button):
        '''open new window with brick information like name, firmware...'''
        if self.menupop.get_visible():
            self.menupop.hide()
        self.brick_info = BrickInfo(self.application)

    def on_btn_brickfiler_clicked(self, button):
        '''open new window with brick file browser...'''
        if self.menupop.get_visible():
            self.menupop.hide()
        self.brick_filer = BrickFiler(self.application)

    def on_btn_apiviewer_clicked(self, button):
        '''open new window with API reference browser'''
        if self.menupop.get_visible():
            self.menupop.hide()
        self.api_viewer = ApiViewer(self.application)

    def open_new(self):

        self.untitledDocCount += 1

        dirname = Path.home()
        filename = 'untitled' + str(self.untitledDocCount)
        newfile = Path(dirname, filename)

        self.load_file_in_editor(Path(newfile).as_uri())

    def load_file_in_editor(self, file_uri):

        if not 'untitled' in file_uri:
            # look if untitled empty
            page_num = self.notebook.get_n_pages()
            logger.debug('page_num {}'.format(page_num))
            if page_num:
                editor = self.get_editor()
                start_iter, end_iter = editor.get_buffer().get_bounds()
                if start_iter.equal(end_iter):
                    logger.debug('empty buffer')
                    # load in existing buffer
                    editor.document.set_uri(file_uri)
                    editor.load_file(editor.document)
                    self.change_language_selection(editor)
                    self.set_title(editor.document)
                    self.untitledDocCount -= 1
                    return
        # make new page
        try:
            editor = EditorApp(self, file_uri)
        except:
            logger.warn('Something went terrible wrong')
        else:
            self.notebook.append_page(editor, self.create_tab_label(editor))
            self.notebook.set_current_page(-1)

            buf = editor.get_buffer()
            buf.connect('modified_changed', self.on_buffer_modified)
            buf.connect('mark_set', self.update_cursor_location)
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

            logger.debug('file {} loaded in buffer, modified {}'.format(file_uri, buf.get_modified()))
        return 1

    def save_file_as(self, editor):

        logger.debug('dialog save_file_as: {}'.format(editor.document.get_uri()))

        save_dialog = Gtk.FileChooserDialog('Pick a file', self.window,
                                            Gtk.FileChooserAction.SAVE,
                                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                             Gtk.STOCK_SAVE, Gtk.ResponseType.ACCEPT))
        save_dialog.set_do_overwrite_confirmation(True)
        save_dialog.set_local_only(False)
        try:
            save_dialog.set_uri(editor.document.get_uri())
        except GObject.GError as e:
            logger.error('# Error: {}'.format(e.message))

        save_dialog.connect('response', self.save_file_as_response, editor)
        save_dialog.show()

    def save_file_as_response(self, dialog, response, editor):

        save_dialog = dialog
        if response == Gtk.ResponseType.ACCEPT:
            filename = Path(save_dialog.get_filename())  # or uri?

            # check for right suffix
            if editor.this_lang:
                if editor.this_lang.get_name() == 'EVC':
                    if not filename.suffix == '.evc':
                        logger.debug('No suffix')
                        filename = filename.with_suffix('.evc')
                        logger.debug('append suffix: {}'.format(filename.name))
                if editor.this_lang.get_name() == 'NXC':
                    if not filename.suffix == '.nxc':
                        logger.debug('No suffix')
                        filename = filename.with_suffix('.nxc')
                        logger.debug('append suffix: {}'.format(filename.name))

            # check for valid filename
            if self.forbiddenchar.match(filename.stem) is not None:
                editor.document.set_uri(filename.as_uri())
                if logger.isEnabledFor(logging.DEBUG):
                    page_num = self.notebook.page_num(editor)
                    logger.debug('func save_file_as_response: %s on tab %s, '
                                 % (editor.document.get_uri(), page_num))

                self.save_file_sync(editor)

                # change language according file extension, e.g. new created files
                editor.set_completion(editor.document)
                self.change_language_selection(editor)
                # change tab label
                self.change_tab_label(editor, editor.document.get_basename())
                # change headerbar
                self.set_title(editor.document)
                dialog.destroy()
            else:
                self.dlg_something_wrong(
                    'Filename {} unvalid!'.format(filename.name),
                    'Filename contains non-alphanumeric characters.')
                save_dialog.set_uri(editor.document.get_uri())

        elif response == Gtk.ResponseType.CANCEL:
            logger.debug('cancelled: SAVE AS')
            dialog.destroy()

    def save_file_sync(self, editor):

        if 'untitled' in editor.document.get_basename():
            logger.debug('Found untitled file: {}'.format(editor.document.get_uri()))
            self.save_file_as(editor)
        else:
            buf = editor.get_buffer()
            start, end = buf.get_bounds()
            content = buf.get_text(start, end, False)
            f = editor.document.gio_file
            try:
                f.replace_contents(content.encode(), None, False, Gio.FileCreateFlags(0),None)
                logger.debug('file {} saved sync'.format(editor.document.get_uri()))
            except GLib.Error as e:
                logger.error('# Error: {}'.format(e.message))
            else:
                if buf.get_modified():
                    buf.set_modified(False)
                    logger.debug('set buffer modified {}'.format(buf.get_modified()))

    def save_file_async(self, editor):

        if 'untitled' in editor.document.get_basename():
            logger.debug('Found untitled file: {}'.format(editor.document.get_uri()))
            self.save_file_as(editor)
        else:
            buf = editor.get_buffer()

            try:
                saver = GtkSource.FileSaver.new(buf, editor.document)
                saver.save_async(1, None, None, None, self.on_save_async_finish, editor)
            except GObject.GError as e:
                logger.error('# Error: {}'.format(e.message))

    def on_save_async_finish(self, source, result, editor):

        try:
            # async saving, we have to wait for finish before removing
            success = source.save_finish(result)
            logger.debug('file {} saved async {}'.format(editor.document.get_uri(), success))
        except GObject.GError as e:
            logger.error('problem saving file {}'.format(e.message))
            self.dlg_something_wrong(
                'Could not save file {}'.format(editor.document.get_uri()),
                e.message)
        else:
            buf = editor.get_buffer()
            if buf.get_modified():
                buf.set_modified(False)
                logger.debug('set buffer modified {}'.format(buf.get_modified()))

    def dlg_something_wrong(self, what, why):

        dlg = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.INFO,
                                Gtk.ButtonsType.OK, what)
        dlg.format_secondary_text(why)

        dlg.run()
        dlg.destroy()

    def dlg_close_confirmation(self, editor):

        dlg = CloseConfirmationDialog(self.window, editor.document.get_basename())
        response = dlg.run()

        page_num = self.notebook.page_num(editor)
        if response == Gtk.ResponseType.NO:
            logger.debug('Close tab without saving')
            self.notebook.remove_page(page_num)
            try:
                editor.destroy()
            except:
                logger.debug('Nothing to destroy')

        elif response == Gtk.ResponseType.CANCEL:
            logger.debug('Cancel closing tab')

        elif response == Gtk.ResponseType.YES:
            logger.debug('Save file before closing')
            # synchronous saving - otherwise page removed
            # before save_finish
            self.save_file_sync(editor)
            self.notebook.remove_page(page_num)
            editor.destroy()

        # if the messagedialog is destroyed (by pressing ESC)
        elif response == Gtk.ResponseType.DELETE_EVENT:
            logger.debug('dialog closed or cancelled')
        # finally, destroy the messagedialog
        dlg.destroy()

    def create_tab_label(self, editor):
        ''' create tab header with close button '''
        closebtn = Gtk.Button()
        icon = Gio.ThemedIcon(name='window-close')
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        closebtn.set_image(image)
        closebtn.set_relief(Gtk.ReliefStyle.NONE)
        closebtn.connect('clicked', self.on_btn_close_tab_clicked, editor)

        box = Gtk.HBox()
        box.pack_start(Gtk.Label(editor.document.get_basename()), True, True, 0)
        box.pack_end(closebtn, False, False, 0)
        box.show_all()
        return box

    def change_tab_label(self, editor, filename):
        ''' language change or save as '''
        buf = editor.get_buffer()
        if buf.get_modified() and not filename.startswith('*'): 
            filename = '*'+filename
        box = self.notebook.get_tab_label(editor)
        if box:
            widglist = box.get_children()
            widglist[0].set_text(filename)

    def on_buffer_modified(self, widget):
        ''' callback for buffer '''
        editor = self.get_editor()
        if editor:
            buf = editor.get_buffer()
            logger.debug('modified tab {}'.format(buf.get_modified()))

            filename = editor.document.get_basename()

            if buf.get_modified(): 
                filename = '*'+filename
            else:
                if filename.startswith('*'):
                    filename = filename[1:]

            self.change_tab_label(editor, filename)

    def on_notebook_switch_page(self, notebook, page, page_num):
        '''change headerbar and language selection accordingly'''
        editor = self.notebook.get_nth_page(page_num)
        self.change_language_selection(editor)
        self.set_title(editor.document)

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
            logger.debug('Language selected %s', model[treeiter][0])
            self.language_label.set_text(model[treeiter][1])

            editor = self.get_editor()
            file_uri = Path(editor.document.get_uri())

            if model[treeiter][0] == 'nxc':
                editor.document.set_uri(str(file_uri.with_suffix('.nxc')))
            if model[treeiter][0] == 'evc':
                editor.document.set_uri(str(file_uri.with_suffix('.evc')))
            editor.set_completion(editor.document)
            self.set_title(editor.document)
            self.change_tab_label(editor, editor.document.get_basename())
            self.languagemenu.hide()
            editor.codeview.grab_focus()

    def change_language_selection(self, editor):
        '''changes language_label and language_tree on load file and on switch page'''
        editor.this_lang = editor.lm.guess_language(editor.document.get_basename(), None)

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
        select.connect('changed', self.on_languageselect_changed)

    def set_title(self, document):
        self.headerbar.set_title(document.get_basename())
        self.headerbar.set_subtitle(document.get_path())

    def update_cursor_location(self, buf, location, mark):
        self.cursor_location.pop(self.cursor_location_id)

        #iter = buffer.get_iter_at_mark(buffer.get_insert())
        pos = buf.props.cursor_position
        cursor_it = buf.get_iter_at_offset(pos)
        row = cursor_it.get_line()
        col = cursor_it.get_line_offset()

        msg = 'Ln {}, Col {}'.format(row+1, col+1)
        self.cursor_location.push(self.cursor_location_id, msg)

    def get_editor(self):
        page_num = self.notebook.get_current_page()
        return self.notebook.get_nth_page(page_num)

    def idle_nbc_proc(self, window, document, upload: bool=False):
        '''
        compile and upload file to NXT brick
        '''
        helper = BrickHelper(self.application)

        (error, msg) = helper.nbc_proc(document, upload)
        if error == 2:
            dlg_something_wrong(
                'No NBC-executable found!',
                'not in /usr/bin, not in /usr/local/bin')
        else:
            self.log_buffer.set_text(msg)
            self.format_log(self.log_buffer.get_start_iter())

        self.window.get_window().set_cursor(None)

    def idle_evc_proc(self, window, document, upload: bool=False):
        '''
        compile and upload file to EV3 brick
        '''
        helper = BrickHelper(self.application)

        prjname = Path(document.get_basename()).stem

        starter = 0
        msg=''
        gcc_error = 0

        if self.forbiddenchar.match(Path(document.get_path()).name) is not None:
            gcc_error = helper.cross_compile(document)
            if gcc_error:
                msg = '# Error: {}'.format(gcc_error)
                upload = False
            else:
                msg = 'Compile successfull\n'
        else:
            msg = 'filename contains non-alphanumeric characters\n'
            upload = False
        if upload:
            if not gcc_error:
                starter = helper.mkstarter(document)
                msg += 'Build starter successfull\n'
            if starter:
                filename = Path(document.get_parent(), prjname + '.rbf')
                errora = helper.ev3_upload(filename)
                if errora:
                    msg += '# Error: Failed to upload {}.rbf, try again\n'.format(filename)
                else:
                    msg += 'Upload of {}.rbf successfull\n'.format(prjname)
                filename = Path(document.get_parent(), prjname)
                errorb = helper.ev3_upload(filename)
                if errorb:
                    msg += '# Error: Failed to upload {}, try again\n'.format(filename)
                else:
                    msg += 'Upload of {} successfull\n'.format(prjname)

                if not errora and not errorb:
                    self.application.ev3brick.play_sound('./ui/DownloadSucces')

        self.log_buffer.set_text(msg)
        self.format_log(self.log_buffer.get_start_iter())

    def format_log(self, start_iter):
        '''
        eye candy for error message
        '''
        end = self.log_buffer.get_end_iter()
        match = start_iter.forward_search('# Error:', 0, end)
        if match != None:
            match_start, match_end = match
            self.log_buffer.apply_tag_by_name('warning', match_start, match_end)
            self.format_log(match_end)

        self.window.get_window().set_cursor(None)

class FileOpenDialog(Gtk.FileChooserDialog):

    def __init__(self, parent, path):

        Gtk.FileChooserDialog.__init__(self, 'Please choose a file', parent,
                                       Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_OPEN, Gtk.ResponseType.ACCEPT))

        # Set the current folder
        #path = document.get_parent()
        self.set_current_folder(path)

        self.set_local_only(False)

        filter_brickc = Gtk.FileFilter()
        filter_brickc.set_name('Brick files')
        filter_brickc.add_pattern('*.evc')
        filter_brickc.add_pattern('*.nxc')
        self.add_filter(filter_brickc)

        filter_any = Gtk.FileFilter()
        filter_any.set_name('Any files')
        filter_any.add_pattern('*')
        self.add_filter(filter_any)


class CloseConfirmationDialog(Gtk.MessageDialog):

    def __init__(self, parent, filename):
        Gtk.MessageDialog.__init__(self, parent, 0, Gtk.MessageType.WARNING,
                                Gtk.ButtonsType.NONE,
                                'Save changes to document {} before closing?'.format(filename))
        self.add_buttons('Close without Saving', Gtk.ResponseType.NO,
                         'Cancel', Gtk.ResponseType.CANCEL,
                         'Save', Gtk.ResponseType.YES)
        self.format_secondary_text('Changes to document {} will be permanently lost.'
                                   .format(filename))
        self.set_default_response(Gtk.ResponseType.YES)


class PrintingApp:
    '''
    Print with syntax highlightning
    '''

    def __init__(self, textview):
        self.operation = Gtk.PrintOperation.new()
        self.compositor = GtkSource.PrintCompositor.new_from_view(textview.codeview)

        self.compositor.set_header_format(True, textview.document.get_path(), None, None)
        self.compositor.set_print_header(True)
        self.compositor.set_body_font_name('Monospace 10')

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

        logger.debug('Initializing printing process...')

        while not compositor.paginate(context):
            pass
        n_pages = compositor.get_n_pages()
        operation.set_n_pages(n_pages)

        logger.debug('Sending %s pages to printer', n_pages)

    def draw_page(self, operation, context, page_num, compositor):

        logger.debug('Sending page: %s', (page_num+1))

        compositor.draw_page(context, page_num)

    def end_print(self, operation, context):

        logger.debug('Document sent to printer')

