import sys
from pathlib import Path
import threading
import importlib
import turtle
import queue
import watchfiles
import hua


reload_queue = queue.Queue(maxsize=1)

def watch_file(py_file):
    for _changes in watchfiles.watch(py_file):
        # print(_changes)
        reload_queue.put('reload')

# In Python 3.13+, we must use polling instead of root.after_idle
def poll(fn, interval):
    def new_fn():
        fn()
        turtle.ontimer(new_fn, interval)

    turtle.ontimer(new_fn, interval)

if __name__ == '__main__':
    py_file = Path(sys.argv[1])

    # Monkey patch hua.run so it doesn't run the main function during import
    hua.run = lambda main: main
    module = importlib.import_module(py_file.stem)

    watch_thread = threading.Thread(target=watch_file, args=(py_file,))
    watch_thread.daemon = True
    watch_thread.start()

    def reload():
        if not reload_queue.empty():
            reload_queue.get() # we don't need the value
            print('Reloading...')
            turtle.getscreen().clear()
            importlib.reload(module)
            module.main()

    poll(reload, interval=100)

    hua._run(module.main)
