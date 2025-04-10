import itertools
from turtle import *
import hua

colors = itertools.cycle('red purple blue green yellow orange'.split())

def main():
    tracer(10)
    bgcolor('black')

    for color, x in zip(colors, range(360)):
        pencolor(color)
        width(x/100 + 1)
        fd(x)
        # change this value for wildly different results
        left(59)

hua.run(main)
