from turtle import *
import tg

def main():
    shape('turtle')
    tracer(40)
    for i in range(15_000):
        fd(1)
        if i % 360 == 0:
            right(10)
        else:
            right(1)

if __name__ == '__main__':
    tg.run(main)
