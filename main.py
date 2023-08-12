from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# generate screen
screen = Screen()
screen_width = 1600
screen_height = 1200
screen.setup(screen_width, screen_height)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# draw center line
line_turtle = Turtle()
line_turtle.color('white')
line_turtle.pensize(5)
line_turtle.hideturtle()
line_turtle.penup()
line_turtle.goto(0, -screen_height/2 + 15)
y_pos = line_turtle.ycor()
while y_pos < screen_height/2:
    line_turtle.pendown()
    y_pos += 25
    line_turtle.goto(0, y_pos)
    line_turtle.penup()
    y_pos += 25
    line_turtle.goto(0, y_pos)

# create paddles
x_pos_offset = 50
x_positions = [-screen_width/2 + x_pos_offset, screen_width/2 - x_pos_offset]
left_paddle = Paddle(x_positions[0])
right_paddle = Paddle(x_positions[1])
screen.listen()
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')

# create ball
ball = Ball()
ball_speed = 1/60
y_limit = screen_height/2 - 25

# create scoreboards
left_pos = [-200, 550]
right_pos = [200, 550]
left_score = Scoreboard(left_pos)
right_score = Scoreboard(right_pos)

# play game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball_speed)
    ball.move()
    ball_x_pos = ball.xcor()
    ball_y_pos = ball.ycor()
    if ball_y_pos > y_limit or ball_y_pos < -y_limit:
        ball.wall_bounce()
    if ball.hit_paddle(left_paddle.pos()) or ball.hit_paddle(right_paddle.pos()):
        ball.paddle_bounce()
        ball_speed *= 0.9
    elif ball_x_pos > screen_width/2:
        left_score.increase_score()
        ball.restart()
        ball.paddle_bounce()
        ball_speed = 1/60
    elif ball_x_pos < -screen_width/2:
        right_score.increase_score()
        ball.restart()
        ball.paddle_bounce()
        ball_speed = 1 / 60
