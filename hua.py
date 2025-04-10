from pathlib import Path
import tempfile
import turtle


geometry_file = Path(tempfile.gettempdir()) / 'hua_geometry'

def _run(main):
    root = turtle.getcanvas().winfo_toplevel()

    if geometry_file.exists():
        root.geometry(geometry_file.read_text())

    def on_exit():
        geometry_file.write_text(root.geometry())
        turtle.bye()

    root.protocol('WM_DELETE_WINDOW', on_exit)

    def on_key(evt):
        print(evt.keycode, evt.state, evt.keysym)
        if evt.keysym == 'Escape':
            on_exit()
        # Restart the program on Cmd+r
        elif evt.keysym == 'r' and (evt.state & 0x8):
            turtle.getscreen().clear()
            main()

    root.bind('<KeyRelease>', on_key)

    main()
    turtle.mainloop()

# Overridable inside watch
run = _run
