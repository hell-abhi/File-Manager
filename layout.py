import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, GdkPixbuf

CURRENT_DIRECTORY = '/'

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
        vertical_box.pack_start(horizontal_box, False, True, 0)
        
        # side bar
        placessidebar = Gtk.PlacesSidebar()
        placessidebar.connect("open-location", self.on_open_location)
        horizontal_box.pack_start(placessidebar, True, False, 0)
        horizontal_box.set_halign(1.0)
        
        # creating list view
        store = Gtk.ListStore(GdkPixbuf.Pixbuf, str, bool, float, float)
        self.get_files(store)
        treeview = Gtk.TreeView(store)
        treeview.connect("button_press_event", self.on_button1_clicked)
        horizontal_box.pack_start(treeview, True, True, 0)

        cellrenderertext = Gtk.CellRendererText()
        cellrendererpixbuf = Gtk.CellRendererPixbuf()

        #column 0 of list view to display icons
        treeviewcolumn = Gtk.TreeViewColumn("Icon")
        treeviewcolumn.set_spacing(10)
        treeview.append_column(treeviewcolumn)
        treeviewcolumn.pack_start(cellrendererpixbuf, True)
        treeviewcolumn.add_attribute(cellrendererpixbuf, "pixbuf", 0)

        #column 1 of list view to display names
        treeviewcolumn = Gtk.TreeViewColumn("Name")
        treeviewcolumn.set_spacing(100)
        treeview.append_column(treeviewcolumn)
        treeviewcolumn.pack_start(cellrenderertext, True)
        treeviewcolumn.add_attribute(cellrenderertext, "text", 1)
        
        #column 2 of list view to display if it is directory
        treeviewcolumn = Gtk.TreeViewColumn("Is Dir?")
        treeviewcolumn.set_spacing(100)
        treeview.append_column(treeviewcolumn)
        treeviewcolumn.pack_start(cellrenderertext, True)
        treeviewcolumn.add_attribute(cellrenderertext, "text", 2)
        
        #column 3 of list view to display last modified time
        treeviewcolumn = Gtk.TreeViewColumn("Modified Time")
        treeviewcolumn.set_spacing(100)
        treeview.append_column(treeviewcolumn)
        treeviewcolumn.pack_start(cellrenderertext, True)
        treeviewcolumn.add_attribute(cellrenderertext, "text", 3)
        
        #column 4 of list view to display size
        treeviewcolumn = Gtk.TreeViewColumn("Size")
        treeviewcolumn.set_spacing(100)
        treeview.append_column(treeviewcolumn)
        treeviewcolumn.pack_start(cellrenderertext, True)
        treeviewcolumn.add_attribute(cellrenderertext, "text", 4)
        

    def on_open_location(self, placessidebar, location, flags):
        location = placessidebar.get_location()

        print("Opened URI: %s" % (GLocalFile.get_uri(location)))
        
    
    def get_files(self, store):
        for file_name in os.listdir(CURRENT_DIRECTORY):
            
            modified_time = os.path.getmtime(CURRENT_DIRECTORY+file_name)
            size = os.path.getsize(CURRENT_DIRECTORY+file_name)
            if not file_name[0] == '.': 
                if os.path.isdir(os.path.join(CURRENT_DIRECTORY, file_name)):
                    store.append([
                    Gtk.Image.new_from_stock(Gtk.STOCK_DIRECTORY, Gtk.IconSize.MENU), 
                    file_name, 
                    True,
                    modified_time,
                    size
                    ])
                else:
                    store.append([
                    Gtk.Image.new_from_stock(Gtk.STOCK_FILE, Gtk.IconSize.MENU), 
                    file_name, 
                    False,
                    modified_time,
                    size
                    ])
                    
                    
    def on_button1_clicked(self, widget, event):
        if event.button == 1:
            print("Hello")
        elif event.button == 3:
            print("welcome")
        

win = EntryWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
