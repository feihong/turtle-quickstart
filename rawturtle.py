import tkinter as tk
import turtle

width, height = 600, 400

root = tk.Tk()
root.geometry(f'{width}x{height}')
root.title("RawTurtle in Tkinter Example")

def on_key(evt):
    if evt.keysym == 'Escape':
        root.quit()
root.bind('<KeyRelease>', on_key)

canvas = turtle.ScrolledCanvas(root, width=width, height=height, canvwidth=width-20, canvheight=height-20)
canvas.pack(fill=tk.BOTH, expand=True)

screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)

t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.hideturtle()

root.mainloop()
