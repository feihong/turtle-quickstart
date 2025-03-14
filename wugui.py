import sys
from pathlib import Path
import tempfile
import threading
import importlib
import turtle
import watchfiles


geometry_file = Path(tempfile.gettempdir()) / 'wugui_geometry'

def run(main):
    root = get_root()

    if geometry_file.exists():
        root.geometry(geometry_file.read_text())

    root.protocol('WM_DELETE_WINDOW', on_exit)

    def on_key(evt):
        if evt.keysym == 'Escape':
            on_exit()

    root.bind('<KeyRelease>', on_key)

    turtle.listen()
    main()
    turtle.mainloop()

def get_root():
    return turtle.getscreen().getcanvas().winfo_toplevel()

def on_exit():
    geometry_file.write_text(get_root().geometry())
    turtle.bye()

def watch_file(py_file, module):
    for _changes in watchfiles.watch(py_file):
        get_root().after_idle(reload, module)

def reload(module):
    turtle.getscreen().clearscreen()
    importlib.reload(module)
    module.main()

if __name__ == '__main__':
    py_file = Path(sys.argv[1])
    module = importlib.import_module(py_file.stem)

    watch_thread = threading.Thread(target=watch_file, args=(py_file, module))
    watch_thread.daemon = True
    watch_thread.start()

    run(module.main)
