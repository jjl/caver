from gi.repository import Gtk
from .file import FileEntry
class DirectoryColumnList(Gtk.ListBox):
    """
    A DirectoryColumnList is the listbox widget that renders a list of files
    in the column view
    """
    def __init__(self,app):
        Gtk.ListBox.__init__(self)
        self.app = app

    def replace_files(self,files):
        for f in files:
            self.insert(FileEntry(self.app,f),-1)

    def find_name(self,name):
        "Given a filename, locates the file that bears it or None"
        # Each child gets automatically wrapped in a ListBowRow
        for r in self.get_children():
            for c in r.get_children():
                try: # Just in case somebody packs in something else
                    if c.name == name:
                        return name
                except Exception, e:
                    continue
        return None

    def select_name(self,name):
        "Given a filename, selects the file that bears it. Returns bool"
        c = self.find_name(name)
        if c is not None:
            self.select_row(c.get_parent())
            return True
        return False
    
