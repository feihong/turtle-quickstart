import random
from turtle import *
import hua

colors = 'red yellow blue green orange purple white gray'.split()

def spiral(x, y, size):
    penup()
    setpos(x, y)
    pendown()
    for m in range(size):
        forward(m * 2)
        left(91)

@hua.run
def main():
    # tracer(2)
    speed(0)

    bgcolor('black')
    for n in range(50):
        pencolor(random.choice(colors))
        size = random.randint(10, 40)
        x = random.randrange(0, window_width() // 2)
        y = random.randrange(0, window_height() // 2)

        spiral(x, y, size)
        spiral(-x, y, size)
        spiral(-x, -y, size)
        spiral(x, -y, size)
