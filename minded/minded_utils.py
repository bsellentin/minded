#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gio, Pango

def convert_markup_to_tags(buffer):
    '''convert Pango Markup to Gtk.TextTag'''
    #start = buffer.get_iter_at_offset(0)
    #end = buf.get_end_iter()
    (start, end) = buffer.get_bounds()
    buffer.apply_tag_by_name('text', start, end)
    for tag in ['<b>', '<span foreground="brown">', '<span foreground="red">']:
        convert_tags(buffer, tag, start)
    for tag in ['<b>', '</b>',
                '<span foreground="brown">',
                '<span foreground="green">',
                '<span foreground="red">', '</span>']:
        delete_tags(buffer, tag)
    # first line
    start = buffer.get_iter_at_offset(0)
    end = start.copy()
    if end.forward_to_line_end():
        buffer.apply_tag_by_name('title', start, end)

    example_code(buffer)

def convert_tags(buffer, tag, start):
    ''' convert html tags to pango tags '''
    end = buffer.get_end_iter()
    match = start.forward_search(tag, 0, end)
    if match is not None:
        match_start, match_end = match
        (close_tag, tag_end) = match_end.forward_search('<', 0, end)
        if tag == '<b>':
            buffer.apply_tag_by_name('bold', match_end, close_tag)
        elif 'brown' in tag:
            buffer.apply_tag_by_name('param', match_end, close_tag)
        elif 'red' in tag:
            buffer.apply_tag_by_name('warn', match_end, close_tag)
        convert_tags(buffer, tag, tag_end)

def create_tags(buffer):
    '''create TagTable for buffer'''
    buffer.create_tag('title', font='Mono 12')
    buffer.create_tag('text',
                      font=Gio.Settings('org.gnome.desktop.interface').get_string('font-name'))
    buffer.create_tag('param', foreground='Brown')
    buffer.create_tag('bold', weight=Pango.Weight.BOLD)
    buffer.create_tag('mono',
                      font=Gio.Settings('org.gnome.desktop.interface').get_string('monospace-font-name'))
    buffer.create_tag('warn', foreground='Red')

def delete_tags(buffer, tag):
    ''' delete html tags from visible text'''
    (start, end) = buffer.get_bounds()
    match = start.forward_search(tag, 0, end)
    if match is not None:
        match_start, match_end = match
        buffer.delete(match_start, match_end)
        delete_tags(buffer, tag)

def example_code(buffer):
    ''' format code examples different'''
    (start, end) = buffer.get_bounds()
    match = start.forward_search('Example:', 0, end)
    if match is not None:
        match_start, match_end = match
        buffer.apply_tag_by_name('mono', match_end, end)
