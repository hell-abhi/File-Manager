from gi.repository import Gtk


def create_menu_bar():        
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
        return menu_bar
