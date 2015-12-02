from gi.repository import Gtk

class CaverHeader(Gtk.HeaderBar):
    def __init__(self, win):
        Gtk.HeaderBar.__init__(self)
        self.win = win
        self.set_show_close_button(True)
        self._init_new_button()._init_search()
        self.set_title("Caver")

    def _init_search(self):
        self.search_entry = Gtk.SearchEntry()
        self.search_entry.set_placeholder_text("Search")
        self.search_entry.connect('search-changed', self.win.on_search_change)
        self.search_entry.connect('stop-search',    self.win.on_search_stop)
        # self.search_entry.connect('next-match',     self.win.on_search_next)
        # self.search_entry.connect('previous-match', self.win.on_search_prev)
        self.pack_start(self.search_entry)
        return self

    def _init_new_button(self):
        self.new_button = Gtk.Button(label="New")
        self.new_button.connect('clicked', self.win.on_new_press)
        self.pack_start(self.new_button)
        return self

