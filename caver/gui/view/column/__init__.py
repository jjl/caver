from gi.repository import Gtk
from .list import DirectoryColumnList
from .file import ColumnFile, FileEntry
from ....util import relative_to
import os

class ColumnView(Gtk.ScrolledWindow):
    def __init__(self, app, path, rel_to):
        """
        A column view renders a column for each directory in a path
        It is relative to a provided root. E.g. if path is /foo/bar/baz/quux
        and rel_to is /foo/bar, we would render columns for baz and quux
        @param path string currently selected path
        @param rel_to the path of the 'root' element
        """
        Gtk.ScrolledWindow.__init__(self)
        self.app = app
        self._init_box()
        self.navigate_to(path, rel_to)
        
    def _init_box(self):
        self.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.NEVER)
        self.flowbox = Gtk.FlowBox()
        self.flowbox.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.add(self.flowbox)

    def navigate_to(self, path, rel_to):
        """
        """
        if not os.path.isdir(rel_to):
            rel_to = "/"
        rel = relative_to(path, rel_to)
        if rel is None or rel == ".":
            rel = []
        else:
            rel = [x for x in rel.split(os.path.sep) if x != ""]
        self.cols = []
        working = rel_to
        self._add_column(rel_to)
        for p in rel:
            working = os.path.join(working, p)
            self.cols[-1].select_item(p)
            self._add_column(working)
      
    def _add_column(self, path):
        if os.path.isdir(path):
            c = DirectoryColumn(self.app,self,path)
        else:
            c = FileColumn(self.app,self,path)
        self.flowbox.insert(c,-1)

    
class DirectoryColumn(Gtk.ScrolledWindow):
    """
    A DirectoryColumn is a column in the ColumnView that shows the contents
    of a directory. Each entry will be a ColumnFile
    """
    def __init__(self,app,view,path,sort="name"):
        Gtk.ScrolledWindow.__init__(self)
        self.app, self.view, self.path = app, view, path
        self._init_box()
        self.change_sort(sort)
        self.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.update_files([os.path.join(path, p) for p in sorted(os.listdir(path))])
  
    def _init_box(self):
        self.listbox = DirectoryColumnList(self.app)
        self.listbox.connect('row-selected',self.on_select_item)
        self.vbox = Gtk.Box()
        self.vbox.set_orientation(Gtk.Orientation.VERTICAL)
        self.vbox.pack_start(self.listbox, True, True, 0)
        self.add(self.vbox)
    
    def change_sort(self, sort):
        if sort not in ["name","date"]:
            self.sort = "name"
        else:
            self.sort = sort
            print("Invalid sort type: {}. Defaulting to name".format(sort))

    def update_files(self,files):
        self.listbox.replace_files(files)

    def select_item(self,name):
        self.listbox.select_name(name)

    def on_select_item(self, lb, item):
        row = self.listbox.get_selected_row()
        if row is not None:
            print("file selected: {}".format(row))
            print("children: {}".format(row.get_children()))
        else:
            print "No selection"

    def on_deselect_item(self, item):
        pass

class FileColumn():
    def __init__(self,app,view,path):
        pass

    
    
