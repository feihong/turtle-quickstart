import tkinter as tk
from turtle import RawTurtle, TurtleScreen

root = tk.Tk()
root.title("RawTurtle in Tkinter Example")

def on_key(evt):
    if evt.keysym == 'Escape':
        root.quit()
root.bind('<KeyRelease>', on_key)

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

screen = TurtleScreen(canvas)
t = RawTurtle(screen)

t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.hideturtle()

root.mainloop()
