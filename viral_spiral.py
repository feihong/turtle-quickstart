import itertools
from turtle import *
import hua

colors = itertools.cycle('red yellow blue green purple orange'.split())

def main():
    tracer(10)

    penup()
    bgcolor('black')
    sides = int(numinput('Number of sides', 'How many sides in your spiral of spirals? (2-6)', 4, 2, 6))

    for m in range(100):
        forward(m * 4)
        pos = position()
        hd = heading()
        print(pos, hd)

        for n in range(m // 2):
            pendown()
            pencolor(next(colors))
            forward(2*n)
            right(360 / sides - 2)
            penup()

        setx(pos[0])
        sety(pos[1])
        setheading(hd)
        left(360 / sides + 2)

hua.run(main)
