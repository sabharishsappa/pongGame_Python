from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreBoard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800,height = 600)
screen.bgcolor("Black")
screen.title("Pong Game")
screen.tracer(0)

screen.listen()

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
sb = ScoreBoard()

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")


game_is_on = True
sb.update_scoreBoard()


while game_is_on:
    screen.update()
    time.sleep(0.08)
    ball.move()

#     collosion detection with paddle
    if ball.xcor()>340 and ball.distance(r_paddle) < 50 or ball.xcor()<-340 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        ball.speed *= 0.9

    if ball.xcor() >380:
        ball.goto(0,0)
        sb.l_score_update()
        ball.bounce_x()
        ball.speed = 0.1

    if ball.xcor()<-380:
        ball.goto(0,0)
        sb.r_score_update()
        ball.bounce_x()
        ball.speed = 0.1

    #     collision with walls
    if ball.ycor()>280 or ball.ycor() <-280:
        ball.bounce_y()



screen.exitonclick()