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
from gettext import gettext as _
import logging

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import Gtk, Gdk, Gio, GObject
gi.require_version('GtkSource', '3.0')
from gi.repository import GtkSource

from minded.minded_editorapp import EditorApp, MindEdDocument
from minded.minded_brickhelper import BrickHelper
from minded.minded_brickinfo import BrickInfo
from minded.minded_brickfiler import BrickFiler
from minded.minded_apiviewer import ApiViewer
from minded.minded_widgets import ErrorDialog, FileOpenDialog, CancelProcDialog
from minded.minded_widgets import CloseConfirmationDialog, MindedTabLabel

LOGGER = logging.getLogger(__name__)

def add_simple_action(self, name, callback):
    action = Gio.SimpleAction.new(name, None)
    action.connect('activate', callback)
    self.add_action(action)

def document_is_open(self, document_uri):
    for page_num in range(self.notebook.get_n_pages()-1, -1, -1):
            editor = self.notebook.get_nth_page(page_num)
            LOGGER.debug('doc_uri:{}, get_uri: {}'.format(document_uri,
                         editor.document.get_uri()))
            if editor.document.get_uri() == document_uri:
                # first page has page_num 0
                return page_num + 1
    return 0

class MindEdAppWin(Gtk.ApplicationWindow):
    '''The Main Application Window'''

    def __init__(self, files, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #for key in kwargs:
        #    print("%s : %s" % (key, kwargs[key]))
        self.app = kwargs['application']
        #LOGGER.debug('Application: {}'.format(self.app))
        #LOGGER.debug('Filelist: {}'.format(files))

        self.set_default_size(800, 600)

        self.set_application(self.app)
        # flag for delete-event on modified document
        self.can_close = True  # type: bool

        actions = [
            ['new_doc', self.on_btn_new_clicked],
            ['open_doc', self.on_btn_open_clicked],
            ['save_doc', self.on_btn_save_clicked],
            ['save_doc_as', self.on_btn_save_as_clicked],
            ['print_doc', self.on_btn_print_clicked],
            ['close_doc', self.on_doc_close_request],
            #['transmit', self.on_btn_transmit_clicked],
            #['compile', self.on_btn_compile_clicked],
            ['brick_info', self.on_btn_brickinfo_clicked],
            ['brick_filer', self.on_btn_brickfiler_clicked],
            ['api_browser', self.on_btn_apiviewer_clicked],
            ['overwrite_mode', self.on_key_insert],
            ['select_lang', self.on_btn_language_clicked]
        ]
        for action in actions:
            add_simple_action(self, action[0], action[1])
        del actions

        # a name as identifier is needed to enable/disable action
        # so i can't do this with add_simple_action
        self.compile_action = Gio.SimpleAction.new('compile', None)
        self.compile_action.connect('activate', self.on_btn_compile_clicked)
        self.add_action(self.compile_action)

        self.transmit_action = Gio.SimpleAction.new('transmit', None)
        self.transmit_action.connect('activate', self.on_btn_transmit_clicked)
        self.add_action(self.transmit_action)
        self.transmit_action.set_enabled(False)

        accels = [
            ['win.new_doc', ['<Ctrl>n']],
            ['win.open_doc', ['<Ctrl>o']],
            ['win.save_doc', ['<Ctrl>s']],
            ['win.save_doc_as', ['<Ctrl><Shift>s']],
            ['win.print_doc', ['<Ctrl>p']],
            ['win.close_doc', ['<Ctrl>w']],
            ['win.transmit', ['F6']],
            ['win.compile', ['F5']],
            ['win.overwrite_mode', ['Insert']],
            ['win.select_lang', ['<Ctrl>l']]
        ]
        for accel in accels:
            self.app.set_accels_for_action(accel[0], accel[1])
        del accels

        builder = Gtk.Builder()
        GObject.type_register(GtkSource.View)
        builder.add_from_resource('/org/gge-em/MindEd/minded-appwin.ui')
        builder.connect_signals(self)
        self.connect('delete-event', self.gtk_main_quit)

        box = builder.get_object('TopBox')

        self.notebook = builder.get_object('notebook')

        self.headerbar = builder.get_object('headerbar')
        self.set_titlebar(self.headerbar)

        self.brick_status = builder.get_object('brick_status')
        self.brick_status_id = self.brick_status.get_context_id('BrickStatus')
        self.overwrite_status = builder.get_object('ovw_status')
        #self.overwrite_status_id = self.overwrite_status.get_context_id('ovw_id')
        self.cursor_location = builder.get_object('colln_status')
        self.cursor_location_id = self.cursor_location.get_context_id('ColLn')
        self.btn_language = builder.get_object('btn_language')
        self.btn_language.set_sensitive(False)

        self.language_label = builder.get_object('language_label')
        self.languagemenu = builder.get_object('languagemenu')
        self.language_tree = builder.get_object('languagetree')
        self.language_store = builder.get_object('language_store')

        compilerview = builder.get_object('compilerview')
        self.log_buffer = compilerview.get_buffer()
        self.log_buffer.create_tag('warning', foreground='red', background='yellow')

        self.canceldlg = None

        # Look for Brick
        if self.app.nxt_brick:
            self.brick_status.push(self.brick_status_id, 'NXT')
            self.transmit_action.set_enabled(True)
        elif self.app.ev3_brick:
            self.brick_status.push(self.brick_status_id, 'EV3')
            self.transmit_action.set_enabled(True)

        self.add(box)

        loaded_files = 0
        if len(files) > 1:
            for nth_file in files[1:]:
                if Path(nth_file).is_file():
                    if self.load_file_in_editor(Path(nth_file).resolve().as_uri()):
                        LOGGER.debug('loaded {}'.format(nth_file))
                        loaded_files += 1
            LOGGER.debug('{} files loaded'.format(loaded_files))
        if not loaded_files:
            self.open_new()

    def gtk_main_quit(self, *args):
        '''
        TopWin CloseButton clicked, are there unsaved changes
        '''
        # get_n_pages from 0...n-1, remove reversed!
        for page_num in range(self.notebook.get_n_pages()-1, -1, -1):

            LOGGER.debug('Window close clicked! Remove page {}'.format(page_num))

            editor = self.notebook.get_nth_page(page_num)
            buf = editor.get_buffer()
            if buf.get_modified():

                dlg = CloseConfirmationDialog(self, editor.document.get_basename())
                response = dlg.run()

                if response == Gtk.ResponseType.NO:
                    LOGGER.debug('Close tab without saving')
                    self.notebook.remove_page(page_num)
                    dlg.destroy()
                elif response == Gtk.ResponseType.CANCEL:
                    LOGGER.debug('Cancel closing tab')
                    dlg.destroy()
                    return True
                elif response == Gtk.ResponseType.YES:
                    LOGGER.debug('Save file on page {} before closing'.format(page_num))
                    self.can_close = False
                    editor.save_file_async(True, editor.document.get_newline_type())
                    dlg.destroy()
                    if not self.can_close:
                        return True
                # if the messagedialog is destroyed (by pressing ESC)
                elif response == Gtk.ResponseType.DELETE_EVENT:
                    LOGGER.debug('dialog closed or cancelled')
                    dlg.destroy()

            else:
                #self.notebook.remove_page(page_num)
                self.close_this_tab(page_num, editor)

        if self.notebook.get_n_pages() == 0:
            LOGGER.debug('No more pages - destroy win')
            self.app.quit()

    def on_btn_new_clicked(self, action, param):
        '''
        gaction: new_doc
        '''
        self.open_new()

    def on_btn_open_clicked(self, action, param):
        '''
        gaction: open_doc
        '''
        # get directory of current document
        if self.notebook.get_n_pages():
            editor = self.get_editor()
            path = editor.document.get_parent()
        else:
            # zero pages
            path = Path.home().joinpath('untitled').as_uri()
            # make new page
            self.make_new_page(path)
            editor = self.get_editor()

        dialog = FileOpenDialog(self, path)
        dialog.connect('response', self.open_file_response, editor)
        dialog.show()

    def open_file_response(self, dialog, response, editor):
        '''
        load or present selected file
        '''
        if response == Gtk.ResponseType.ACCEPT:
            LOGGER.debug('FileOpenDialog File selected: {}'.format(dialog.get_uri()))
            # check if file already open
            page_num = document_is_open(self, dialog.get_uri())
            LOGGER.debug('page_num {}'.format(page_num))
            if page_num:
                self.notebook.set_current_page(page_num - 1)
            else:
                self.load_file_in_editor(dialog.get_uri())

        elif response == Gtk.ResponseType.CANCEL:
            LOGGER.debug('FileOpenDialog Cancel clicked')

        dialog.destroy()

    def on_btn_save_clicked(self, action, param):
        '''
        gaction: save_doc
        '''
        editor = self.get_editor()
        editor.save_file_async(False, editor.document.get_newline_type())

    def on_btn_save_as_clicked(self, action, param):
        '''
        gaction: save_doc_as
        '''
        editor = self.get_editor()
        editor.save_file_as(False)

    def on_doc_close_request(self, action, param):
        '''
        gaction: close_doc, accelerator <Ctrl>w
        on current page
        '''
        page_num = self.notebook.get_current_page()
        LOGGER.debug('action: close tab {}'.format(page_num))
        if page_num != -1:
            editor = self.notebook.get_nth_page(page_num)
            self.close_this_tab(page_num, editor)

    def on_btn_close_tab_clicked(self, button, editor):
        '''tab-close-button on any page clicked'''
        # widget must be child of page, that is editor
        page_num = self.notebook.page_num(editor)
        LOGGER.debug('close tab {}'.format(page_num))
        self.close_this_tab(page_num, editor)

    def close_this_tab(self, page_num, editor):
        '''
        closes a notebook-page
        '''
        if page_num != -1 and not editor.get_buffer().get_modified():
            if 'untitled' in editor.document.get_basename():
                editor.document.dec_untitled()

            else:
                # GLib.Error: »/home/selles/untitled1«: No such file or directory
                # save cursor position
                info = editor.document.gio_file.query_info('metadata::gedit-position',
                                                           Gio.FileQueryInfoFlags.NONE,
                                                           None)
                LOGGER.debug('metadata::gedit-position {}'.format(
                             info.get_attribute_as_string('metadata::gedit-position')))
                mark = editor.get_buffer().get_insert()
                titer = editor.get_buffer().get_iter_at_mark(mark)
                offset = titer.get_offset()
                editor.document.gio_file.set_attribute_string('metadata::gedit-position',
                                                            str(offset),
                                                            Gio.FileQueryInfoFlags.NONE,
                                                            None)

            self.notebook.remove_page(page_num)
            #TODO check for empty notebook, disable save-, save_as-, print-action
        else:
            LOGGER.debug('file modified, save before closing')
            self.dlg_close_confirmation(editor)

    def on_btn_compile_clicked(self, action, param):
        '''
        compile the saved file
        '''
        editor = self.get_editor()
        if editor.get_buffer().get_modified():
            ErrorDialog(self,
                        _('You have to save first!'),
                        _('The compiler works on the real file.'))
        else:
            ext = Path(editor.document.get_basename()).suffix
            if ext == '.nxc':
                # change cursor
                watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
                self.get_window().set_cursor(watch_cursor)
                # don't starve the gui thread before it can change the cursor,
                # call the time consuming in an idle callback
                GObject.idle_add(self.idle_nbc_proc, self, editor.document, False)
            elif ext == '.evc':
                watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
                self.get_window().set_cursor(watch_cursor)
                GObject.idle_add(self.idle_evc_proc, self, editor.document)
            else:
                self.log_buffer.set_text(_('# Error: unknown file extension, expected: .nxc or .evc'))
                self.format_log(self.log_buffer.get_start_iter())

    def on_btn_transmit_clicked(self, action, param):
        '''
        transmit compiled file to brick
        '''
        editor = self.get_editor()
        if editor.get_buffer().get_modified():
            ErrorDialog(self,
                        _('You have to save first!'),
                        _('The compiler works on the real file.'))
        else:
            ext = Path(editor.document.get_basename()).suffix
            if ext == '.nxc':
                # change cursor
                watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
                self.get_window().set_cursor(watch_cursor)
                # don't starve the gui thread before it can change the cursor,
                # call the time consuming in an idle callback
                GObject.idle_add(self.idle_nbc_proc, self, editor.document, True)
            elif ext == '.evc':
                watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
                self.get_window().set_cursor(watch_cursor)
                GObject.idle_add(self.idle_evc_proc, self, editor.document, True)
            else:
                self.log_buffer.set_text(_('# Error: unknown file extension, expected: .nxc or .evc'))
                self.format_log(self.log_buffer.get_start_iter())

    def on_btn_print_clicked(self, action, param):
        '''
        open print app
        '''
        printer = PrintingApp(self.get_editor())
        printer.run()

    def on_btn_brickinfo_clicked(self, action, param):
        '''
        open new window with brick information like name, firmware...
        '''
        BrickInfo(self.app)

    def on_btn_brickfiler_clicked(self, action, param):
        '''
        open new window with brick file browser...
        '''
        BrickFiler(self.app)

    def on_btn_apiviewer_clicked(self, action, param):
        '''
        open new window with API reference browser
        '''
        ApiViewer(self.app)

    def open_new(self):
        '''
        open new empty document
        '''
        doc = MindEdDocument('untitled')
        self.load_file_in_editor(doc.get_uri())

    def load_file_in_editor(self, file_uri):
        '''
        create new page and load document(s)
        param: str file_uri
        '''
        page_num = self.notebook.get_n_pages()
        if page_num:
            editor = self.get_editor()
            #   untitled -> new page        untitled and empty doc -> replace with file_uri
            if (not 'untitled' in file_uri) and 'untitled' in editor.document.get_uri():
                start_iter, end_iter = editor.get_buffer().get_bounds()
                if start_iter.equal(end_iter):
                    LOGGER.debug('found empty untitled doc')
                    editor.document.set_uri(file_uri)
                    editor.load_file(editor.document)
                    self.change_language_selection(editor)
                    self.set_title(editor.document)
                    editor.document.dec_untitled()
                    return True
        LOGGER.debug('make new page {}'.format(file_uri))
        if self.make_new_page(file_uri):
            return True

    def make_new_page(self, file_uri):
        '''
        make new page
        '''
        try:
            editor = EditorApp(self, file_uri)
        except Exception as e:
            LOGGER.warning('Something went terrible wrong: %s' % e)
        else:
            self.notebook.append_page(editor, self.create_tab_label(editor))
            self.notebook.set_current_page(-1)

            # this seems not to be in sync with get_overwrite,
            # workaround: GAction accelerated by Insert-Key
            # editor.codeview.connect('toggle-overwrite', self.toggle_overwrite_status)

            self.overwrite_status.set_text('  {}  '.format(_('INS')))

            buf = editor.get_buffer()
            buf.connect('modified_changed', self.on_buffer_modified)
            buf.connect('mark_set', self.update_cursor_location)
            editor.codeview.grab_focus()

            if not self.btn_language.get_sensitive():
                self.btn_language.set_sensitive(True)

            self.change_language_selection(editor)

            LOGGER.debug('file {} loaded in buffer, modified {}'
                         .format(file_uri, buf.get_modified()))
        return True

    def dlg_close_confirmation(self, editor):
        '''
        ask for saving modified document
        '''
        dlg = CloseConfirmationDialog(self, editor.document.get_basename())
        response = dlg.run()

        page_num = self.notebook.page_num(editor)
        if response == Gtk.ResponseType.NO:
            LOGGER.debug('Close tab without saving')
            self.notebook.remove_page(page_num)
        elif response == Gtk.ResponseType.CANCEL:
            LOGGER.debug('Cancel closing tab')
        elif response == Gtk.ResponseType.YES:
            LOGGER.debug('Save file on page {} before closing'.format(page_num))
            editor.save_file_async(True, editor.document.get_newline_type())
        # if the messagedialog is destroyed (by pressing ESC)
        elif response == Gtk.ResponseType.DELETE_EVENT:
            LOGGER.debug('dialog closed or cancelled')
        # finally, destroy the messagedialog
        dlg.destroy()

    def create_tab_label(self, editor):
        '''
        create tab header with close button
        '''
        return MindedTabLabel(self, editor)

    def change_tab_label(self, editor, filename):
        '''
        language change or save as
        '''
        buf = editor.get_buffer()
        if buf.get_modified() and not filename.startswith('*'):
            filename = '*'+filename
        box = self.notebook.get_tab_label(editor)
        if box:
            box.set_text(filename)

    def on_buffer_modified(self, widget):
        '''
        callback for buffer
        '''
        editor = self.get_editor()
        if editor:
            buf = editor.get_buffer()
            LOGGER.debug('modified tab {}'.format(buf.get_modified()))

            filename = editor.document.get_basename()

            if buf.get_modified():
                filename = '*'+filename
            else:
                if filename.startswith('*'):
                    filename = filename[1:]

            self.change_tab_label(editor, filename)

    def on_notebook_switch_page(self, notebook, page, page_num):
        '''
        change headerbar and language selection accordingly
        '''
        self.change_language_selection(page)
        self.set_title(page.document)
        self.change_overwrite_status(page.codeview)

    def on_btn_language_clicked(self, action, param):
        LOGGER.debug('<ctrl>l')
        self.btn_language.get_popover().popup()

    def on_languageselect_changed(self, selection):
        '''
        single click, language changed
        GtkTreeView->GtkTreeSelection->signal: changed
        not good for using <KEY down> or <KEY up>
        '''
        #model, treeiter = selection.get_selected()
        #self.change_language(model, treeiter)
        pass

    def on_languagetree_row_activated(self, treeview, path, column):
        '''
        double click or <Enter>
        '''
        selection = treeview.get_selection()
        model, treeiter = selection.get_selected()
        self.change_language(model, treeiter)

    def change_language(self, model, treeiter):
        '''
        change language for current document
        '''
        if treeiter is not None:
            LOGGER.debug('Language selected {}'.format(model[treeiter][0]))
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
            editor.codeview.set_cursor_visible(True)

    def change_language_selection(self, editor):
        '''
        changes language_label and language_tree on load file and on switch page
        '''
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
        try:
            self.language_tree.set_cursor(path, None, False)    # emits changed-signal
        except UnboundLocalError:
            LOGGER.debug("Known Language, but not in language_tree")

        select.connect('changed', self.on_languageselect_changed)

    def set_title(self, document):
        '''
        set MindEd-win title
        '''
        self.headerbar.set_title(document.get_basename())
        self.headerbar.set_subtitle(document.get_path())

    def on_key_insert(self, action, param):
        '''
        toggle overwrite-mode
        '''
        LOGGER.debug('action: {}, param: {}'.format(action, param))
        view = self.get_editor().codeview
        if view.get_overwrite():
            view.set_overwrite(False)
        else:
            view.set_overwrite(True)

        self.change_overwrite_status(view)

    def change_overwrite_status(self, view):
        '''
        change statusbar according to current overwrite-mode
        '''
        ovr = view.get_overwrite()
        if ovr:
            self.overwrite_status.set_text('  {}  '.format(_('OVR')))
        else:
            self.overwrite_status.set_text('  {}  '.format(_('INS')))

    def update_cursor_location(self, buf, location, mark):
        '''
        show cursor location in statusbar
        '''
        self.cursor_location.pop(self.cursor_location_id)

        pos = buf.props.cursor_position
        cursor_it = buf.get_iter_at_offset(pos)
        row = cursor_it.get_line()
        col = cursor_it.get_line_offset()

        msg = _('Ln {}, Col {}').format(row+1, col+1)
        self.cursor_location.push(self.cursor_location_id, msg)

    def get_editor(self):
        '''
        get EditorApp on current notebook-page
        '''
        page_num = self.notebook.get_current_page()
        return self.notebook.get_nth_page(page_num)

    def idle_nbc_proc(self, window, document, upload: bool = False):
        '''
        compile and upload file to NXT brick
        '''
        msg = ''

        helper = BrickHelper(self.app)
        (nbc_error, nbc_data) = helper.nbc_proc(document, upload)

        if nbc_error == 1:
            # compilation failed
            msg = nbc_data[1].decode()
        elif nbc_error == 0:
            # compilation successful
            msg = '\n'.join([str(i) for i in nbc_data[0].decode().split('\n')[-5:]])
        else:
            # what happened?
            LOGGER.debug('Error: {}, {}'.format(nbc_error, nbc_data[1].decode()))
            ErrorDialog(self,
                        'Error {}:'.format(nbc_error),
                        nbc_data[1].decode())

        self.log_buffer.set_text(msg)
        self.format_log(self.log_buffer.get_start_iter())

        self.get_window().set_cursor(None)

    def idle_evc_proc(self, window, document, upload: bool = False):
        '''
        compile and upload file to EV3 brick
        '''
        helper = BrickHelper(self.app)

        msg = ''

        valid, msgtupel = document.filename_is_valid(Path(document.get_path()))
        if valid:
            (error, msg) = helper.evc_proc(document, upload)
        else:
            msg = msgtupel[1]

        self.log_buffer.set_text(msg)
        self.format_log(self.log_buffer.get_start_iter())

    def format_log(self, start_iter):
        '''
        eye candy for error message
        '''
        end = self.log_buffer.get_end_iter()
        match = start_iter.forward_search('# Error:', 0, end)
        if match is not None:
            match_start, match_end = match
            self.log_buffer.apply_tag_by_name('warning', match_start, match_end)
            self.format_log(match_end)

        self.get_window().set_cursor(None)


class PrintingApp:
    '''
    Print with syntax highlightning
    '''
    # TODO: GtkDialog mapped without a transient parent
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

        LOGGER.debug('Initializing printing process...')

        while not compositor.paginate(context):
            pass
        n_pages = compositor.get_n_pages()
        operation.set_n_pages(n_pages)

        LOGGER.debug('Sending {} pages to printer'.format(n_pages))

    def draw_page(self, operation, context, page_num, compositor):

        LOGGER.debug('Sending page: {}'.format(page_num+1))

        compositor.draw_page(context, page_num)

    def end_print(self, operation, context):

        LOGGER.debug('Document sent to printer')
