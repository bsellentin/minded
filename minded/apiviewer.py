#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango

import logging
logger = logging.getLogger(__name__)

#import evc_funcs
#import nxc_funcs
import minded.nxc_funcs as nxc_funcs
import minded.evc_funcs as evc_funcs

class ApiViewer(object):

    def __init__(self, application, *args, **kwargs):

        self.window = Gtk.Window(title = "API Viewer")
        self.window.set_application(application)
        self.window.set_default_size(800,480)
        self.window.set_border_width(6)

        hpaned = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)
        hpaned.set_position(280)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                       homogeneous=False,
                       spacing=0)
        hpaned.add1(vbox)

        # perhaps overkill, alternative: 2 buttons populate one store
        stack = Gtk.Stack()
        scrollable_evclist = Gtk.ScrolledWindow()
        stack.add_titled(scrollable_evclist, 'evc', 'EVC')

        scrollable_nxclist = Gtk.ScrolledWindow()
        stack.add_titled(scrollable_nxclist, 'nxc', 'NXC')

        stack_switcher = Gtk.StackSwitcher(homogeneous=True)
        stack_switcher.set_stack(stack)

        vbox.pack_start(stack_switcher, False, False, 0)
        vbox.pack_start(stack, True, True, 0)

        self.scrollable_textview = Gtk.ScrolledWindow()
        hpaned.add2(self.scrollable_textview)
        self.window.add(hpaned)

        # buid tree view for EVC
        evcstore = Gtk.TreeStore(str)
        self.populate_store(evcstore, 'evc')

        evcview = Gtk.TreeView.new_with_model(evcstore)
        evcrenderer = Gtk.CellRendererText()
        evccolumn = Gtk.TreeViewColumn('EVC functions', evcrenderer, text=0)
        evcview.append_column(evccolumn)
        evcselect = evcview.get_selection()
        evcselect.connect('changed', self.on_tree_selection_changed, 'evc')

        scrollable_evclist.add(evcview)

        # buid tree view for NXC
        nxcstore = Gtk.TreeStore(str)
        self.populate_store(nxcstore, 'nxc')

        nxcview = Gtk.TreeView.new_with_model(nxcstore)
        nxcrenderer = Gtk.CellRendererText()
        nxccolumn = Gtk.TreeViewColumn('NXC functions', nxcrenderer, text=0)
        nxcview.append_column(nxccolumn)
        nxcselect = nxcview.get_selection()
        nxcselect.connect('changed', self.on_tree_selection_changed, 'nxc')

        scrollable_nxclist.add(nxcview)

        info_view = Gtk.TextView()
        info_view.set_editable(False)
        info_view.set_cursor_visible(False)
        info_view.set_pixels_above_lines(2)
        info_view.set_pixels_below_lines(2)
        info_view.set_left_margin(10)

        self.info_buffer = info_view.get_buffer()
        self.info_buffer.create_tag('title', font='Mono 12')
        self.info_buffer.create_tag('text', font='Mono 10')
        self.info_buffer.create_tag('param', foreground='Brown')
        self.info_buffer.create_tag('bold', weight=Pango.Weight.BOLD)
        self.info_buffer.create_tag('mono', font='Courier 11')
        self.info_buffer.create_tag('warn', foreground='Red')
        self.scrollable_textview.add(info_view)

        self.window.show_all()
        self.window.connect('delete-event', self.quit)

    def populate_store(self, store, lang):
        categories = []
        if lang == 'evc':
            functions = evc_funcs.evc_funcs
        elif lang == 'nxc':
            functions = nxc_funcs.nxc_funcs

        for cat in [func[3] for func in functions]:
            if cat not in categories:
                categories.append(cat)
        logger.debug(categories)

        for cat in categories:
            iter = store.append(None)
            store.set(iter, 0, cat)

            for func in [func[0] for func in functions if func[3] == cat]:
                child_iter = store.append(iter)
                store.set(child_iter, 0, func)

    def on_tree_selection_changed(self, selection, lang):
        if lang == 'evc':
            functions = evc_funcs.evc_funcs
        elif lang == 'nxc':
            functions = nxc_funcs.nxc_funcs

        model, treeiter = selection.get_selected()
        if treeiter != None:
            logger.debug('you selected {}'.format(model[treeiter][0]))
            for func in functions:
                if func[0] == model[treeiter][0] and len(func[2]) != 0:

                    self.info_buffer.set_text(func[2])
                    # doesn't exist: text_buffer.set_markup
                    # have to do it ourself
                    # format first line
                    start = self.info_buffer.get_iter_at_offset(0)
                    end = start.copy()
                    if end.forward_to_line_end():
                        self.info_buffer.apply_tag_by_name('title', start, end)
                    for search in ['<b>', '</b>']:
                        start = self.info_buffer.get_iter_at_offset(0)
                        end = start.copy()
                        if end.forward_to_line_end():
                            match_start, match_end = start.forward_search(search,
                                                                   Gtk.TextSearchFlags.VISIBLE_ONLY,
                                                                   end)
                            self.info_buffer.delete(match_start, match_end)
                     # format text
                    start = self.info_buffer.get_start_iter()
                    text_start = start.copy()
                    end = self.info_buffer.get_end_iter()
                    if text_start.forward_visible_line():
                        self.info_buffer.apply_tag_by_name('text', text_start, end)
                    for tag in ['<b>', '<span foreground="brown">', '<span foreground="red">']:
                        self.convert_tags(tag, start)
                    for tag in ['<b>', '</b>', 
                                '<span foreground="brown">',
                                '<span foreground="green">',
                                '<span foreground="red">', '</span>']:
                        self.delete_tags(tag)
                    # format example
                    self.example_code()
                    break

    def convert_tags(self, tag, start):
        ''' convert html tags to pango tags '''
        end = self.info_buffer.get_end_iter()
        match = start.forward_search(tag, 0, end)

        if match != None:
            match_start, match_end = match
            tag_end = match_end.copy()
            if tag_end.forward_visible_word_end():
                if tag == '<b>':
                    self.info_buffer.apply_tag_by_name('bold', match_end, tag_end)
                elif 'brown' in tag:
                    self.info_buffer.apply_tag_by_name('param', match_end, tag_end)
                elif 'red' in tag:
                    self.info_buffer.apply_tag_by_name('warn', match_end, tag_end)
            self.convert_tags(tag, tag_end)

    def delete_tags(self, tag):
        ''' delete html tags from visible text'''
        (start, end) = self.info_buffer.get_bounds()
        match = start.forward_search(tag, 0, end)
        if match != None:
            match_start, match_end = match
            self.info_buffer.delete(match_start, match_end)
            self.delete_tags(tag)

    def example_code(self):
        ''' format code examples different'''
        (start, end) = self.info_buffer.get_bounds()
        match = start.forward_search('Example:', 0, end)
        if match != None:
            match_start, match_end = match
            self.info_buffer.apply_tag_by_name('mono', match_end, end)

    def print_tree_store(store):
        rootiter = store.get_iter_first()
        print_rows(store, rootiter, '')

    def print_rows(store, treeiter, indent):
        while treeiter != None:
            logger.debug(indent + str(store[treeiter][:]))
            if store.iter_has_child(treeiter):
                childiter = store.iter_children(treeiter)
                print_rows(store, childiter, indent + '\t')
            treeiter = store.iter_next(treeiter)

    def quit(self, *args):
        'Quit the program'
        self.window.destroy()
        #Gtk.main_quit()
        # needed! Else Window disappears, but App lives still.
        return True


