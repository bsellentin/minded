# -*- coding: utf-8 -*-

'''
Editor Application of MindEd
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
from gettext import gettext as _
import logging

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import Gtk, Gdk, Gio, GObject, Pango
gi.require_version('GtkSource', '3.0')
from gi.repository import GtkSource

from minded.brickcompletionprovider import BrickCompletionProvider
from minded.widgets import ErrorDialog, FileSaveDialog

LOGGER = logging.getLogger(__name__)

class MindEdDocument(GtkSource.File):
    '''
    representation of a file
    '''

    untitledDocCount = 0

    def __init__(self, file_uri):
        GtkSource.File.__init__(self)

        # bricks don't want prognames with non-alphanumeric characters
        # returns None if non-alphanumeric character found
        self.forbiddenchar = re.compile('^[a-zA-Z0-9_.]+$')

        if file_uri == 'untitled':
            dirname = Path.home()
            MindEdDocument.untitledDocCount += 1
            filename = file_uri + str(MindEdDocument.untitledDocCount)
            file_uri = Path(dirname, filename).as_uri()

        self.gio_file = Gio.File.new_for_uri(file_uri)
        self.set_location(self.gio_file)

    def get_uri(self):
        '''file:///path/to/the/file.ext'''
        return self.gio_file.get_uri()

    def set_uri(self, documenturi):
        '''new uri eg save as'''
        old_uri = self.gio_file.get_uri()
        self.gio_file = Gio.File.new_for_uri(documenturi)
        self.set_location(self.gio_file)
        LOGGER.debug('old {} gio_file to new {}'.format(old_uri, self.gio_file.get_uri()))

    def get_path(self):
        '''/path/to/the/file.ext'''
        return self.gio_file.get_path()

    def get_parent(self):
        '''/path/to/the/'''
        return self.gio_file.get_parent().get_path()

    def get_basename(self):
        '''file.ext'''
        return self.gio_file.get_basename()

    def dec_untitled(self):
        MindEdDocument.untitledDocCount -= 1

    def filename_is_valid(self, newname):
        '''
        p-bricks don't want prognames with non-alphanumeric characters
        nxt max progname length is 15.3, ev3 20.3
        :param newname:  filename as Path '''

        if self.forbiddenchar.match(newname.stem) is not None:
            if newname.suffix == '.nxc' and len(newname.stem) > 15:
                err_msg = _('Filename {} to long!').format(newname.stem)
                hint_msg = _('Maximum allowable are 15 characters')
                return (0, (err_msg, hint_msg))
            if newname.suffix == '.evc' and len(newname.stem) > 20:
                err_msg = _('Filename {} to long!').format(newname.stem)
                hint_msg = _('Maximum allowable are 20 characters')
                return (0, (err_msg, hint_msg))
            LOGGER.debug('valid: {}'.format(newname.stem))
            return (1, (None, None))
        else:
            err_msg = _('Filename {} unvalid!').format(newname)
            hint_msg = _('Filename contains non-alphanumeric characters.')
            return (0, (err_msg, hint_msg))

class EditorApp(Gtk.ScrolledWindow):
    '''This class handels all editing tasks.
    opening and saving MindEdDocuments, setting language manager
    completion is done by class BrickCompletionProvider
    bracket completion
    key event handling
    '''

    def __init__(self, mindedappwin, file_uri):
        Gtk.ScrolledWindow.__init__(self)
        self.set_hexpand(True)
        self.set_vexpand(True)

        self.mindedappwin = mindedappwin

        # look for settings
        srcdir = Path(__file__).parents[1]
        LOGGER.debug('SettingsDir: {}'.format(srcdir))
        if Path(srcdir, 'data').exists():
            # local schema for developping only
            schema_source = Gio.SettingsSchemaSource.new_from_directory(
                str(Path(srcdir, 'data')),
                Gio.SettingsSchemaSource.get_default(), False)
            schema = Gio.SettingsSchemaSource.lookup(
                schema_source, 'org.gge-em.MindEd', False)
            LOGGER.debug('Gsettings schema: {}'.format(schema.get_path()))
            if not schema:
                raise Exception("Cannot get GSettings schema")
            self.settings = Gio.Settings.new_full(schema, None, None)
        else:
            self.settings = Gio.Settings('org.gge-em.MindEd')

        self.buffer = GtkSource.Buffer()
        self.codeview = GtkSource.View().new_with_buffer(self.buffer)

        sm = GtkSource.StyleSchemeManager.get_default()
        sid = GtkSource.StyleSchemeManager.get_scheme(sm, 'minded')
        self.buffer.set_style_scheme(sid)

        setters = [
            ['linenumbers', 'show-line-numbers'],
            ['showrightmargin', 'show-right-margin'],
            ['setrightmargin', 'right-margin-position'],
            ['autoindent', 'auto-indent'],
            ['indentontab', 'indent-on-tab'],
            ['tabwidth', 'tab-width'],
            ['spacesinsteadtab', 'insert-spaces-instead-of-tabs'],
            ['highlightcurrentline', 'highlight-current-line'],
            ['smartbackspace', 'smart-backspace'],
            ['linewrapmode', 'wrap-mode']
        ]
        for setter in setters:
            self.settings.bind(setter[0], self.codeview, setter[1], Gio.SettingsBindFlags.DEFAULT)
        del setters

        self.settings.bind('highlightmatchingbrackets', self.buffer, 'highlight-matching-brackets',
                           Gio.SettingsBindFlags.DEFAULT)

        self.codeview.override_font(Pango.FontDescription(
            self.settings.get_string('fontname')))  # gedit like

        targets = Gtk.TargetList.new(None)
        targets.add_uri_targets(0)
        targets.add_text_targets(1)
        self.codeview.drag_dest_set_target_list(targets)
        #self.codeview.connect('drag_motion', self.drag_motion)
        self.codeview.connect('drag_data_received', self.drag_data_received)
        #self.codeview.connect("drag_drop", self.drag_data_received)

        # for bracket completion
        self.codeview.connect('key-press-event', self.on_key_press)
        self.add_brackets()

        self.add(self.codeview)
        self.show_all()

        self.lm = GtkSource.LanguageManager.new()
        self.this_lang = ()

        self.custom_completion_provider = BrickCompletionProvider(self.this_lang)
        self.codeview_completion = self.codeview.get_completion()
        self.codeview_completion.add_provider(self.custom_completion_provider)

        self.word_completion_provider = GtkSource.CompletionWords.new()
        self.word_completion_provider.register(self.buffer)
        #self.word_completion = self.codeview.get_completion()
        self.codeview_completion.add_provider(self.word_completion_provider)

        self.document = MindEdDocument(file_uri)
        # throws error if file not exists -> load empty buffer
        #try:
        #    info = self.document.gio_file.query_info('standard::type,standard::size',
        #                                             Gio.FileQueryInfoFlags(0))
        #    self.load_file(self.document)
        #except Exception as e:
        #    LOGGER.debug(str(e))
        if self.document.gio_file.query_exists(None):
            self.load_file(self.document)

    def load_file(self, document):
        '''load MindEdDocument async into GtkSource.Buffer'''

        try:
            loader = GtkSource.FileLoader.new(self.codeview.get_buffer(), document)
            loader.load_async(1, None, None, None, self.file_load_finish, document)
        except GObject.GError as e:
            LOGGER.warning("Error: " + e.message)

    def file_load_finish(self, source, result, document):
        success = False
        try:
            success = source.load_finish(result)
        except GObject.GError as e:
            # happens on new file, if not exists <- hopefully no more
            LOGGER.warning(e.message)
        if success:
            self.set_completion(document)
            LOGGER.debug("NewlineType {}".format(document.get_newline_type()))
        else:
            LOGGER.debug('Could not load {}'.format(document.get_path()))

    def save_file_as(self, close_tab):
        '''
        save MindEdDocument async
        '''

        LOGGER.debug('dialog save_file_as: {}'.format(self.document.get_uri()))
        save_dialog = FileSaveDialog(self.mindedappwin, self.document)
        save_dialog.connect('response', self.save_file_as_response, close_tab)
        save_dialog.show()

    def save_file_as_response(self, dialog, response, close_tab):

        #save_dialog = dialog
        if response == Gtk.ResponseType.ACCEPT:
            filename = Path(dialog.get_filename())  # or uri?

            # check for right suffix
            if self.this_lang:
                if self.this_lang.get_name() == 'EVC':
                    if filename.suffix != '.evc':
                        LOGGER.debug('No suffix')
                        filename = filename.with_suffix('.evc')
                        LOGGER.debug('append suffix: {}'.format(filename.name))
                if self.this_lang.get_name() == 'NXC':
                    if filename.suffix != '.nxc':
                        LOGGER.debug('No suffix')
                        filename = filename.with_suffix('.nxc')
                        LOGGER.debug('append suffix: {}'.format(filename.name))

            # check for valid filename
            (valid, msgtupel) = self.document.filename_is_valid(filename)
            if valid:
                self.document.set_uri(filename.as_uri())

                if LOGGER.isEnabledFor(logging.DEBUG):
                    page_num = self.mindedappwin.notebook.page_num(self)
                    LOGGER.debug('func save_file_as_response: {} on tab {}, '
                                 .format(self.document.get_uri(), page_num))

                newline_types = {'linux': GtkSource.NewlineType.LF,
                                 'mac' : GtkSource.NewlineType.CR,
                                 'windows': GtkSource.NewlineType.CR_LF}
                self.save_file_async(close_tab,
                                     newline_types.get(dialog.get_choice('newline_type')))

                dialog.destroy()
            else:
                ErrorDialog(dialog, msgtupel[0], msgtupel[1])
                dialog.set_uri(self.document.get_uri())

        elif response == Gtk.ResponseType.CANCEL:
            LOGGER.debug('cancelled: SAVE AS')
            dialog.destroy()

    def save_file_async(self, close_tab, newline_type):
        '''
        only saving: page_num = None
        save and close tab: page_num to close
        '''
        LOGGER.debug('NewlineType: {}'.format(newline_type))
        if 'untitled' in self.document.get_basename():
            LOGGER.debug('Found untitled file: {}'.format(self.document.get_uri()))
            self.save_file_as(close_tab)
        else:
            buf = self.get_buffer()

            try:
                saver = GtkSource.FileSaver.new(buf, self.document)
                saver.set_newline_type(newline_type)
                saver.save_async(1, None, None, None, self.on_save_async_finish, close_tab)
            except GObject.GError as e:
                LOGGER.error('# Error: {}'.format(e.message))

    def on_save_async_finish(self, source, result, close_tab):
        '''
        wait for async-saving to finish
        '''
        try:
            success = source.save_finish(result)
            LOGGER.debug('file {} saved async {}'.format(self.document.get_uri(), success))

        except GObject.GError as e:
            LOGGER.error('problem saving file {}'.format(e.message))
            ErrorDialog(self,
                _('Could not save file {}').format(self.document.get_uri()),
                e.message)
        else:
            if close_tab:
                # close tab request
                page_num = self.mindedappwin.notebook.page_num(self)
                self.mindedappwin.notebook.remove_page(page_num)
            else:
                buf = self.get_buffer()
                if buf.get_modified():
                    buf.set_modified(False)
                    LOGGER.debug('set buffer modified {}'.format(buf.get_modified()))

                # change language according file extension, e.g. new created files
                self.set_completion(self.document)
                self.mindedappwin.change_language_selection(self)
                # change tab label
                self.mindedappwin.change_tab_label(self, self.document.get_basename())
                # change headerbar
                self.mindedappwin.set_title(self.document)

        if not self.mindedappwin.can_close:
            # there was window-delete-event, but modified document
            self.mindedappwin.can_close = True
            self.mindedappwin.gtk_main_quit()

    def set_completion(self, document):
        '''
        set syntax highlight and completion
        '''
        self.this_lang = self.lm.guess_language(document.get_path(), None)
        if self.this_lang:
            if not self.buffer.get_highlight_syntax():
                self.buffer.set_highlight_syntax(True)
            self.buffer.set_language(self.this_lang)
            LOGGER.debug('LanguageManager: {}'.format(self.this_lang.get_name()))
            self.custom_completion_provider.set_completion_list(self.this_lang)
        else:
            LOGGER.warning('No language found for file {}'.format(document.get_path()))
            if self.buffer.get_highlight_syntax():
                self.buffer.set_highlight_syntax(False)
            self.buffer.set_language(None)

    def drag_motion(self, wid, context, x, y, time):
        Gdk.drag_status(context, Gdk.DragAction.COPY | Gdk.DragAction.MOVE, time)
        return True

    def drag_data_received(self, source_widget, context, x, y, selection,
        info, etime):

        if selection.get_target().name() == 'text/uri-list':
            LOGGER.debug("DnD: got text-uri")
            LOGGER.debug('DnDaction {}'.format(context.get_actions()))
            data = selection.get_data()
            LOGGER.debug('DnD dropped: {}'.format(data))
            #LOGGER.debug('Buffersize: %s ' % len(self.buffer.props.text))
            # check if file already open
            for pagecount in range(self.mindedappwin.notebook.get_n_pages()-1, -1, -1):
                editor = self.mindedappwin.notebook.get_nth_page(pagecount)
                if editor.file == data.decode().strip('\r\n'):
                    self.mindedappwin.notebook.set_current_page(pagecount)
                    break
            else:
                self.mindedappwin.load_file_in_editor(data.decode().strip('\r\n'))

            context.finish(True, False, etime)

        else:
            print('DnD: got {}'.format(selection.get_target()))
            print('DnDaction {}'.format(context.get_actions()))
        '''
        #print('got %s' % selection.get_target())
        #print(type(selection.get_target()))
        
        #file_uris = selection.get_text()
        file_uris = selection.get_data()
        if context.get_actions() == Gdk.DragAction.COPY:
            LOGGER.debug(context.get_actions())
            
            for f in file_uris:
                LOGGER.debug('dropped: %s' % file_uris)
        else:
            LOGGER.debug('what happend?')
            LOGGER.debug(context.get_actions())
            #LOGGER.debug('dropped: %s' % file_uris)
            for t in context.list_targets():
                print(t)
            #context.finish(False, False, etime)
        context.finish(True, False, etime)
        '''
        return True

    def get_buffer(self):
        return self.codeview.get_buffer()

    # bracket completion
    def on_key_press(self, view, event):
        handled = False
        doc = view.get_buffer()
        ch = self.to_char(event.keyval)
        # first handel selection
        if ch:
            selection = doc.get_selection_bounds()
            if selection:
                start, end = selection
                if not start.equal(end):
                    LOGGER.debug('something selected true')
                    doc.begin_user_action()
                    doc.delete(start, end)
                    doc.end_user_action()

        # auto_close_paren
        if self.is_opening_paren(ch):
            LOGGER.debug('opening_paren {}'.format(ch))
            # don't insert parens if right of opening_paren
            iter1 = doc.get_iter_at_mark(doc.get_insert())
            iter1.backward_char()
            lb = iter1.get_char()
            if lb == ch and lb in self.opening_parens:
                LOGGER.debug("there is same opening paren, don't do twice")
                handled = True
            elif self.should_auto_close_paren(doc):
                handled = self.auto_close_paren(doc, ch)

        # autoindent in {}
        if not handled and event.keyval == Gdk.KEY_Return:
            iter1 = doc.get_iter_at_mark(doc.get_insert())
            rb = iter1.get_char()
            iter1.backward_char()
            lb = iter1.get_char()
            if lb == '{' and rb == '}':
                LOGGER.debug('Insert new line and indent {}'.format(view.get_tab_width()))
                text_to_insert = '\n' + self.get_current_line_indent(doc)
                doc.begin_user_action()
                mark = doc.get_insert()
                iter1 = doc.get_iter_at_mark(mark)
                doc.place_cursor(iter1)
                doc.insert_at_cursor(text_to_insert + ' ' * view.get_tab_width())
                doc.insert_at_cursor(text_to_insert)
                mark = doc.get_insert()
                iter2 = doc.get_iter_at_mark(mark)
                iter2.backward_chars(len(text_to_insert))
                doc.place_cursor(iter2)
                doc.end_user_action()
                handled = True
        # move selection to next hint
        # don't insert comma if left of one, instead move right
        if not handled and (ch == ',' or event.keyval == Gdk.KEY_Tab):
            LOGGER.debug('KeyEvent: {}'.format(ch))
            iter1 = doc.get_iter_at_mark(doc.get_insert())
            rb = iter1.get_char()
            if rb == '"': 
                iter1.forward_char()
                rb = iter1.get_char()
            if rb == ',':
                iter1.forward_char()
                word_end = iter1.copy()
                word_end.forward_word_end()
                if iter1.equal(word_end):
                    # no hint
                    doc.place_cursor(iter1)
                else:
                    # select hint
                    word_start = word_end.copy()
                    word_start.backward_word_start()
                    doc.select_range(word_start, word_end)
                handled = True
            # snippets
            else:
                # this runs on Debian Buster, but not on Ubuntu Xenial
                #line_start = iter1.copy()
                #line_start.backward_visible_line()
                #snippet = iter1.backward_search('skel',
                #    Gtk.TextSearchFlags.VISIBLE_ONLY, line_start)

                # idea from gedit-3.18/plugins/snippets/document.py L600
                start = iter1.copy()
                while start.backward_char():
                    c = start.get_char()
                    if start.starts_word():
                        break
                if not start.equal(iter1):
                    word = doc.get_text(start, iter1, False)
                    LOGGER.debug(word)
                    if word == 'skel':
                        snippet = (start, iter1)
                    else:
                        snippet = None

                if snippet:
                    LOGGER.debug('insert snippet')
                    language = doc.get_language()
                    if language:
                        if language.get_name() == 'EVC':
                            text_to_insert = ('#include "ev3.h"\n' +
                                'int main(){\n\tInitEV3();\n\n\t$0\n\n' +
                                '\tFreeEV3();\n\treturn 0;\n}')
                        elif language.get_name() == 'NXC':
                            text_to_insert = 'task main (){\n\t$0\n}'
                        else:
                            LOGGER.debug('no snippet for language {}'.format(language.get_name()))
                            handled = False
                            return handled

                        LOGGER.debug('snippet for language {}'.format(language.get_name()))
                        snip_start, snip_end = snippet
                        doc.delete(snip_start, snip_end)
                        doc.begin_user_action()
                        doc.insert(snip_start, text_to_insert)
                        mark = doc.get_insert()
                        iter1 = doc.get_iter_at_mark(mark)
                        start, end = doc.get_bounds()
                        token = iter1.backward_search('$0',
                            Gtk.TextSearchFlags.VISIBLE_ONLY, start)
                        if token:
                            token_start, token_end = token
                            doc.delete(token_start, token_end)
                            doc.place_cursor(token_start)
                        doc.end_user_action()
                        handled = True
                else:
                    LOGGER.debug('no snippet')

        return handled

    def to_char(self, keyval_or_char):
        '''Convert a event keyval or character to a character'''
        if isinstance(keyval_or_char, str):
            return keyval_or_char
        return chr(keyval_or_char) if 0 < keyval_or_char < 128 else None

    def is_opening_paren(self, char):
        return char in self.opening_parens

    def is_closing_paren(self, char):
        return char in self.closing_parens

    def should_auto_close_paren(self, doc):
        iter1 = doc.get_iter_at_mark(doc.get_insert())
        if iter1.is_end() or iter1.ends_line():
            return True
        #if doc.get_has_selection():
        #    return True
        char = iter1.get_char()
        mark = iter1.get_marks
        LOGGER.debug('%s' % char)
        #LOGGER.debug('%s' % mark)
        # don't close inside words
        return not (char.isalnum() or char == '_')

    def auto_close_paren(self, doc, opening_paren):
        closing_paren = self.get_matching_closing_paren(opening_paren)
        doc.begin_user_action()
        doc.insert_at_cursor(opening_paren + closing_paren)
        iter1 = doc.get_iter_at_mark(doc.get_insert())
        iter1.backward_char()
        doc.place_cursor(iter1)
        doc.end_user_action()
        LOGGER.debug('autoclosed by {}'.format(closing_paren))
        return True

    def get_matching_closing_paren(self, opener):
        try:
            return self.closing_parens[self.opening_parens.index(opener)]
        except ValueError:
            return None

    def get_current_line_indent(self, doc):
        it_start = doc.get_iter_at_mark(doc.get_insert())
        it_start.set_line_offset(0)
        it_end = it_start.copy()
        it_end.forward_to_line_end()
        indentation = []
        while it_start.compare(it_end) < 0:
            char = it_start.get_char()
            if char in (' ', '\t'):
                indentation.append(char)
            else:
                break
            it_start.forward_char()
        return ''.join(indentation)

    def add_brackets(self):

        brackets = '(){}[]""'
        parens = [], []
        for i in range(0, len(brackets), 2):
            parens[0].append(brackets[i+0])
            parens[1].append(brackets[i+1])
        self.opening_parens = parens[0]
        self.closing_parens = parens[1]
        LOGGER.debug('opening {}'.format(self.opening_parens))
        LOGGER.debug('closing {}'.format(self.closing_parens))
    # end bracket completion
