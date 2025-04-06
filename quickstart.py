from turtle import *
import hua

def main():
    tracer(100)
    shape('turtle')

    for i in range(15_000):
        forward(1)
        if i % 360 == 0:
            right(10)
        else:
            right(1)

if __name__ == '__main__':
    hua.run(main)
