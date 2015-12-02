from gi.repository import Gtk

from .header import CaverHeader
from ..view.column import ColumnView
from ..root import Root

class CaverWindow(Gtk.Window):
    def __init__(self, app, path, rel_to, view):
        Gtk.Window.__init__(self)
        self.set_default_size(600,450)
        self.app = app
        print("app at CW: {}".format(app))
        self._setup_self()._setup_root()._setup_view(path, rel_to, view)._setup_grid()

    def _setup_self(self):
        self.set_title('Caver')
        return self._setup_header()
    
    def _setup_header(self):
        self.header = CaverHeader(self)
        return self

    def _setup_root(self):
        self.root = Root()
        return self

    def _setup_view(self, path, rel_to, view):
        if view == "column":
            self.view = ColumnView(self.app, path, rel_to)
        # elif view == "list":
        #     pass
        # elif view == "icon":
        #     pass
        else:
            print "WARNING: defaulting to column view\n"
            return self._setup_view('column')
        return self

    def _setup_grid(self):
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.vbox.pack_end(  self.hbox, True,  True,  0)
        self.hbox.pack_start(self.root, False, False, 0)
        self.hbox.pack_end(  self.view, True,  True,  0)
        self.add(self.vbox)
        return self

    def navigate_to(self, path, rel_to):
        pass

    def on_new_press(self,*_):
        pass

    def on_search_change(self,*_):
        pass

    def on_search_stop(self,*_):
        pass
