import sys
from pathlib import Path
import threading
import importlib
import turtle
import watchfiles
import hua


def watch_file(py_file, module):
    for _changes in watchfiles.watch(py_file):
        print(_changes)
        hua.get_root().after_idle(reload, module)

def reload(module):
    print('reload')
    turtle.getscreen().clearscreen()
    importlib.reload(module)
    module.main()

if __name__ == '__main__':
    py_file = Path(sys.argv[1])
    module = importlib.import_module(py_file.stem)

    watch_thread = threading.Thread(target=watch_file, args=(py_file, module))
    watch_thread.daemon = True
    watch_thread.start()

    hua.run(module.main)
