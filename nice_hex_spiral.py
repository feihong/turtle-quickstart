from turtle import *
import hua

colors = 'red purple blue green yellow orange'.split()

def main():
    tracer(10)
    bgcolor('black')

    for x in range(360):
        pencolor(colors[x % 6])
        width(x/100 + 1)
        fd(x)
        # change this value for wildly different results
        left(59)

hua.run(main)
