#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Browse the NXC- and EVC-API reference
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

import logging
from typing import List

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Gio, Pango

import minded.nxc_funcs as nxc_funcs
import minded.evc_funcs as evc_funcs
from minded.minded_utils import create_tags, convert_markup_to_tags

LOGGER = logging.getLogger(__name__)

CSS = b'''
        #displayer {
            background-image: none;
            background-color: white;
        }
    '''


class ApiViewer():
    '''A window with a Treeview to select item and a Textview to see
    details ( function call, parameters, return, example) for this item.
    '''

    def __init__(self, application):
        '''A new API-viewer window'''

        builder = Gtk.Builder()
        builder.add_from_resource('/org/gge-em/MindEd/minded-apiviewer.ui')
        builder.connect_signals(self)

        self.window = builder.get_object('window')
        self.window.set_application(application)

        nxcstore = builder.get_object('nxcstore')
        self.populate_store(nxcstore, 'nxc')

        evcstore = builder.get_object('evcstore')
        self.populate_store(evcstore, 'evc')

        evcselect = builder.get_object('evcselect')
        evcselect.connect('changed', self.on_tree_selection_changed, 'evc')
        nxcselect = builder.get_object('nxcselect')
        nxcselect.connect('changed', self.on_tree_selection_changed, 'nxc')

        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(CSS)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        stack = builder.get_object('stack')
        stack.set_visible_child_name('nxc')

        self.title_label = builder.get_object('title_label')
        self.title_label.set_markup("<big>NXC Programmers's Guide</big>")

        info_view = builder.get_object('info_view')
        info_view.set_wrap_mode(Gtk.WrapMode.WORD)

        tabs = Pango.TabArray.new(3, True)
        tabs.set_tab(0, Pango.TabAlign.LEFT, 15)
        tabs.set_tab(1, Pango.TabAlign.LEFT, 95)
        tabs.set_tab(2, Pango.TabAlign.LEFT, 290)
        info_view.set_tabs(tabs)

        self.info_buffer = info_view.get_buffer()
        create_tags(self.info_buffer)

        self.window.show_all()
        self.window.connect('delete-event', self.quit)

    def populate_store(self, store, lang: str):
        '''read functions into store
        :param store: a Gtk.TreeStore
        :param lang: str programming language
        '''
        categories = []  # type: List[str]
        if lang == 'evc':
            functions = evc_funcs.EVC_FUNCS
        elif lang == 'nxc':
            functions = nxc_funcs.NXC_FUNCS

        for cat in [func[3] for func in functions]:
            if cat not in categories:
                categories.append(cat)
        LOGGER.debug(categories)

        for cat in categories:
            parent_iter = store.append(None)
            store.set(parent_iter, 0, cat)

            for func in [func[0] for func in functions if func[3] == cat]:
                child_iter = store.append(parent_iter)
                store.set(child_iter, 0, func)

    def on_child_change(self, stack, visible_child):  #pylint: disable=unused-argument
        '''Changes shown programming language in Gtk.Stack'''
        LOGGER.debug('visible-child: {}'.format(stack.get_visible_child_name()))

        if stack.get_visible_child_name() == 'nxc':
            self.title_label.set_markup("<big>NXC Programmers's Guide</big>")
        elif stack.get_visible_child_name() == 'evc':
            self.title_label.set_markup("<big>EVC Programmers's Guide</big>")
        self.info_buffer.set_text('')

    def on_row_activated(self, treeview, treepath, treecolumn):  #pylint: disable=unused-argument
        '''single-click or ENTER-key on TreeView expands or
        collapses child-nodes
        '''
        LOGGER.debug('row activated {}, depth {}'.format(treepath, treepath.get_depth()))
        if treepath.get_depth() == 1:
            LOGGER.debug('Top Element, expanded {}'.format(treeview.row_expanded(treepath)))
            if treeview.row_expanded(treepath):
                treeview.collapse_row(treepath)
            else:
                treeview.expand_row(treepath, True)

    def on_tree_selection_changed(self, selection, lang):
        '''show for selected child-node the details in TextView'''
        if lang == 'evc':
            functions = evc_funcs.EVC_FUNCS
        elif lang == 'nxc':
            functions = nxc_funcs.NXC_FUNCS

        model, treeiter = selection.get_selected()
        if treeiter is not None:
            LOGGER.debug('you selected {}'.format(model[treeiter][0]))
            for func in functions:
                if func[0] == model[treeiter][0] and func[2]:
                    self.info_buffer.set_text(func[2])
                    convert_markup_to_tags(self.info_buffer)
                    break

    def quit(self, *args):      #pylint: disable=unused-argument
        '''Close API-viewer-window'''
        # pylint: Unused argument 'args' (unused-argument)
        # but: TypeError: quit() takes 1 positional argument but 3 were given
        self.window.destroy()
        # needed! Else Window disappears, but App lives still.
        return True
