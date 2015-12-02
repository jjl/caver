Caver
-----

A file manager for the rest of us, written for pypy and gtk+

Features
--------

* Clean, minimal user interface
* Column view (like Finder.app). Why the hell has noone else implemented this?

Future Features
---------------
* Sorting per column
* Press the spacebar to quickly preview a file
* Virtual drive mounting
* Full plugin support

Future plugins
--------------
* rsync
* git
* mercurial
* nelly

Pypy?
-----

https://pypy.org/

Pypy implements the python language, but better. It adds support for JIT
compilation and continuations and there will be an STM at some point.

Pypy allows us to write this in python and it be quick and responsive enough

Right now, it supports cpython as well, but in the future that is likely to
change.

Use?
----

    pypy -m caver

