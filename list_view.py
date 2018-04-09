from gi.repository import Gtk, Gdk
from shared_variables import (CURRENT_DIRECTORY, store, tool_button_up, tool_button_back, 
tool_button_forward, path_list, path_index)
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
        
        
def on_double_click(widget, path, column):
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
    tool_button_up.set_sensitive(True)
    tool_button_back.set_sensitive(True)
    path_list.append(CURRENT_DIRECTORY)
    global path_index
    path_index += 1
    print(path_list, path_index)
    
    
def click_home_button(widget):
    
    global CURRENT_DIRECTORY
    if CURRENT_DIRECTORY == '/home/hell_abhi':
        return
    CURRENT_DIRECTORY = os.path.realpath(os.path.expanduser('~'))
    populate_list_store(store)
    tool_button_up.set_sensitive(True)
    tool_button_back.set_sensitive(True)
    path_list.append(CURRENT_DIRECTORY)
    global path_index
    path_index += 1
    print(path_list, path_index)
    
    
def click_up_button(widget):
    
    global CURRENT_DIRECTORY
    CURRENT_DIRECTORY = os.path.dirname(CURRENT_DIRECTORY)
    path_list.append(CURRENT_DIRECTORY)
    global path_index
    path_index += 1
    print(path_list, path_index)
    populate_list_store(store)
    sensitive = True
    if  CURRENT_DIRECTORY == '/': 
        sensitive = False
    widget.set_sensitive(sensitive)
    if sensitive:
        tool_button_back.set_sensitive(True)
    
    
def click_back_button(widget):
    
    global path_index
    if path_index == 0:
        widget.set_sensitive(False)
        return
    path_index -= 1
    print(path_list, path_index)
    tool_button_forward.set_sensitive(True)
    global CURRENT_DIRECTORY
    CURRENT_DIRECTORY = path_list[path_index]
    populate_list_store(store)
    if CURRENT_DIRECTORY == '/':
        tool_button_up.set_sensitive(False)
    
    
def click_forward_button(widget):
    
    global path_index
    if path_index == len(path_list)-1:
        widget.set_sensitive(False)
        return
    path_index += 1
    print(path_list, path_index)
    tool_button_back.set_sensitive(True)
    global CURRENT_DIRECTORY
    CURRENT_DIRECTORY = path_list[path_index]
    populate_list_store(store)
    if CURRENT_DIRECTORY == '/':
        tool_button_up.set_sensitive(False)


def create_list_view():

    # creating list view
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
    #treeviewcolumn.set_expand(True)

    #column 1 of list view to display names
    treeviewcolumn = Gtk.TreeViewColumn("Name")
    treeview.append_column(treeviewcolumn)
    treeviewcolumn.pack_start(cellrenderertext, True)
    treeviewcolumn.add_attribute(cellrenderertext, "text", 1)
    treeviewcolumn.set_expand(True)
    
    #column 2 of list view to display if it is directory
    treeviewcolumn = Gtk.TreeViewColumn("Is Dir?")
    treeview.append_column(treeviewcolumn)
    treeviewcolumn.pack_start(cellrenderertext, True)
    treeviewcolumn.add_attribute(cellrenderertext, "text", 2)
    treeviewcolumn.set_expand(True)
    
    #column 3 of list view to display last modified time
    treeviewcolumn = Gtk.TreeViewColumn("Modified Time")
    treeview.append_column(treeviewcolumn)
    treeviewcolumn.pack_start(cellrenderertext, True)
    treeviewcolumn.add_attribute(cellrenderertext, "text", 3)
    treeviewcolumn.set_expand(True)
    
    #column 4 of list view to display size
    treeviewcolumn = Gtk.TreeViewColumn("Size")
    treeview.append_column(treeviewcolumn)
    treeviewcolumn.pack_start(cellrenderertext, True)
    treeviewcolumn.add_attribute(cellrenderertext, "text", 4)
    treeviewcolumn.set_expand(True)
    
    treeview.connect("row-activated", on_double_click)
    
    return treeview
