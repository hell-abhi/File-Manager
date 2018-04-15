from gi.repository import Gtk, Gdk
from shared_variables import (CURRENT_DIRECTORY, tool_button_up, tool_button_back, 
tool_button_forward, path_list, path_index, list_store, icon_store, toggletoolbutton, main_view)
from functools import partial
import os, subprocess


def get_icon(name):
        theme = Gtk.IconTheme.get_default()
        return theme.load_icon(name, 60, 0)


def populate_icon_store():

    global icon_store
    icon_store.clear()
    
    file_icon = get_icon(Gtk.STOCK_FILE)
    folder_icon = get_icon(Gtk.STOCK_DIRECTORY)

    for file_name in os.listdir(CURRENT_DIRECTORY):        
        modified_time = 0#os.path.getmtime(CURRENT_DIRECTORY+file_name)
        size = 0#os.path.getsize(CURRENT_DIRECTORY+file_name)
        if not file_name[0] == '.':
            if os.path.isdir(os.path.join(CURRENT_DIRECTORY, file_name)):
                icon_store.append([
                folder_icon, 
                file_name, 
                True,
                modified_time,
                size
                ])
            else:
                icon_store.append([
                file_icon, 
                file_name, 
                False,
                modified_time,
                size
                ])
                
                
def populate_list_store():

    global list_store
    list_store.clear()
    
    file_icon = Gtk.STOCK_FILE
    folder_icon = Gtk.STOCK_DIRECTORY
    
    for file_name in os.listdir(CURRENT_DIRECTORY):        
        modified_time = 0#os.path.getmtime(CURRENT_DIRECTORY+file_name)
        size = 0#os.path.getsize(CURRENT_DIRECTORY+file_name)
        if not file_name[0] == '.':
            if os.path.isdir(os.path.join(CURRENT_DIRECTORY, file_name)):
                list_store.append([
                folder_icon, 
                file_name, 
                True,
                modified_time,
                size
                ])
            else:
                list_store.append([
                file_icon, 
                file_name, 
                False,
                modified_time,
                size
                ])
                
                
def populate_main_store():

    if(toggletoolbutton.get_active()):
        populate_icon_store()
    else:
        populate_list_store()


def on_single_click(widget, event):

    if event.button == 1:
        print("Hello")
    elif event.button == 3:
        print("welcome")
        
        
def on_double_click_list(widget, path, column):

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
        if CURRENT_DIRECTORY == '/':
            current_file = CURRENT_DIRECTORY+file_name
        else:
            current_file = CURRENT_DIRECTORY + '/' + file_name
        subprocess.call(['xdg-open', current_file])
        
    if(toggletoolbutton.get_active()):
        populate_icon_store()
    else:
        populate_list_store()
    tool_button_up.set_sensitive(True)
    tool_button_back.set_sensitive(True)
    path_list.append(CURRENT_DIRECTORY)
    global path_index
    path_index += 1
    print(path_list, path_index)
    
    
def on_double_click_icon(widget, path):

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
        if CURRENT_DIRECTORY == '/':
            current_file = CURRENT_DIRECTORY+file_name
        else:
            current_file = CURRENT_DIRECTORY + '/' + file_name
        subprocess.call(['xdg-open', current_file])
        
    populate_icon_store()
    tool_button_up.set_sensitive(True)
    tool_button_back.set_sensitive(True)
    path_list.append(CURRENT_DIRECTORY)
    global path_index
    path_index += 1
    print(path_list, path_index) 


def click_toggle_button(widget):
    global store
    global main_view
    print(toggletoolbutton.get_active())
    print(main_view)
    if(toggletoolbutton.get_active()):
        populate_icon_store()
    else:
        populate_list_store()
    if toggletoolbutton.get_active():
        main_view = create_icon_view()
    else:
        main_view = create_list_view()
    
    
def click_home_button(widget):
    
    global CURRENT_DIRECTORY
    if CURRENT_DIRECTORY == '/home/hell_abhi':
        return
    CURRENT_DIRECTORY = os.path.realpath(os.path.expanduser('~'))
    if(toggletoolbutton.get_active()):
        populate_icon_store()
    else:
        populate_list_store()
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
    if(toggletoolbutton.get_active()):
        populate_icon_store()
    else:
        populate_list_store()
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
    if(toggletoolbutton.get_active()):
        populate_icon_store()
    else:
        populate_list_store()
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
    if(toggletoolbutton.get_active()):
        populate_icon_store()
    else:
        populate_list_store()
    if CURRENT_DIRECTORY == '/':
        tool_button_up.set_sensitive(False)


def create_list_view():

    # creating list view
    populate_list_store()
    treeview = Gtk.TreeView(list_store)
    treeview.connect("button_press_event", on_single_click)
    
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
    #treeviewcolumn.set_expand(True)
    
    #column 2 of list view to display if it is directory
    treeviewcolumn = Gtk.TreeViewColumn("Is Dir?")
    treeview.append_column(treeviewcolumn)
    treeviewcolumn.pack_start(cellrenderertext, True)
    treeviewcolumn.add_attribute(cellrenderertext, "text", 2)
    #treeviewcolumn.set_expand(True)
    
    #column 3 of list view to display last modified time
    treeviewcolumn = Gtk.TreeViewColumn("Modified Time")
    treeview.append_column(treeviewcolumn)
    treeviewcolumn.pack_start(cellrenderertext, True)
    treeviewcolumn.add_attribute(cellrenderertext, "text", 3)
    #treeviewcolumn.set_expand(True)
    
    #column 4 of list view to display size
    treeviewcolumn = Gtk.TreeViewColumn("Size")
    treeview.append_column(treeviewcolumn)
    treeviewcolumn.pack_start(cellrenderertext, True)
    treeviewcolumn.add_attribute(cellrenderertext, "text", 4)
    #treeviewcolumn.set_expand(True)
    
    treeview.connect("row-activated", on_double_click_list)
    
    return treeview
    
    
def create_icon_view():

    populate_icon_store()
    iconview = Gtk.IconView()
    iconview.set_model(icon_store)
    iconview.set_text_column(1)
    iconview.set_pixbuf_column(0)
    #iconview.set_tooltip_column(2)
    
    iconview.connect("item-activated", on_double_click_icon)
    
    return iconview

