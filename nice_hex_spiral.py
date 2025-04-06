import turtle
import hua

colors = 'red purple blue green yellow orange'.split()

def main():
    turtle.tracer(1)

    # t = turtle.Pen()
    t = turtle
    turtle.bgcolor('black')

    for x in range(360):
        t.pencolor(colors[x % 6])
        t.width(x/100 + 1)
        t.fd(x)
        t.left(90)

if __name__ == '__main__':
    hua.run(main)
