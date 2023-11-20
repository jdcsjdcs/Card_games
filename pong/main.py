from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball =  Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # collusion with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # collusion with paddle
    if (ball.distance(r_paddle) < 63 and ball.xcor() == 330) or (ball.distance(l_paddle) < 60 and ball.xcor() < -330):
        ball.bounce_x()
    
    # detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
     # detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        
        
screen.exitonclick()

