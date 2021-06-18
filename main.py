# import colorgram
#
# colors = colorgram.extract("dots.jpg", 30)
# colors_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     colors_list.append(new_color)
# print(colors_list)

import random
from turtle import Turtle, Screen

little_frog = Turtle()
screen = Screen()
screen.colormode(255)

colors = [(231, 206, 83), (229, 147, 85), (119, 166, 186), (160, 13, 19), (30, 110, 159), (235, 81, 44), (5, 99, 37),
          (176, 19, 14), (187, 187, 25), (121, 177, 144), (207, 62, 22), (23, 132, 41), (245, 201, 4), (10, 42, 77),
          (13, 64, 41), (137, 83, 98), (83, 17, 24), (46, 168, 74), (3, 66, 140), (173, 133, 149), (36, 25, 21),
          (45, 151, 198), (220, 63, 68), (227, 171, 162), (73, 135, 188), (172, 204, 174)]

y = -200
x = -200
little_frog.penup()
little_frog.setx(x)
little_frog.sety(y)


def draw():
    for _ in range(10):
        little_frog.dot(20, random.choice(colors))
        little_frog.forward(50)
    little_frog.sety(little_frog.ycor() + 35)
    little_frog.setx(x)


for _ in range(10):
    draw()
screen.exitonclick()
