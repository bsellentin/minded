#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
from gi.repository import Gtk, Gdk, Gio, GObject, Pango
gi.require_version('GtkSource', '3.0')
from gi.repository import GtkSource

import logging
logger = logging.getLogger(__name__)

import minded.nxc_funcs as nxc_funcs
import minded.evc_funcs as evc_funcs


class NXCCompletionProvider(GObject.GObject, GtkSource.CompletionProvider):

    def __init__(self, language):
        GObject.GObject.__init__(self)
        
        if language:
            logger.debug('Completion for language: %s', language.get_name())
            if language.get_name() == 'NXC':
                self.funcs = nxc_funcs.nxc_funcs
                self.lang = 'NXC'
            if language.get_name() == 'EVC':
                self.funcs = evc_funcs.evc_funcs
                self.lang = 'EVC'
        else:
            logger.debug('No language - no completion')
            self.funcs = []
            self.lang = ''   
            
    def do_get_name(self):
        return ('%s-Functions' % self.lang)

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

                context.add_proposals(self, proposals, True)
            return
    
    def do_activate_proposal(self, completion_item, text_iter):
        logger.debug('activate_proposal: %s', completion_item.get_text())
        buf = text_iter.get_buffer()
                
        buf.begin_user_action()
        end_iter = text_iter.copy()
        if text_iter.backward_word_start():
            start_iter = text_iter.copy()
            buf.delete(start_iter, end_iter)
        buf.insert_at_cursor(completion_item.get_text())
       
        ins_iter = buf.get_iter_at_mark(buf.get_insert())
        lim_iter = ins_iter.copy()
        if lim_iter.backward_word_start():
            start_iter = lim_iter.copy()
            match_start, match_end = ins_iter.backward_search('(', Gtk.TextSearchFlags.VISIBLE_ONLY, start_iter)
            match_start.forward_char()
            buf.place_cursor(match_start)
        buf.end_user_action()
        
        return True

