import pgi
pgi.install_as_gi()
from gi.repository import Gio
from gi.repository import Gtk

from .gui.window import CaverWindow
from os import environ

class App(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(
            self,
            application_id="com.github.jjl.caver",
            flags=Gio.ApplicationFlags.FLAGS_NONE
        )
        self.theme = Gtk.IconTheme.get_default()
        self.connect('activate', self.on_activate)

    def lookup_icon(self, mime):
        return Gio.content_type_get_icon(mime)

    def on_activate(self,_):
        "Called when the mainloop has started up"
        self.spawn_window('/home/james','/home/james')

    def spawn_window(self, path, rel_to, view="column"):
        w = CaverWindow(self, path, rel_to, view)
        w.show_all()
        self.add_window(w)
        
    def _quit(self):
        Gtk.main_quit()
        
    def quit(self):
        for s in self.sessions:
            s.close_if_open()
        self._quit()
        
    def quit_with_error(self,message):
        dialog = Gtk.MessageDialog(
            self, 0, Gtk.MessageType.ERROR,
            Gtk.ButtonsType.OK, message
        )
        dialog.run()
        dialog.destroy()
        self._quit()
