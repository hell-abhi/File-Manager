import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, GdkPixbuf, Gdk
from menu_bar import create_menu_bar
from tool_bar import create_tool_bar
from side_bar import create_side_bar
from list_view import create_list_view


class EntryWindow(Gtk.Window):

    def __init__(self):
        # creating window
        Gtk.Window.__init__(self, title="File Manager")
        self.set_size_request(800, 600)
        self.set_position(Gtk.WindowPosition.CENTER)
        
        vertical_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(vertical_box)
        
        menu_bar = create_menu_bar()
        vertical_box.pack_start(menu_bar, False, False, 0)
        
        tool_bar = create_tool_bar()
        vertical_box.pack_start(tool_bar, False, False, 0)
        
        horizontal_box = Gtk.Box()
        vertical_box.pack_start(horizontal_box, True, True, 0)
        
        side_bar = create_side_bar()
        horizontal_box.pack_start(side_bar, False, True, 0)
        horizontal_box.set_halign(Gtk.Align.START)
        
        list_view = create_list_view()
        #list_view.set_hexpand (True)
        #list_view.set_vexpand (True)
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(list_view)
        #scrolled_window.set_min_content_width(1000)
        scrolled_window.set_policy(hscrollbar_policy=Gtk.PolicyType.NEVER, vscrollbar_policy=Gtk.PolicyType.AUTOMATIC)
        horizontal_box.pack_start(scrolled_window, True, True, 0)
        

win = EntryWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
