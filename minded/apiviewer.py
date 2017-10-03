#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango

import evc_funcs

categories = ['General', 'Input', 'Output', 'Button', 'Display', 'Sound']

class ApiViewer(object):

    def __init__(self, *args, **kwargs):

        self.window = Gtk.Window(title = "API Viewer")
        #self.window.set_application(application)
        self.window.set_default_size(640,480)
        self.window.set_border_width(6)

        hpaned = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)
        hpaned.set_position(300)

        scrollable_treelist = Gtk.ScrolledWindow()
        hpaned.add1(scrollable_treelist)

        self.scrollable_textview = Gtk.ScrolledWindow()
        hpaned.add2(self.scrollable_textview)
        self.window.add(hpaned)

        store = Gtk.TreeStore(str)
        for cat in categories:
            iter = store.append(None)
            store.set(iter, 0, cat)

            for func in [func[0] for func in evc_funcs.evc_funcs if func[3] == cat]:
                child_iter = store.append(iter)
                store.set(child_iter, 0, func)

        self.treeview = Gtk.TreeView.new_with_model(store)
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn('functions', renderer, text=0)
        self.treeview.append_column(column)
        select = self.treeview.get_selection()
        select.connect('changed', self.on_tree_selection_changed)

        scrollable_treelist.add(self.treeview)

        self.info_view = Gtk.TextView()
        self.info_view.set_editable(False)
        self.info_view.set_cursor_visible(False)
        self.info_view.set_pixels_above_lines(2)
        self.info_view.set_pixels_below_lines(2)
        self.info_view.set_left_margin(10)

        self.info_buffer = self.info_view.get_buffer()
        self.info_buffer.create_tag('title', font='Mono 12')
        self.info_buffer.create_tag('text', font='Mono 10')
        self.info_buffer.create_tag('param', foreground='Brown')
        self.info_buffer.create_tag('bold', weight=Pango.Weight.BOLD)
        self.info_buffer.create_tag('mono', font='Courier 11')
        self.scrollable_textview.add(self.info_view)

        self.window.show_all()
        self.window.connect('delete-event', self.quit)

    def on_tree_selection_changed(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter != None:
            print('you selected', model[treeiter][0])
            for func in evc_funcs.evc_funcs:
                if func[0] == model[treeiter][0] and len(func[2]) != 0:

                    self.info_buffer.set_text(func[2])

                    # first line
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
                     # text
                    start = self.info_buffer.get_start_iter()
                    text_start = start.copy()
                    end = self.info_buffer.get_end_iter()
                    if text_start.forward_visible_line():
                        self.info_buffer.apply_tag_by_name('text', text_start, end)
                    for tag in ['<b>', '<span foreground="brown">']:
                        self.convert_tags(tag, start)
                    for tag in ['<b>', '</b>', '<span foreground="brown">', '</span>']:
                        self.delete_tags(tag)
                    self.example_code()
                    break

    def convert_tags(self, tag, start):
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
            self.convert_tags(tag, tag_end)

    def delete_tags(self, tag):
        (start, end) = self.info_buffer.get_bounds()
        match = start.forward_search(tag, 0, end)
        if match != None:
            match_start, match_end = match
            self.info_buffer.delete(match_start, match_end)
            self.delete_tags(tag)

    def example_code(self):
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
            print(indent + str(store[treeiter][:]))
            if store.iter_has_child(treeiter):
                childiter = store.iter_children(treeiter)
                print_rows(store, childiter, indent + '\t')
            treeiter = store.iter_next(treeiter)

        #print_tree_store(store)

    def quit(self, *args):
        'Quit the program'
        #self.window.destroy()
        Gtk.main_quit()
        # needed! Else Window disappears, but App lives still.
        #return True

win = ApiViewer()
Gtk.main()
