# -*- coding: utf-8 -*-

from pathlib import Path
from gettext import gettext as _
import re
import logging

import gi
from gi.repository import Gio
gi.require_version('GtkSource', '3.0')
from gi.repository import GtkSource

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
            LOGGER.debug('file_uri is type {}'.format(type(file_uri)))

        self.gio_file = Gio.File.new_for_uri(file_uri)
        self.set_location(self.gio_file)
        LOGGER.debug('Location: {}'.format(self.gio_file.get_parse_name()))

    def get_uri(self):
        '''file:///path/to/the/file.ext'''
        LOGGER.debug('get_uri is type {}'.format(type(self.gio_file.get_uri())))
        return self.gio_file.get_uri()

    def set_uri(self, documenturi):
        '''new uri eg save as
           str documenturi
        '''
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
            LOGGER.debug('valid: {}'.format(newname))
            return (1, (None, None))
        else:
            err_msg = _('Filename {} unvalid!').format(newname)
            hint_msg = _('Filename contains non-alphanumeric characters.')
            return (0, (err_msg, hint_msg))

