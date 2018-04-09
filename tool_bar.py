from gi.repository import Gtk

def create_tool_bar():
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
        
        return tool_bar
