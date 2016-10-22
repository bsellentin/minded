#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''MindEd - An Editor for programming LEGO Mindstorms Bricks
- NXT with NXC
- EV3 with EV3-Python
'''

import os
import subprocess
# requires package python-pathlib
import pathlib
from urllib.parse import urlparse, unquote
import shlex

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GObject', '2.0')
#gi.require_version('PangoCairo', '1.0')
from gi.repository import Gtk, Gdk, Gio, GObject, Pango
gi.require_version('GtkSource', '3.0')
from gi.repository import GtkSource

# for usbListener
#gi.require_version('GUdev', '1.0')
#from gi.repository import GUdev

import nxc_funcs

DEBUGLEVEL = 1
SIMPLE_COMPLETE = 0

class MindEdAppWin(object):
    '''The Main Application Window'''

    def __init__(self, application, *args, **kwargs):
        #self.app = application
        builder = Gtk.Builder()
        GObject.type_register(GtkSource.View)
        builder.add_from_file("minded.glade")
        builder.connect_signals(self)
        self.window = builder.get_object("TopWin")
        self.window.set_application(application)

        self.notebook = builder.get_object("notebook")
        self.compilerview = builder.get_object("compilerview")
        self.menupop = builder.get_object("menumenu")
        self.btn_transmit = builder.get_object("btn_transmit")
        self.btn_transmit.set_sensitive(False)
        self.btn_save = builder.get_object("btn_save")
        self.btn_save.set_sensitive(False)
        self.btn_save_as = builder.get_object("btn_save_as")
        self.btn_save_as.set_sensitive(False)
        self.btn_print = builder.get_object("btn_print")
        self.btn_print.set_sensitive(False)
        self.brick_status = builder.get_object("brick_status")
        self.brick_status_id = self.brick_status.get_context_id("BrickStatus")
        # TODO: change label on tab change
        self.language_label = builder.get_object("language_label")
        self.languagemenu = builder.get_object("languagemenu")
        self.language_tree = builder.get_object("languagetree")
        self.language_store = Gtk.ListStore(str, str)
        self.language_store.append(["text", "Text"])
        self.language_store.append(["nxc", "NXC"])
        self.language_store.append(["python", "Python"])
        self.language_tree.set_model(self.language_store)
        self.cell = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Language", self.cell, text=1)
        self.language_tree.append_column(column)
        
        # Look for Brick
        for device in application.client.query_by_subsystem("usb"):
            if device.get_property('ID_VENDOR') == '0694' and device.get_property('ID_MODEL') == '0002':
            #if device.get_property('ID_MODEL_FROM_DATABASE') == "Mindstorms NXT":
                self.brick_status.push(self.brick_status_id, "NXT")
                self.btn_transmit.set_sensitive(True)

        self.window.show_all()

        self.untitledDocCount = 0

    def gtk_main_quit(self, *args):
        '''TopWin CloseButton clicked, are there unsaved changes'''
        # get_n_pages from 0...n-1, remove reversed!
        for pagecount in range(self.notebook.get_n_pages()-1, -1, -1):

            if DEBUGLEVEL > 0:
                print("Window close clicked! Remove page %s" % pagecount)

            editor = self.notebook.get_nth_page(pagecount)
            if editor.get_buffer().get_modified():
                self.close_confirmation_dialog(editor)
            else:
                self.notebook.remove_page(pagecount)

        if self.notebook.get_n_pages() == 0:
            self.window.destroy()
        # needed! Else Window disappears, but App lives still.
        return True

    def on_btn_new_clicked(self, button):

        if DEBUGLEVEL > 0:
            print("Button New clicked from:\n %s" % button)

        self.untitledDocCount += 1
        
        dirname = os.path.expanduser("~")
        filename = 'untitled' + str(self.untitledDocCount)
        file = os.path.join(dirname, filename)

        # make empty file to avoid error on loading
        try:
            os.mknod(file)
        except OSError:
            pass

        self.load_file_in_editor(pathlib.Path(file).as_uri())

    def on_btn_open_clicked(self, button):

        if DEBUGLEVEL > 0:
            print("Button Open clicked from:\n %s" % button)

        open_dlg = Gtk.FileChooserDialog("Please choose a file", self.window,
                                         Gtk.FileChooserAction.OPEN,
                                         (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                          Gtk.STOCK_OPEN, Gtk.ResponseType.ACCEPT))
        open_dlg.set_local_only(False)
        open_dlg.connect("response", self.open_dlg_response)
        open_dlg.show()

    def open_dlg_response(self, dialog, response):

        open_dlg = dialog
        if response == Gtk.ResponseType.ACCEPT:
            if DEBUGLEVEL > 0:
                print("OpenDialog File selected: " + dialog.get_uri())
            # check if file already open
            for pagecount in range(self.notebook.get_n_pages()-1, -1, -1):
                editor = self.notebook.get_nth_page(pagecount)
                if editor.file == open_dlg.get_uri():
                    self.notebook.set_current_page(pagecount)
                    break
            else:
                self.load_file_in_editor(open_dlg.get_uri())

        elif response == Gtk.ResponseType.CANCEL:
            if DEBUGLEVEL > 0:
                print("OpenDialog Cancel clicked")

        dialog.destroy()

    def on_btn_save_clicked(self, button):

        if DEBUGLEVEL > 0:
            print("Button Save clicked from:\n %s" % button)

        page_num = self.notebook.get_current_page()
        editor = self.notebook.get_nth_page(page_num)
        # is_untitled(widget child, bool close_tab)
        self.is_untitled(editor, 0)

    def on_btn_save_as_clicked(self, button):

        if DEBUGLEVEL > 0:
            print("Button Save as clicked from:\n %s" % button)

        if self.menupop.get_visible():
            self.menupop.hide()

        page_num = self.notebook.get_current_page()
        editor = self.notebook.get_nth_page(page_num)

        self.save_file_as(editor, 0)
        
        if DEBUGLEVEL > 0:
            print("Save as: %s" % editor.file)
            
    def on_btn_close_tab_clicked(self, button, child):

        # widget must be child of page, that is scrolledwindow
        page_num = self.notebook.page_num(child)
        editor = self.notebook.get_nth_page(page_num)
        if DEBUGLEVEL > 0:
            print("Button CloseTab clicked from:\n %s" % button)
            print("close tab %s" % page_num)

        if page_num != -1 and not editor.get_buffer().get_modified():
            self.notebook.remove_page(page_num)
            editor.destroy()
            child.destroy()
        else:
            if DEBUGLEVEL > 0:
                print("file modified, save before closing")
            self.close_confirmation_dialog(child)

    def on_btn_compile_clicked(self, button):
        '''compile the saved file - a .rxe-file results'''
        if DEBUGLEVEL > 0:
            print("Button Compile clicked from:\n %s" % button)

        page_num = self.notebook.get_current_page()
        editor = self.notebook.get_nth_page(page_num)
        if editor.get_buffer().get_modified():
            self.dlg_save_first()
        else:
            nbcfile = urlparse(unquote(editor.file))
            nbcout = os.path.splitext(nbcfile.path)[0]+".rxe"
            if DEBUGLEVEL > 0:
                print("File to compile: %s" % shlex.quote(nbcfile.path))
            nbc_opts = (' -O=%s %s' % (shlex.quote(nbcout), shlex.quote(nbcfile.path)))

            # change cursor
            watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
            self.window.get_window().set_cursor(watch_cursor)
            # don't starve the gui thread before it can change the cursor,
            # call the time consuming in an idle callback
            GObject.idle_add(self.idle_nbc_proc, self.window, nbc_opts)

    def on_btn_transmit_clicked(self, button):

        if DEBUGLEVEL > 0:
            print("Button Transmit clicked from:\n %s" % button)

        page_num = self.notebook.get_current_page()
        editor = self.notebook.get_nth_page(page_num)
        if editor.get_buffer().get_modified():
            self.dlg_save_first()
        else:
            nbcfile = urlparse(unquote(editor.file))
            nbc_opts = (' -d %s' % (shlex.quote(nbcfile.path)))

            # change cursor
            watch_cursor = Gdk.Cursor(Gdk.CursorType.WATCH)
            self.window.get_window().set_cursor(watch_cursor)
            # don't starve the gui thread before it can change the cursor,
            # call the time consuming in an idle callback
            GObject.idle_add(self.idle_nbc_proc, self.window, nbc_opts)

    def dlg_save_first(self):

        dlg = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.INFO,
                                Gtk.ButtonsType.OK, "You have to save first!")
        dlg.format_secondary_text("The compiler works on the real file.")

        dlg.run()
        dlg.destroy()

    def idle_nbc_proc(self, window, nbc_opts):

        nbc_proc = subprocess.Popen(('/usr/local/bin/nbc %s' % (nbc_opts)),
                                    shell=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)

        nbc_data = nbc_proc.communicate()
        if nbc_proc.returncode:  # Error
            self.compilerview.get_buffer().set_text(nbc_data[1].decode())
        else:  # OK
            # nur die letzten 5 Zeilen ausgeben
            msg = '\n'.join([str(i) for i in nbc_data[0].decode().split('\n')[-5:]])
            # python 2.7 only
            #msg = "\n".join(nbc_data[0].split("\n")[-5:])
            self.compilerview.get_buffer().set_text(msg)

        self.window.get_window().set_cursor(None)

    def on_btn_menu_clicked(self, button):

        if DEBUGLEVEL > 0:
            print("Button Menu clicked from:\n %s" % button)

        #Toggl
        if self.menupop.get_visible():
            self.menupop.hide()
        else:
            self.menupop.show_all()

    def on_btn_print_clicked(self, button):

        if DEBUGLEVEL > 0:
            print("Button Print clicked from:\n %s" % button)

        if self.menupop.get_visible():
            self.menupop.hide()

        page_num = self.notebook.get_current_page()
        editor = self.notebook.get_nth_page(page_num)

        printer = PrintingApp(editor)
        printer.run()

    def on_btn_about_clicked(self, button):

        if self.menupop.get_visible():
            self.menupop.hide()

        aboutdlg = Gtk.AboutDialog(transient_for=self.window, modal=True)

        authors = ["Bernd Sellentin"]
        #documenters = []

        aboutdlg.set_program_name("MindEd")
        aboutdlg.set_comments("A NXC-Editor for LEGO Mindstorms NXT-Brick")
        aboutdlg.set_authors(authors)
        aboutdlg.set_version("0.1")
        #image = GdkPixbuf.Pixbuf()
        #image.new_from_file("/home/selles/pyGtk/minded/minded.png")
        aboutdlg.set_logo_icon_name("gedit-symbolic")
        aboutdlg.set_copyright("2016")
        aboutdlg.set_website("http://sellentin.homepage.t-online.de/minded")
        aboutdlg.set_website_label("MindEd Website")

        aboutdlg.present()

    def load_file_in_editor(self, file):

        try:
            editor = EditorApp(file)
        except:
            print("Something went terrible wrong")
            
        self.create_tab_label(editor)
        self.notebook.append_page(editor, self.box)
        self.notebook.set_current_page(-1)
        
        buffer = editor.get_buffer()
        buffer.connect("modified_changed", self.on_buffer_modified)
        editor.codeview.grab_focus()

        if not self.btn_save.get_sensitive():
            self.btn_save.set_sensitive(True)
        if not self.btn_save_as.get_sensitive():
            self.btn_save_as.set_sensitive(True)
        if not self.btn_print.get_sensitive():
            self.btn_print.set_sensitive(True)

        if DEBUGLEVEL > 0:
            print("file %s loaded in buffer, modified %s" % (file, buffer.get_modified()))

    def is_untitled(self, editor, close_tab):
        """looks if file is new with default name
        called by on_btn_save_clicked
                  close_confirmation_dialog_response
                  called by gtk_main_quit
                            on_btn_close_tab
        """
        path = editor.file
        if 'untitled' in path:
            self.save_file_as(editor, close_tab)
        else:
            self.save_file(editor, close_tab)

    def save_file_as(self, editor, close_tab):

        path = editor.file

        if DEBUGLEVEL > 0:
            print("func save_file_as: %s on tab " % (path))

        # FileChooserDialog wants Gio.File
        file = Gio.File.new_for_uri(path)

        save_dialog = Gtk.FileChooserDialog("Pick a file", self.window,
                                            Gtk.FileChooserAction.SAVE,
                                            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                             Gtk.STOCK_SAVE, Gtk.ResponseType.ACCEPT))
        save_dialog.set_do_overwrite_confirmation(True)
        save_dialog.set_local_only(False)
        try:
            save_dialog.set_file(file)
        except GObject.GError as e:
            print("Error: " + e.message)

        save_dialog.connect("response", self.save_file_as_response, editor, close_tab)
        save_dialog.show()

    def save_file_as_response(self, dialog, response, editor, close_tab):

        save_dialog = dialog
        if response == Gtk.ResponseType.ACCEPT:
            editor.file = save_dialog.get_uri()
            if DEBUGLEVEL > 0:
                page_num = self.notebook.page_num(editor)
                print("func save_file_as_response: %s on tab %s, " % (editor.file, page_num))
            self.save_file(editor, close_tab)
        elif response == Gtk.ResponseType.CANCEL:
            print("cancelled: SAVE AS")
        dialog.destroy()

    def save_file(self, editor, close_tab):

        buffer = editor.get_buffer()

        # save file form GtkSourceBuffer as GtkSource.File
        file = GtkSource.File()
        file.set_location(Gio.File.new_for_uri(editor.file))
        try:
            saver = GtkSource.FileSaver.new(buffer, file)
            saver.save_async(1, None, None, None, self.on_save_finish, editor, close_tab)
        except GObject.GError as e:
            print("Error: " + e.message)

    def on_save_finish(self, source, result, editor, close_tab):
        
        try:
            success = source.save_finish(result)

            if close_tab:
                page_num = self.notebook.page_num(editor)
                if DEBUGLEVEL > 0:
                    print("remove tab %s" % page_num)
                # async saving, we have to wait for finish before removing
                self.notebook.get_nth_page(page_num).get_child().destroy()
                self.notebook.get_nth_page(page_num).destroy()
                self.notebook.remove_page(page_num)
            if DEBUGLEVEL > 0:
                print("file %s saved %s" % (editor.file, success))
        
            thisbox = self.notebook.get_tab_label(editor)
            widglist = thisbox.get_children()
            fileuri = urlparse(unquote(editor.file))
            filename = pathlib.Path(fileuri.path).name
            widglist[0].set_text(filename)
        
        except GObject.GError as e:
            print("problem saving file " + e.message)
            return

    def close_confirmation_dialog(self, editor):

        dirname, filename = os.path.split(editor.file)

        dlg = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.WARNING,
                                Gtk.ButtonsType.NONE,
                                "Save changes to document '%s' before closing?" % filename)
        dlg.add_buttons("Close without Saving", Gtk.ResponseType.NO,
                        "Cancel", Gtk.ResponseType.CANCEL,
                        "Save", Gtk.ResponseType.YES)
        dlg.format_secondary_text("Changes to document '%s' will be permanently lost." % filename)
        dlg.set_default_response(Gtk.ResponseType.YES)
        dlg.connect("response", self.close_confirmation_dialog_response, editor)
        dlg.run()

    def close_confirmation_dialog_response(self, widget, response, editor):

        if response == Gtk.ResponseType.NO:
            if DEBUGLEVEL > 0:
                print("Close tab without saving")
            # click perhaps not on current page
            page_num = self.notebook.page_num(editor)
            self.notebook.remove_page(page_num)
            editor.destroy()

        elif response == Gtk.ResponseType.CANCEL:
            if DEBUGLEVEL > 0:
                print("Cancel closing tab")

        elif response == Gtk.ResponseType.YES:
            if DEBUGLEVEL > 0:
                print("Save file before closing")
            
            close_tab = 1
            self.is_untitled(editor, close_tab)

        # if the messagedialog is destroyed (by pressing ESC)
        elif response == Gtk.ResponseType.DELETE_EVENT:
            print("dialog closed or cancelled")
        # finally, destroy the messagedialog
        widget.destroy()

    def create_tab_label(self, editor):

        # create tab header with close button
        self.box = Gtk.HBox()
        closebtn = Gtk.Button()
        icon = Gio.ThemedIcon(name="window-close")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        closebtn.set_image(image)
        closebtn.set_relief(Gtk.ReliefStyle.NONE)
        closebtn.connect("clicked", self.on_btn_close_tab_clicked, editor)

        fileuri = urlparse(unquote(editor.file))
        filename = pathlib.Path(fileuri.path).name

        self.box.pack_start(Gtk.Label(filename), True, True, 0)
        self.box.pack_end(closebtn, False, False, 0)
        self.box.show_all()

    def on_buffer_modified(self, widget):

        page_num = self.notebook.get_current_page()
        editor = self.notebook.get_nth_page(page_num)
        
        if DEBUGLEVEL > 0:
            print("modified tab %s %s" % (page_num, editor.get_buffer().get_modified()))
        
        thisbox = self.notebook.get_tab_label(self.notebook.get_nth_page(page_num))
        widglist = thisbox.get_children()
        
        filename = widglist[0].get_text()
        if editor.get_buffer().get_modified(): 
            filename = "*"+filename
        else:
            filename = filename[1:]
        widglist[0].set_text(filename)

    def on_language_button_clicked(self, button):

        if DEBUGLEVEL > 0:
            print("Button Language clicked from:\n %s" % button)

        #Toggl
        if self.languagemenu.get_visible():
            self.languagemenu.hide()
        else:
            self.languagemenu.show_all()
            
    def on_languageselect_changed(self, selection):

        model, treeiter = selection.get_selected()
        if treeiter != None:
            if DEBUGLEVEL > 0:
                print("Language selected", model[treeiter][0])
            
            self.language_label.set_text(model[treeiter][1])
            
            page_num = self.notebook.get_current_page()
            editor = self.notebook.get_nth_page(page_num)
            nxc_lang = editor.lm.get_language(model[treeiter][0])
            buffer = editor.get_buffer()
            if nxc_lang:
                if not buffer.get_highlight_syntax():
                    buffer.set_highlight_syntax(True)
                buffer.set_language(nxc_lang)
            else:
                if buffer.get_highlight_syntax():
                    buffer.set_highlight_syntax(False)
                buffer.set_language(None)
            
            self.languagemenu.hide()

    def on_notebook_switch_page(self, notebook, page, page_num):
        #print(page_num)
        editor = self.notebook.get_nth_page(page_num)
        buffer = editor.get_buffer()
        if buffer.get_language():
            self.language_label.set_text(buffer.get_language().get_name())
        else:    
            self.language_label.set_text('Text')    

    def on_btn_nxtinfo_clicked(self, button):
        '''new window with brick information like name, firmware...'''
        import nxtinfo
        if self.menupop.get_visible():
            self.menupop.hide()
        self.nxt_info = nxtinfo.NXTInfo(self.window.get_application())

    def on_btn_nxtfiler_clicked(self, button):
        '''new window with brick information like name, firmware...'''
        import nxtfiler
        if self.menupop.get_visible():
            self.menupop.hide()
        self.nxt_filer = nxtfiler.NXT_Filer(self.window.get_application())
        
class EditorApp(Gtk.ScrolledWindow):
    
    def __init__(self, file):
        
        Gtk.ScrolledWindow.__init__(self)
        self.set_hexpand(True)
        self.set_vexpand(True)

        self.lm = GtkSource.LanguageManager.new()
        self.nxc_lang = self.lm.guess_language(file, None)
        #if self.nxc_lang:
        #    self.language_label.set_text(self.nxc_lang.get_name())
        #else:
        #    self.language_label.set_text('Text')
        
        #if DEBUGLEVEL > 0:
        #    print language.get_name()

        self.buffer = GtkSource.Buffer()
        if self.nxc_lang:
            self.buffer.set_highlight_syntax(True)
            self.buffer.set_language(self.nxc_lang)
        else:
            print('No language found for file "%s"' % file)
            self.buffer.set_highlight_syntax(False)

        self.codeview = GtkSource.View().new_with_buffer(self.buffer)

        self.codeview.set_show_line_numbers(True)
        self.codeview.set_auto_indent(True)
        self.codeview.modify_font(Pango.FontDescription("Monospace 12"))

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

            self.custom_completion_provider = CustomCompletionProvider()

        if SIMPLE_COMPLETE:
            self.codeview_completion = self.codeview.get_completion()
            self.codeview_completion.add_provider(self.view_keyword_complete)
            self.codeview_completion.set_property("accelerators", 0)
            self.codeview_completion.set_property("show-headers", 0)
        else:
            self.codeview_completion = self.codeview.get_completion()
            self.codeview_completion.add_provider(self.custom_completion_provider)

        self.file = file
        self.codeview.show()

        self.add(self.codeview)
        self.show()

        # load into GtkSourceBuffer as GtkSource.File
        afile = GtkSource.File()
        afile.set_location(Gio.File.new_for_uri(self.file))
        try:
            loader = GtkSource.FileLoader.new(self.codeview.get_buffer(), afile)
            loader.load_async(1, None, None, None, self.file_load_finish, self.file)
        except GObject.GError as e:
            print("Error: " + e.message)

    def file_load_finish(self, source, result, file):

        try:
            success = source.load_finish(result)
        except GObject.GError as e:
            # happens on new file, if not exists
            print(e.message)

        if DEBUGLEVEL > 0:
            print("file %s loaded %s" % (file, success))

    def get_buffer(self):
        return self.codeview.get_buffer()
                
class CustomCompletionProvider(GObject.GObject, GtkSource.CompletionProvider):

    def do_get_name(self):
        return 'NXC-Functions'

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
                for func in nxc_funcs.nxc_funcs:
                    if func[0].startswith(left_text):
                        proposals.append(GtkSource.CompletionItem.new(
                            func[0], func[1], None, func[2]))

                context.add_proposals(self, proposals, True)
            return

class PrintingApp:
    '''Print with syntax highlightning'''

    def __init__(self, textview):
        self.operation = Gtk.PrintOperation.new()
        self.compositor = GtkSource.PrintCompositor.new_from_view(textview.codeview)

        self.compositor.set_header_format(True, textview.file, None, None)
        self.compositor.set_print_header(True)
        self.compositor.set_body_font_name("Monospace 10")

        self.operation.connect('begin-print', self.begin_print, self.compositor)
        self.operation.connect('draw-page', self.draw_page, self.compositor)
        self.operation.connect('end_print', self.end_print)

    def run(self, parent=None):

        result = self.operation.run(Gtk.PrintOperationAction.PRINT_DIALOG,
                                    parent)

        if result == Gtk.PrintOperationResult.ERROR:
            message = self.operation.get_error()

            dialog = Gtk.MessageDialog(parent,
                                       0,
                                       Gtk.MessageType.ERROR,
                                       Gtk.ButtonsType.CLOSE,
                                       message)
            dialog.run()
            dialog.destroy()

    def begin_print(self, operation, context, compositor):

        if DEBUGLEVEL > 0:
            print("Initializing printing process...")

        while not compositor.paginate(context):
            pass
        n_pages = compositor.get_n_pages()
        operation.set_n_pages(n_pages)

        if DEBUGLEVEL > 0:
            print("Sending", n_pages, " pages to printer")

    def draw_page(self, operation, context, page_num, compositor):

        if DEBUGLEVEL > 0:
            print("Sending page:", (page_num+1))

        compositor.draw_page(context, page_num)

    def end_print(self, operation, context):

        if DEBUGLEVEL > 0:
            print("Document sent to printer")

