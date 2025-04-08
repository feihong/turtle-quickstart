from turtle import *
import hua

def square(length):
    for _ in range(4):
        forward(length)
        left(90)

def main():
    tracer(2)
    for _ in range(36):
        square(100)
        right(10)


hua.run(main)
