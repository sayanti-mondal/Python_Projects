from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()
# Draw a square
# Draw a dashed line
# Draw different shapes in differnt angles with different colors
# tim.shape('turtle')
#tim.color('black')


# # #moved forward 100 paces
#  tim.forward(100) # drawn 1st side of square
# #
# # #draw 2nd side of square
#  tim.left(90) #turned left in 90 degree angle
#  tim.forward(100) #in that direction moved forward
# #
# # #draw 3rd side of square
#  tim.left(90)
#  tim.forward(100)
# #
# # #draw 4th side of square
#  tim.left(90)
#  tim.forward(100)
#
# # for _ in range(4):
# #     timmy_the_turtle.forward(100)
# #     timmy_the_turtle.left(90)

#drawing a dashed line
# for _ in range(5):
#
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

"""
from turtle import Turtle,Screen
import random

tim = Turtle()
colors = ['red','blue','green','yellow','purple','orange','black','pink']

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for side in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(side)
    
"""
#colors = ['red','blue','green','yellow','purple','orange','black','pink']
# import turtle as t
# t.colormode(255)
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r,g,b)
#     return random_color
#
# directions = [0, 90, 180,270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
import turtle as t
t.colormode(255)
tim.speed("fastest")

def random_color():
     r = random.randint(0,255)
     g = random.randint(0,255)
     b = random.randint(0,255)
     color = (r,g,b)
     return color


# for _ in range(100):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.setheading(tim.heading() + 5)

#size_of_gap = 5
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)) :
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)





#it has to be at the end of the code

screen.exitonclick()