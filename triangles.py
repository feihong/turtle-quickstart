import turtle
import hua

def triangle(t):
    for _ in range(3):
        t.forward(100)
        t.right(120)

def main():
    turtle.tracer(1)

    turtles = [turtle.Turtle('turtle') for _ in range(6)]
    for i, t in enumerate(turtles):
        t.teleport(i*60 - 150, 0)

    for t in turtles:
        triangle(t)


hua.run(main)
