import sys
from pathlib import Path
import functools
import threading
import importlib
import turtle
import watchfiles


def run(main):
    turtle.listen()
    root = get_root()
    root.protocol('WM_DELETE_WINDOW', on_exit)

    def on_key(evt):
        if evt.keysym == 'Escape':
            on_exit()

    root.bind('<KeyRelease>', on_key)
    main()
    turtle.mainloop()

def get_root():
    return turtle.getscreen().getcanvas().winfo_toplevel()

def on_exit():
    turtle.bye()

def watch_file(py_file):
    for _changes in watchfiles.watch(py_file):
        get_root().event_generate('<<file_changed>>')

def reload(module, _event):
    turtle.getscreen().clearscreen()
    importlib.reload(module)
    module.main()

if __name__ == '__main__':
    py_file = Path(sys.argv[1])
    module = importlib.import_module(py_file.stem)

    watch_thread = threading.Thread(target=watch_file, args=(py_file,))
    watch_thread.daemon = True
    watch_thread.start()

    get_root().bind('<<file_changed>>', functools.partial(reload, module))

    run(module.main)

