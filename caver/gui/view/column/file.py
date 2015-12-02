from gi.repository import Gtk
from mimetypes import guess_type
import os

icon_size = Gtk.IconSize.BUTTON

class FileEntry(Gtk.ListBoxRow):
  def __init__(self,app,path):
    Gtk.ListBoxRow.__init__(self)
    self.file = ColumnFile(app,path)
    self.add(self.file)

class ColumnFile(Gtk.Box):
  """
  A columnfile is a file widget in the list provided by the DirectoryColumn
  It consists of an icon and a label
  """
  def __init__(self,app,path):
    Gtk.Box.__init__(self)
    self.path, self.app = path, app
    self.name = os.path.basename(path)
    self.set_orientation(Gtk.Orientation.HORIZONTAL)
    self._init_label()._init_icon()._pack()

  def __repr__(self):
    return "<ColumnFile: {} at {}>".format(self.name, self.path)

  def __str__(self):
    return "<ColumnFile: {} at {}>".format(self.name, self.path)

  def _init_label(self):
    """This label holds the name of the file"""
    self.label = Gtk.Label(self.name)
    self.label.set_halign(Gtk.Align.START)
    return self

  def _init_icon(self):
    """
    Tries to find an appropriate icon for the file
    This could be a directory icon, an icon based on the mimetype derived
    from the filename or it will fall back to a default file icon
    """
    if os.path.isdir(self.path):
      i = self.app.lookup_icon("inode/directory")
      # This shouldn't fail. We used to trap it, but it's presumed safe
      self.icon = Gtk.Image.new_from_gicon(i,icon_size)
    else:
      mime = guess_type(self.path)[0]
      if mime is not None:
        i = self.app.lookup_icon(mime)
        if i is not None:
          self.icon = Gtk.Image.new_from_gicon(i,icon_size)
          return self
      # Fallback to a basic file icon
      self.icon = Gtk.Image.new_from_icon_name(Gtk.STOCK_FILE,icon_size)
    return self
  
  def _pack(self):
    "Packs the widgets into the layout"
    self.pack_start(self.icon, False, False, 0)
    self.pack_end(self.label, True, True, 10)
    return self    
