#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
BrickCompletionProvider of MindEd
'''

# Copyright (C) 2017 Bernd Sellentin <sel@gge-em.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import logging
from typing import List

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import Gtk, Gio, GObject, Pango
gi.require_version('GtkSource', '3.0')
from gi.repository import GtkSource

import minded.nxc_funcs as nxc_funcs
import minded.evc_funcs as evc_funcs
from minded.minded_utils import create_tags, convert_markup_to_tags

logger = logging.getLogger(__name__)


class BrickCompletionProvider(GObject.GObject, GtkSource.CompletionProvider):

    def __init__(self, parent, language):
        super(BrickCompletionProvider, self).__init__()

        self.funcs = []  # type: List[List[str]]
        self.consts = []  # type: List[List[str]]
        self.lang = ''
        self.info_widget = None
        self.parent = parent

        if language:
            logger.debug('Completion for language: {}'.format(language.get_name()))
            self.set_completion_list(language)
        else:
            logger.debug('No language - no completion')

    def set_completion_list(self, language):
        if language.get_name() == 'NXC':
            self.funcs = nxc_funcs.NXC_FUNCS
            self.consts = nxc_funcs.NXC_CONSTS
            self.lang = 'NXC'
        elif language.get_name() == 'EVC':
            self.funcs = evc_funcs.EVC_FUNCS
            self.consts = evc_funcs.EVC_CONSTS
            self.lang = 'EVC'
        else:
            self.funcs = []
            self.consts = []
            self.lang = ''

    def do_get_name(self):
        return '{}'.format(self.lang)

    def do_match(self, context):
        return True

    def do_populate(self, context):

        proposals = []

        # found difference in Gtk Versions
        end_iter = context.get_iter()
        if not isinstance(end_iter, Gtk.TextIter):
            _, end_iter = context.get_iter()

        if end_iter:
            buf = end_iter.get_buffer()
            mov_iter = end_iter.copy()

            if mov_iter.backward_word_start():
                start_iter = mov_iter.copy()
                left_text = buf.get_text(start_iter, end_iter, True)
                #print left_text
            else:
                left_text = ''

            if len(left_text) > 1:
                for func in self.funcs:
                    if func[0].startswith(left_text):
                        proposals.append(GtkSource.CompletionItem.new(
                            func[0], func[1], None, func[2]))
                for const in self.consts:
                    if const[0].startswith(left_text):
                        proposals.append(GtkSource.CompletionItem.new(
                            const[0], const[1], None, None))
                context.add_proposals(self, proposals, True)

    def do_activate_proposal(self, completion_item, text_iter):
        logger.debug('activate_proposal: {}'.format(completion_item.get_text()))
        buf = text_iter.get_buffer()

        buf.begin_user_action()
        end_iter = text_iter.copy()
        if text_iter.backward_word_start():
            start_iter = text_iter.copy()
            buf.delete(start_iter, end_iter)
        buf.insert_at_cursor(completion_item.get_text())
        # select if there is first hint
        if completion_item.get_text().endswith(')'):
            lim_iter = buf.get_iter_at_mark(buf.get_insert())
            start_iter = lim_iter.copy()
            start_iter.backward_chars(len(completion_item.get_text()))
            start_open, end_open = start_iter.forward_search('(',
                        Gtk.TextSearchFlags.VISIBLE_ONLY, lim_iter)
            start_iter = end_open.copy()
            start_close, end_close = start_iter.forward_search(')',
                        Gtk.TextSearchFlags.VISIBLE_ONLY, lim_iter)
            if end_open.equal(start_close):
                # no hint
                pass
            else:
                # search for next ','
                match = start_iter.forward_search(',',
                            Gtk.TextSearchFlags.VISIBLE_ONLY, end_close)
                if match:
                    # more than one hint
                    match_start, match_end = match
                    buf.select_range(end_open, match_start)
                else:
                    # only one hint
                    buf.select_range(end_open, start_close)
        buf.end_user_action()

        return True

    def do_get_info_widget(self, proposal):
        if proposal.get_info():
            if not self.info_widget:

                buf = Gtk.TextBuffer.new()
                create_tags(buf)

                view = Gtk.TextView.new_with_buffer(buf)
                view.set_editable(False)
                view.set_wrap_mode(Gtk.WrapMode.WORD)

                tabs = Pango.TabArray.new(4, True)
                tabs.set_tab(0, Pango.TabAlign.LEFT, 15)
                tabs.set_tab(1, Pango.TabAlign.LEFT, 95)
                tabs.set_tab(2, Pango.TabAlign.LEFT, 200)
                tabs.set_tab(3, Pango.TabAlign.LEFT, 280)
                view.set_tabs(tabs)

                sw = Gtk.ScrolledWindow()
                sw.add(view)
                sw.show_all()
                # Fixed size
                sw.set_size_request(400, 220)

                self.info_widget = sw
                # TODO if this will not work -> remove self.parent
                #self.info_widget = GtkSource.CompletionInfo.new()
                #self.info_widget.add(sw)
                #self.info_widget.set_attached_to (self.parent);

            return self.info_widget

    def do_update_info(self, proposal, info):
        if self.info_widget:
            #logger.debug('update {}'.format(info.get_child().get_child()))
            buf = info.get_child().get_child().get_buffer()
            if proposal.get_info():
                buf.set_text(proposal.get_info())
                convert_markup_to_tags(buf)
            else:
                buf.set_text('')
    
    def do_get_activation(self):
        #return GtkSource.CompletionActivation.USER_REQUESTED
        return GtkSource.CompletionActivation.INTERACTIVE
