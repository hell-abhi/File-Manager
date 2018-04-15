from gi.repository import Gtk, GdkPixbuf


CURRENT_DIRECTORY = '/'
icon_store = Gtk.ListStore(GdkPixbuf.Pixbuf, str, bool, float, float)
list_store = Gtk.ListStore(str, str, bool, float, float)
main_view = None


tool_button_up = Gtk.ToolButton(Gtk.STOCK_GO_UP)
tool_button_back = Gtk.ToolButton(Gtk.STOCK_GO_BACK)
tool_button_forward = Gtk.ToolButton(Gtk.STOCK_GO_FORWARD)
#tool_button_list = Gtk.ToolButton(Gtk.STOCK_JUSTIFY_FILL)
#tool_button_icon = Gtk.ToolButton(Gtk.STOCK_PASTE)
toggletoolbutton = Gtk.ToggleToolButton()


path_list = ['/']
path_index = 0
