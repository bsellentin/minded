# -*- coding: utf-8 -*-

import logging

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gio

LOGGER = logging.getLogger(__name__)

class RecentFiles:

    def __init__(self):
        self.recent_manager = Gtk.RecentManager.get_default()
        self.recent_filter = Gtk.RecentFilter()
        self.recent_filter.add_mime_type("application/x-evc")
        self.recent_filter.add_mime_type("application/x-nxc")
        self.recent_filter.add_application("minded")
        self.recent_store = Gtk.ListStore(str, str, str)

        self.clean_recent_files()
        self.recent_manager.connect("changed", self.update_recent_files)

    def add(self, uri):
        gio_file = Gio.File.new_for_uri(uri)

        recent_data = Gtk.RecentData()
        recent_data.display_name = gio_file.get_basename()
        recent_data.description = None;
        recent_data.mime_type, _ = Gio.content_type_guess(uri)
        recent_data.app_name = GLib.get_application_name()
        recent_data.app_exec = "%s %%u" % GLib.get_prgname()
        #recent_data.groups = [];
        recent_data.is_private = False;

        self.recent_manager.add_full(uri, recent_data)

    def update_recent_files(self, *args):
        self.recent_store.clear()
        self.clean_recent_files()

    def clean_recent_files(self):
        minded_items = self.filter_items()
        for item in minded_items:
            gfile = Gio.File.new_for_uri(item.get_uri())
            if gfile.query_exists():
                self.recent_store.append([item.get_short_name(),
                                  item.get_display_name(),
                                  item.get_uri()])
            else:
                self.recent_manager.remove_item(item.get_uri())

    def filter_items(self):
        # from/after meld/recent.py
        getters = {Gtk.RecentFilterFlags.URI: "uri",
                   Gtk.RecentFilterFlags.DISPLAY_NAME: "display_name",
                   Gtk.RecentFilterFlags.MIME_TYPE: "mime_type",
                   Gtk.RecentFilterFlags.APPLICATION: "applications",
                   #Gtk.RecentFilterFlags.GROUP: "groups",
                   Gtk.RecentFilterFlags.AGE: "age"}
        needed = self.recent_filter.get_needed()
        attrs = [v for k, v in getters.items() if needed & k]
        # LOGGER.debug(attrs)
        # ['mime_type', 'applications']

        filtered_items = []
        for item in self.recent_manager.get_items():
            filter_data = {}
            for attr in attrs:
                filter_data[attr] = getattr(item, "get_" + attr)()
            # LOGGER.debug('filter_data {}'.format(filter_data))
            # filter_data {'mime_type': 'application/x-nxc', 'applications': ['minded']}
            filter_info = Gtk.RecentFilterInfo()
            filter_info.contains = self.recent_filter.get_needed()
            for f, v in filter_data.items():
                if isinstance(v, list):
                    continue
                setattr(filter_info, f, v)
            if self.recent_filter.filter(filter_info):
                filtered_items.append(item)

        return filtered_items
