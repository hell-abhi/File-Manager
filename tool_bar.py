from gi.repository import Gtk
from shared_variables import (CURRENT_DIRECTORY, tool_button_up, tool_button_back, tool_button_forward, toggletoolbutton, path_index, path_list, icon_store, list_store)
from list_view import populate_icon_store, populate_list_store
from list_view import click_home_button, click_up_button, click_back_button, click_forward_button, click_toggle_button
import os


def create_tool_bar():

        # tool bar
        tool_bar = Gtk.Toolbar()
        
        tool_button_home = Gtk.ToolButton(Gtk.STOCK_HOME)
        tool_button_home.connect("clicked", click_home_button)
        tool_bar.insert(tool_button_home, 0)
        
        tool_button_up.connect("clicked", click_up_button)
        tool_button_up.set_sensitive(False)
        tool_bar.insert(tool_button_up, 1)
        
        tool_button_back.connect("clicked", click_back_button)
        tool_button_back.set_sensitive(False)
        tool_bar.insert(tool_button_back, 2)
        
        tool_button_forward.connect("clicked", click_forward_button)
        tool_button_forward.set_sensitive(False)
        tool_bar.insert(tool_button_forward, 3)
        
#        tool_button_list.connect("clicked", click_list_button)
#        tool_button_list.set_sensitive(True)
#        tool_bar.insert(tool_button_list, 4)
#        
#        tool_button_icon.connect("clicked", click_icon_button)
#        tool_button_icon.set_sensitive(True)
#        tool_bar.insert(tool_button_icon, 5)

        toggletoolbutton.set_icon_name("gtk-media-play")
        toggletoolbutton.connect("toggled", click_toggle_button)
        tool_bar.add(toggletoolbutton)
        
        return tool_bar

