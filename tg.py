import sys
from pathlib import Path
import functools
import threading
import importlib
import turtle
import watchfiles


def run(main):
    turtle.onkey(turtle.bye, 'q')
    turtle.listen()
    main()
    turtle.mainloop()

def get_root():
    return turtle.getscreen().cv.winfo_toplevel()

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

