from gi.repository import Gtk

class Root(Gtk.FlowBox):
    def __init__(self):
        Gtk.FlowBox.__init__(self)
        self._init_self()

    def _init_self(self):
        l = Gtk.Label("Foo")
        self.add(l)
        return self
    
    
