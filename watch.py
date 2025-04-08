import sys
from pathlib import Path
import threading
import importlib
import turtle
import queue
import watchfiles
import hua


POLL_INTERVAL = 100
reload_queue = queue.Queue(maxsize=1)

def watch_file(py_file):
    for _changes in watchfiles.watch(py_file):
        # print(_changes)
        reload_queue.put('reload')

if __name__ == '__main__':
    py_file = Path(sys.argv[1])

    # Monkey patch hua.run so it doesn't run on import
    hua.run = lambda _main: None
    module = importlib.import_module(py_file.stem)

    watch_thread = threading.Thread(target=watch_file, args=(py_file,))
    watch_thread.daemon = True
    watch_thread.start()

    def poll():
        if not reload_queue.empty():
            reload_queue.get() # we don't need the value
            print('Reloading...')
            turtle.getscreen().clear()
            importlib.reload(module)
            module.main()

        turtle.ontimer(poll, POLL_INTERVAL)

    turtle.ontimer(poll, POLL_INTERVAL)

    hua._run(module.main)
