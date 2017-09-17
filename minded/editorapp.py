#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from urllib.parse import urlparse, unquote

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import Gtk, Gdk, Gio, GObject, Pango
gi.require_version('GtkSource', '3.0')
from gi.repository import GtkSource

import logging
logger = logging.getLogger(__name__)

import minded.nxc_funcs as nxc_funcs
from minded.brickcompletionprovider import BrickCompletionProvider

SIMPLE_COMPLETE = 0

class MindEdDocument:
    def __init__(self, documenturl):
        '''file:///path/to/the/file.ext'''
        self.documenturl = documenturl
        #print('documenturl: %s' % self.documenturl)
        parsed = urlparse(unquote(documenturl))
        '''/path/to/the/file.ext'''
        self.filename = parsed.path
        #print('filename: %s' % self.filename)
        '''file.ext'''
        self.shortname = Path(parsed.path).name
        #print('shortname: %s' % self.shortname)
        '''/path/to/the'''
        self.filepath = str(Path(parsed.path).parent)
        #print('filepath: %s' % self.filepath)

    def get_url(self):
        return self.documenturl

    def set_url(self, documenturl):
        self.documenturl = documenturl
        parsed = urlparse(unquote(documenturl))
        self.filename = parsed.path
        self.shortname = Path(parsed.path).name
        self.filepath = str(Path(parsed.path).parent)

    def get_filename(self):
        return self.filename

    def get_filepath(self):
        return self.filepath

    def get_shortname(self):
        return self.shortname

    def set_shortname(self, shortname):
        self.shortname = shortname
        self.update_documenturl()

    def update_documenturl(self):
        self.documenturl = Path(self.filepath, self.shortname).as_uri() 

class EditorApp(Gtk.ScrolledWindow):

    def __init__(self, mindedappwin, file):

        self.mindedappwin = mindedappwin

        # look for settings
        srcdir = Path(__file__).parents[1]
        logger.debug('SettingsDir: %s' % srcdir)
        if Path(srcdir, 'data').exists():
            # this for developping only
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

        Gtk.ScrolledWindow.__init__(self)
        self.set_hexpand(True)
        self.set_vexpand(True)

        self.lm = GtkSource.LanguageManager.new()
        self.buffer = GtkSource.Buffer()
        self.codeview = GtkSource.View().new_with_buffer(self.buffer)

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
        self.settings.bind('highlightcurrentline', self.codeview, 'highlight-current-line',
                            Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind('highlightmatchingbrackets', self.buffer, 'highlight-matching-brackets',
                            Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind('smartbackspace', self.codeview, 'smart-backspace',
                            Gio.SettingsBindFlags.DEFAULT)

        self.codeview.override_font(Pango.FontDescription(self.settings.get_string('fontname')))  # gedit like

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

        self.codeview.show()

        self.add(self.codeview)
        self.show()

        self.document = MindEdDocument(file)
        #self.custom_completion_provider = None
        self.load_file(self.document.get_url())

    def load_file(self, infile):
        # load into GtkSourceBuffer as GtkSource.File
        afile = GtkSource.File()
        afile.set_location(Gio.File.new_for_uri(infile))
        try:
            loader = GtkSource.FileLoader.new(self.codeview.get_buffer(), afile)
            loader.load_async(1, None, None, None, self.file_load_finish, infile)
        except GObject.GError as e:
            logger.warn("Error: " + e.message)

    def file_load_finish(self, source, result, file):
        success = False
        try:
            success = source.load_finish(result)

        except GObject.GError as e:
            # happens on new file, if not exists
            logger.warn(e.message)

        if success:
            self.this_lang = self.lm.guess_language(file, None)

            if self.this_lang:
                self.buffer.set_highlight_syntax(True)
                self.buffer.set_language(self.this_lang)
                logger.debug("LanguageManager: %s" % self.this_lang.get_name())
            else:
                logger.warn('No language found for file "%s"' % file)
                self.buffer.set_highlight_syntax(False)
                
            logger.debug("file %s loaded %s" % (file, success))

            if SIMPLE_COMPLETE:
                new_lst = []
                for func in nxc_funcs.nxc_funcs:
                    new_lst[len(new_lst):] = [func[0]]
                keywords = ' '.join(new_lst)

                self.keybuff = GtkSource.Buffer()
                self.keybuff.begin_not_undoable_action()
                self.keybuff.set_text(keywords)
                self.keybuff.end_not_undoable_action()
                self.view_keyword_complete = GtkSource.CompletionWords.new('keyword')
                self.view_keyword_complete.register(self.keybuff)
            else:
                self.custom_completion_provider = BrickCompletionProvider(self.this_lang)

            if SIMPLE_COMPLETE:
                self.codeview_completion = self.codeview.get_completion()
                self.codeview_completion.add_provider(self.view_keyword_complete)
                self.codeview_completion.set_property("accelerators", 0)
                self.codeview_completion.set_property("show-headers", 0)
            else:
                self.codeview_completion = self.codeview.get_completion()
                self.codeview_completion.add_provider(self.custom_completion_provider)

        else:
            logger.debug("Could not load %s" % file)

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
        if self.is_opening_paren(ch):
            logger.debug('opening_paren %s', ch)
            if self.should_auto_close_paren(doc):
                handled = self.auto_close_paren(doc, ch)

        if not handled and event.keyval == Gdk.KEY_Return:
            iter1 = doc.get_iter_at_mark(doc.get_insert())
            rb = iter1.get_char()
            iter1.backward_char()
            lb = iter1.get_char()
            if lb == '{' and rb == '}':
                logger.debug('Insert new line and indent %s',view.get_tab_width())
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
        return handled

    def to_char(self, keyval_or_char):
        """Convert a event keyval or character to a character"""
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
        logger.debug('autoclosed by %s', closing_paren)
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
        logger.debug('opening %s', self.opening_parens)
        logger.debug('closing %s', self.closing_parens)
    # end bracket completion
