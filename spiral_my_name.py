import itertools
from turtle import *
import hua

colors = itertools.cycle('red yellow blue green'.split())

def get_font(font_size):
    return 'Arial', int(font_size), 'bold'

@hua.run
def main():
    tracer(10)
    bgcolor('black')

    your_name = textinput('Enter your name', "What's your name?")

    for color, x in zip(colors, range(100)):
        penup()
        forward(x * 4)
        pencolor(color)
        pendown()
        write(your_name, font=get_font((x + 4) / 4))
        left(92)
