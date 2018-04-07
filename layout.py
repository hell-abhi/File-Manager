import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class EntryWindow(Gtk.Window):

    def __init__(self):
        # creating window
        Gtk.Window.__init__(self, title="File Manager")
        self.set_size_request(800, 600)
        self.set_position(Gtk.WindowPosition.CENTER)
        
        vertical_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(vertical_box)
        
        # menu bar
        menu_bar = Gtk.MenuBar()
        menu_bar_item_file = Gtk.MenuItem(label="File")
        menu_bar.append(menu_bar_item_file)
        menu_bar_item_edit = Gtk.MenuItem(label="Edit")
        menu_bar.append(menu_bar_item_edit)
        menu_bar_item_view = Gtk.MenuItem(label="View")
        menu_bar.append(menu_bar_item_view)
        menu_bar_item_go = Gtk.MenuItem(label="Go")
        menu_bar.append(menu_bar_item_go)
        menu_bar_item_bookmarks = Gtk.MenuItem(label="Bookmarks")
        menu_bar.append(menu_bar_item_bookmarks)
        menu_bar_item_help = Gtk.MenuItem(label="Help")
        menu_bar.append(menu_bar_item_help)
        vertical_box.pack_start(menu_bar, False, False, 0)
        
        # tool bar
        tool_bar = Gtk.Toolbar()
        tool_button_home = Gtk.ToolButton(Gtk.STOCK_HOME)
        tool_bar.insert(tool_button_home, 0)
        tool_button_forward = Gtk.ToolButton(Gtk.STOCK_GO_BACK)
        tool_bar.insert(tool_button_forward, 1)
        tool_button_back = Gtk.ToolButton(Gtk.STOCK_GO_FORWARD)
        tool_bar.insert(tool_button_back, 2)
        tool_button_create = Gtk.ToolButton(Gtk.STOCK_NEW)
        tool_bar.insert(tool_button_create, -1)
        vertical_box.pack_start(tool_bar, False, False, 0)
        
        horizontal_box = Gtk.Box()
        vertical_box.pack_start(horizontal_box, True, True, 0)
        
        # side bar
        placessidebar = Gtk.PlacesSidebar()
        placessidebar.connect("open-location", self.on_open_location)
        horizontal_box.pack_start(placessidebar, True, True, 0)

    def on_open_location(self, placessidebar, location, flags):
        location = placessidebar.get_location()

        print("Opened URI: %s" % (GLocalFile.get_uri(location)))
        

win = EntryWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
