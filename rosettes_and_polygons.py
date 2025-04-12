from turtle import *
import hua

def get_sides():
    return int(numinput('Number of sides', 'How many sides in your spiral?', 4))

@hua.run
def main():
    tracer(2)

    sides = get_sides()
    for m in range(5, 75):
        left(360 / sides + 5)
        width(m // 25 + 1)
        penup()
        forward(m * 4)
        pendown()
        if m % 2 == 0:
            for _ in range(sides):
                circle(m / 3)
                right(360 / sides)
        else:
            for _ in range(sides):
                forward(m)
                right(360 / sides)
