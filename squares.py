from turtle import *
import wugui

def square(length):
    for _ in range(4):
        forward(length)
        left(90)

def main():
    tracer(2)
    for _ in range(36):
        square(100)
        right(10)

if __name__ == '__main__':
    wugui.run(main)
