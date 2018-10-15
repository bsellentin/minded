#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
BrickCompletionProvider of MindEd
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

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import Gtk, GObject
gi.require_version('GtkSource', '3.0')
from gi.repository import GtkSource

import minded.nxc_funcs as nxc_funcs
import minded.evc_funcs as evc_funcs

logger = logging.getLogger(__name__)


class BrickCompletionProvider(GObject.GObject, GtkSource.CompletionProvider):

    def __init__(self, language):
        GObject.GObject.__init__(self)

        if language:
            logger.debug('Completion for language: {}'.format(language.get_name()))
            self.set_completion_list(language)
        else:
            logger.debug('No language - no completion')
            self.funcs = []
            self.consts = []
            self.lang = ''

    def set_completion_list(self, language):
        if language.get_name() == 'NXC':
            self.funcs = nxc_funcs.NXC_FUNCS
            self.consts = nxc_funcs.NXC_CONSTS
            self.lang = 'NXC'
        elif language.get_name() == 'EVC':
            self.funcs = evc_funcs.evc_funcs
            self.consts = evc_funcs.evc_consts
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
                            func[0], func[1], None, '<small>'+func[2]+'</small>'))
                for const in self.consts:
                    if const[0].startswith(left_text):
                        proposals.append(GtkSource.CompletionItem.new(
                            const[0], const[1], None, None))
                context.add_proposals(self, proposals, True)
            return

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
