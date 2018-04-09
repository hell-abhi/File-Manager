from gi.repository import Gtk
from shared_variables import CURRENT_DIRECTORY, tool_button_up, tool_button_back, tool_button_forward
from list_view import click_home_button, click_up_button, click_back_button, click_forward_button
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
        
        tool_button_create = Gtk.ToolButton(Gtk.STOCK_NEW)
        tool_bar.insert(tool_button_create, 4)
        
        return tool_bar
