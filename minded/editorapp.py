#!/usr/bin/env python3
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

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import Gtk, Gdk, Gio, GObject, Pango
gi.require_version('GtkSource', '3.0')
from gi.repository import GtkSource

import logging
logger = logging.getLogger(__name__)

from minded.brickcompletionprovider import BrickCompletionProvider

SIMPLE_COMPLETE = 0

class MindEdDocument(GtkSource.File):
    def __init__(self, file_uri):
        GtkSource.File.__init__(self)
        self.gio_file = Gio.File.new_for_uri(file_uri)
        self.set_location(self.gio_file)

    def get_uri(self):
        '''file:///path/to/the/file.ext'''
        return self.gio_file.get_uri()

    def set_uri(self, documenturi):
        '''new uri eg save as'''
        old_uri = self.gio_file.get_uri()
        # self.gio_file.unref() raise RuntimeError('This method is currently unsupported.')
        self.gio_file = Gio.File.new_for_uri(documenturi)
        self.set_location(self.gio_file)
        logger.debug('old {} gio_file to new {}'.format(old_uri, self.gio_file.get_uri()))

    def get_path(self):
        '''/path/to/the/file.ext'''
        return self.gio_file.get_path()

    def get_parent(self):
        '''/path/to/the/'''
        return self.gio_file.get_parent().get_path()

    def get_basename(self):
        '''file.ext'''
        return self.gio_file.get_basename()

class EditorApp(Gtk.ScrolledWindow):

    def __init__(self, mindedappwin, file_uri):
        Gtk.ScrolledWindow.__init__(self)
        self.set_hexpand(True)
        self.set_vexpand(True)
        
        self.mindedappwin = mindedappwin

        # look for settings
        srcdir = Path(__file__).parents[1]
        logger.debug('SettingsDir: {}'.format(srcdir))
        if Path(srcdir, 'data').exists():
            # local schema for developping only
            schema_source = Gio.SettingsSchemaSource.new_from_directory(
                str(Path(srcdir, 'data')),
                Gio.SettingsSchemaSource.get_default(), False)
            schema = Gio.SettingsSchemaSource.lookup(
                schema_source, 'org.gge-em.MindEd', False)
            logger.debug('Gsettings schema: {}'.format(schema.get_path()))
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

        self.settings.bind('linenumbers', self.codeview, 'show-line-numbers',
                            Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind('showrightmargin', self.codeview, 'show-right-margin',
                            Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind('setrightmargin', self.codeview, 'right-margin-position',
                            Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind('autoindent', self.codeview, 'auto-indent',
                            Gio.SettingsBindFlags.DEFAULT)
        # selected lines are indented instead of being replaced, shift+tab unindents
        self.settings.bind('indentontab', self.codeview, 'indent-on-tab',
                            Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind('tabwidth', self.codeview, 'tab-width',
                            Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind('spacesinsteadtab', self.codeview, 'insert-spaces-instead-of-tabs',
                            Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind('highlightcurrentline', self.codeview, 'highlight-current-line',
                            Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind('highlightmatchingbrackets', self.buffer, 'highlight-matching-brackets',
                            Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind('smartbackspace', self.codeview, 'smart-backspace',
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

        self.document = MindEdDocument(file_uri)
        # throws error if file not exists -> load empty buffer
        #try:
        #    info = self.document.gio_file.query_info('standard::type,standard::size',
        #                                             Gio.FileQueryInfoFlags(0))
        #    self.load_file(self.document)
        #except Exception as e:
        #    logger.debug(str(e))
        if self.document.gio_file.query_exists(None):
            self.load_file(self.document)

    def load_file(self, document):
        # load into GtkSource.Buffer as GtkSource.File
        try:
            loader = GtkSource.FileLoader.new(self.codeview.get_buffer(), document)
            loader.load_async(1, None, None, None, self.file_load_finish, document)
        except GObject.GError as e:
            logger.warn("Error: " + e.message)

    def file_load_finish(self, source, result, document):
        success = False
        try:
            success = source.load_finish(result)
        except GObject.GError as e:
            # happens on new file, if not exists <- hopefully no more
            logger.warn(e.message)
        if success:
            self.set_completion(document)
        else:
            logger.debug('Could not load {}'.format(document.get_path()))

    def set_completion(self, document):
        ''' set syntax highlight and completion '''
        self.this_lang = self.lm.guess_language(document.get_path(), None)
        if self.this_lang:
            if not self.buffer.get_highlight_syntax():
                self.buffer.set_highlight_syntax(True)
            self.buffer.set_language(self.this_lang)
            logger.debug('LanguageManager: {}'.format(self.this_lang.get_name()))
            self.custom_completion_provider.set_completion_list(self.this_lang)
        else:
            logger.warn('No language found for file {}'.format(document.get_path()))
            if self.buffer.get_highlight_syntax():
                self.buffer.set_highlight_syntax(False)
            self.buffer.set_language(None)

    def drag_motion(self,wid, context, x, y, time):
        Gdk.drag_status(context, Gdk.DragAction.COPY | Gdk.DragAction.MOVE, time)
        return True

    def drag_data_received(self, source_widget, context, x, y, selection,
        info, etime):

        if selection.get_target().name() == 'text/uri-list':
            logger.debug("DnD: got text-uri")
            logger.debug('DnDaction %s' % context.get_actions())
            data = selection.get_data()
            logger.debug('DnD dropped: %s' % data)
            #logger.debug('Buffersize: %s ' % len(self.buffer.props.text))
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
            print('DnD: got %s' % selection.get_target())
            print('DnDaction %s' % context.get_actions())
        '''
        #print('got %s' % selection.get_target())
        #print(type(selection.get_target()))
        
        #file_uris = selection.get_text()
        file_uris = selection.get_data()
        if context.get_actions() == Gdk.DragAction.COPY:
            logger.debug(context.get_actions())
            
            for f in file_uris:
                logger.debug('dropped: %s' % file_uris)
        else:
            logger.debug('what happend?')
            logger.debug(context.get_actions())
            #logger.debug('dropped: %s' % file_uris)
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

        # auto_close_paren
        if self.is_opening_paren(ch):
            logger.debug('opening_paren {}'.format(ch))
            # don't insert parens if right of opening_paren
            iter1 = doc.get_iter_at_mark(doc.get_insert())
            iter1.backward_char()
            lb = iter1.get_char()
            if lb in self.opening_parens:
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
                logger.debug('Insert new line and indent {}'.format(view.get_tab_width()))
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
        # don't insert comma if left of one, instead move right
        if not handled and (ch == ',' or event.keyval == Gdk.KEY_Tab):
            logger.debug('KeyEvent: {}'.format(ch))
            iter1 = doc.get_iter_at_mark(doc.get_insert())
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
        char = iter1.get_char()
        return not (char.isalnum() or char == '_')

    def auto_close_paren(self, doc, opening_paren):
        closing_paren = self.get_matching_closing_paren(opening_paren)
        doc.begin_user_action()
        doc.insert_at_cursor(opening_paren + closing_paren)
        iter1 = doc.get_iter_at_mark(doc.get_insert())
        iter1.backward_char()
        doc.place_cursor(iter1)
        doc.end_user_action()
        logger.debug('autoclosed by {}'.format(closing_paren))
        return True

    def get_matching_closing_paren(self,opener):
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
            if char == ' ' or char == '\t':
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
        logger.debug('opening {}'.format(self.opening_parens))
        logger.debug('closing {}'.format(self.closing_parens))
    # end bracket completion
