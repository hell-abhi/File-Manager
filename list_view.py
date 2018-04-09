from gi.repository import Gtk, Gdk
from shared_variables import CURRENT_DIRECTORY
from functools import partial
import os


def populate_list_store(store):

    store.clear()
    
    for file_name in os.listdir(CURRENT_DIRECTORY):        
        modified_time = 0#os.path.getmtime(CURRENT_DIRECTORY+file_name)
        size = 0#os.path.getsize(CURRENT_DIRECTORY+file_name)
        if not file_name[0] == '.': 
            if os.path.isdir(os.path.join(CURRENT_DIRECTORY, file_name)):
                store.append([
                'folder', 
                file_name, 
                True,
                modified_time,
                size
                ])
            else:
                store.append([
                'text-x-generic', 
                file_name, 
                False,
                modified_time,
                size
                ])
                
             
def on_button_clicked(widget, event):
    if event.button == 1:
        print("Hello")
    elif event.button == 3:
        print("welcome")
        
        
def on_double_click(store, widget, path, column):
    #import pdb;
    #pdb.set_trace()
    global CURRENT_DIRECTORY
    model = widget.get_model()
    file_name = model[path][1]
    file_is_dir = model[path][2]
    
    if file_is_dir:
        if CURRENT_DIRECTORY == '/':
            CURRENT_DIRECTORY = CURRENT_DIRECTORY+file_name
        else:
            CURRENT_DIRECTORY = CURRENT_DIRECTORY + '/' + file_name
    else:
        return
        
    populate_list_store(store)


def create_list_view():

    # creating list view
    store = Gtk.ListStore(str, str, bool, float, float)
    populate_list_store(store)
    treeview = Gtk.TreeView(store)
    #treeview.connect("button_press_event", on_button_clicked)
    
    # setting up renderer
    cellrenderertext = Gtk.CellRendererText()
    cellrendererpixbuf = Gtk.CellRendererPixbuf()

    #column 0 of list view to display icons
    treeviewcolumn = Gtk.TreeViewColumn("Icon")
    treeview.append_column(treeviewcolumn)
    treeviewcolumn.pack_start(cellrendererpixbuf, True)
    treeviewcolumn.add_attribute(cellrendererpixbuf, "icon-name", 0)

    #column 1 of list view to display names
    treeviewcolumn = Gtk.TreeViewColumn("Name")
    treeview.append_column(treeviewcolumn)
    treeviewcolumn.pack_start(cellrenderertext, True)
    treeviewcolumn.add_attribute(cellrenderertext, "text", 1)
    
    #column 2 of list view to display if it is directory
    treeviewcolumn = Gtk.TreeViewColumn("Is Dir?")
    treeview.append_column(treeviewcolumn)
    treeviewcolumn.pack_start(cellrenderertext, True)
    treeviewcolumn.add_attribute(cellrenderertext, "text", 2)
    
    #column 3 of list view to display last modified time
    treeviewcolumn = Gtk.TreeViewColumn("Modified Time")
    treeview.append_column(treeviewcolumn)
    treeviewcolumn.pack_start(cellrenderertext, True)
    treeviewcolumn.add_attribute(cellrenderertext, "text", 3)
    
    #column 4 of list view to display size
    treeviewcolumn = Gtk.TreeViewColumn("Size")
    treeview.append_column(treeviewcolumn)
    treeviewcolumn.pack_start(cellrenderertext, True)
    treeviewcolumn.add_attribute(cellrenderertext, "text", 4)
    
    treeview.connect("row-activated", partial(on_double_click, store))
    
    return treeview
