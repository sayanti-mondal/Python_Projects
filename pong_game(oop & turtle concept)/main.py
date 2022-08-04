from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

# paddle = Turtle()
# paddle.shape('square')#20,20 #100,20 #width, height
# paddle.color('white')
# paddle.shapesize(stretch_wid=5,stretch_len=1)
# paddle.penup()
# paddle.goto(x=350, y=0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(),new_y)
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(),new_y)

screen.listen()
screen.onkey(fun=r_paddle.go_up, key='Up')
screen.onkey(fun=r_paddle.go_down, key='Down')
screen.onkey(fun=l_paddle.go_up, key='w')
screen.onkey(fun=l_paddle.go_down, key='s')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball need to bounce vertically
        ball.y_bounce()

    # detect collision with paddle with ball
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        # ball need to bounce horizontally
        ball.x_bounce()

    # detect r_paddle miss
    if ball.xcor() > 380:
        # ball need to goto initial position and then opposite direction
        ball.reset_position()
        scoreboard.l_point()

    # detect l_paddle miss
    if ball.xcor() < -380:
        # ball need to goto initial position and then opposite direction
        ball.reset_position()
        scoreboard.r_point()





screen.exitonclick()
