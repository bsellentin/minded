# -*- coding: utf-8 -*-

'''
Widgets used for MindEd
'''

from gettext import gettext as _
import logging
import platform

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

LOGGER = logging.getLogger(__name__)

if platform.system() == 'Windows':
    NEWLINE_TYPE_DEFAULT = 'windows'
else:
    NEWLINE_TYPE_DEFAULT = 'linux'

class MindedTabLabel(Gtk.Bin):
    '''
    Create TabLabel for Notebook with close-button
    '''
    def __init__(self, parent, editor):

        Gtk.Bin.__init__(self)
        builder = Gtk.Builder()
        builder.add_from_resource('/org/gge-em/MindEd/minded-tab-label.ui')
        self.add(builder.get_object('tablabel'))
        self.label = builder.get_object('label')
        self.label.set_text(editor.document.get_basename())
        close_button = builder.get_object('close_button')
        close_button.connect('clicked', parent.on_btn_close_tab_clicked, editor)
        self.show_all()

    def set_text(self, text):
        self.label.set_text(text)

class ErrorDialog(Gtk.MessageDialog):
    '''
    Message dialog with hints what and why something went wrong
    '''
    def __init__(self, parent, what, why):

        Gtk.MessageDialog.__init__(self, transient_for=parent,
                                   modal=True,
                                   message_type=Gtk.MessageType.INFO,
                                   buttons=Gtk.ButtonsType.OK,
                                   text=what)
        self.format_secondary_text(why)

        self.run()
        self.destroy()

class FileOpenDialog(Gtk.FileChooserDialog):
    '''
    File open dialog with filter for brick-files
    '''
    def __init__(self, parent, path):

        Gtk.FileChooserDialog.__init__(self, _('Please choose a file'), parent,
                                       Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_OPEN, Gtk.ResponseType.ACCEPT))

        # Set the current folder
        #path = document.get_parent()
        self.set_current_folder(path)

        self.set_local_only(False)

        filter_brickc = Gtk.FileFilter()
        filter_brickc.set_name(_('Brick files'))
        filter_brickc.add_pattern('*.evc')
        filter_brickc.add_pattern('*.nxc')
        self.add_filter(filter_brickc)

        filter_any = Gtk.FileFilter()
        filter_any.set_name(_('Any files'))
        filter_any.add_pattern('*')
        self.add_filter(filter_any)

class FileSaveDialog(Gtk.FileChooserDialog):
    '''
    File save dialog with choice for newline-type
    '''
    def __init__(self, parent, document):

        Gtk.FileChooserDialog.__init__(self, _('Pick a file'), parent,
                                       Gtk.FileChooserAction.SAVE,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                       Gtk.STOCK_SAVE, Gtk.ResponseType.ACCEPT))

        self.set_do_overwrite_confirmation(True)
        self.set_local_only(False)

        self.create_extra_widget()
        # requires Gtk >= 3.22
        #self.add_choice('newline_type', ),
        #    ['linux', 'mac', 'windows'],
        #    ['Unix/Linux', 'Mac OS', 'Windows'])
        #self.set_choice('newline_type', 'windows')

        try:
            self.set_uri(document.get_uri())
        except GObject.GError as e:
            LOGGER.error('# Error: {}'.format(e.message))

    def get_choice(self, choice_type):
        '''
        return newline_type (and character encoding)
        '''
        if choice_type == 'newline_type':
            newline_type = self.store[self.combo.get_active_iter()][0]
            return newline_type

    def create_newline_combo(self, extra_widget):
        '''
        create newline_type_combobox
        '''
        newline_types = [
            ['linux', 'Unix/Linux'],
            ['mac', 'Mac OS'],
            ['windows', 'Windows']
        ]
        self.store = Gtk.ListStore(str, str)
        for newline_type in newline_types:
            nl_iter = self.store.append(newline_type)
            if newline_type[0] == NEWLINE_TYPE_DEFAULT:
                default_iter = nl_iter

        self.combo = Gtk.ComboBox().new_with_model(self.store)
        renderer = Gtk.CellRendererText.new()
        self.combo.pack_start(renderer, True)
        self.combo.add_attribute(renderer, 'text', 1)
        self.combo.set_active_iter(default_iter)

        label = Gtk.Label(_('Line Ending'))

        extra_widget.pack_start(label, True, True, 0)
        extra_widget.pack_start(self.combo, True, True, 0)

    def create_extra_widget(self):
        '''
        create box for newline_type (and character encodig)_combo
        '''
        extra_widget = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

        self.create_newline_combo(extra_widget)

        extra_widget.show_all()
        self.set_extra_widget(extra_widget)


class CloseConfirmationDialog(Gtk.MessageDialog):
    '''
    confirm closing if unsaved changes
    '''
    def __init__(self, parent, filename):

        Gtk.MessageDialog.__init__(self, parent, 0, Gtk.MessageType.WARNING,
                                   Gtk.ButtonsType.NONE,
                                   _('Save changes to document {} before closing?').format(filename))

        self.add_buttons(_('Close without Saving'), Gtk.ResponseType.NO,
                         _('Cancel'), Gtk.ResponseType.CANCEL,
                         _('Save'), Gtk.ResponseType.YES)

        self.format_secondary_text(_('Changes to document {} will be permanently lost.')
                                   .format(filename))
        self.set_default_response(Gtk.ResponseType.YES)
        self.set_modal(True)
        #LOGGER.debug('parent {}'.format(parent))
