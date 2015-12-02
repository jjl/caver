import os
from gi.repository import Gio

def move_to_trash(path):
    return Gio.File.new_from_path(path).do_trash(None)

def exists(p):
    "Does the file path exist?"
    return os.path.isfile(p) or os.path.isdir(p)

def is_prefix(p, rel):
    """
    Determines whether p is inside of rel
    """
    # By requiring they both exist, we should be fine
    if exists(p) and os.path.isdir(rel):
        return (os.path.commonprefix([p,rel]) == rel)
    else:
        return False

def relative_to(p, rel):
    """
    if rel contains p (deeply), returns p relative to rel else None
    """
    if is_prefix(p, rel):
        return os.path.relpath(p,rel)
    else:
        return None

def read_dir(p):
    ps = sorted([os.path.join(p, x) for x in os.listdir(p)])
    dirs, files = [], []
    for p in ps:
        if os.path.isdir(p):
            dirs.push(p)
        else:
            files.push(p)
    return dirs, files
