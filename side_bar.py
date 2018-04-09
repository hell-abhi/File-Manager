from gi.repository import Gtk


def on_open_location(self, placessidebar, location, flags):
    location = placessidebar.get_location()
    flag = placessidebar.get_flag()
    print(location)

def create_side_bar():
    # side bar
    placessidebar = Gtk.PlacesSidebar()
    placessidebar.set_open_flags(Gtk.PlacesOpenFlags.NORMAL)
    placessidebar.connect("open-location", on_open_location)
    
    return placessidebar
