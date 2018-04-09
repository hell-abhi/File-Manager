from gi.repository import Gtk


CURRENT_DIRECTORY = '/'
store = Gtk.ListStore(str, str, bool, float, float)


tool_button_up = Gtk.ToolButton(Gtk.STOCK_GO_UP)
tool_button_back = Gtk.ToolButton(Gtk.STOCK_GO_BACK)
tool_button_forward = Gtk.ToolButton(Gtk.STOCK_GO_FORWARD)


path_list = ['/']
path_index = 0
