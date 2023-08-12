from turtle import Turtle
MOVE_DIST = 10
PADDLE_HEIGHT = 110
PADDLE_WIDTH = 15
PADDLE_X_OFFSET = 15


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(2, 2)
        self.color('red')
        self.penup()
        self.y_dir = 1
        self.x_dir = 1
        self.speed(0)

    def move(self):
        new_x = self.xcor() + self.x_dir * MOVE_DIST
        new_y = self.ycor() + self.y_dir * MOVE_DIST
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_dir *= -1

    def paddle_bounce(self):
        self.x_dir *= -1

    def hit_paddle(self, paddle_pos):
        paddle_x = paddle_pos[0]
        paddle_y = paddle_pos[1]
        ball_x = self.xcor()
        ball_y = self.ycor()
        if ball_x * paddle_x > 0:  # make sure paddle on correct side
            if self.x_dir * ball_x > 0:  # check if new direction is opposite to prevent multiple bounces
                if paddle_y - PADDLE_HEIGHT < ball_y < paddle_y + PADDLE_HEIGHT:  # check that ball hits paddle in y
                    if paddle_x > 0:  # check if right or left paddle
                        if paddle_x - PADDLE_WIDTH - PADDLE_X_OFFSET < ball_x < paddle_x - PADDLE_X_OFFSET:  # check
                            # that ball hits paddle in x
                            return True
                    else:
                        if paddle_x + PADDLE_X_OFFSET < ball_x < paddle_x + PADDLE_WIDTH + PADDLE_X_OFFSET:  # check
                            # that ball hits paddle in x
                            return True
        return False

    def restart(self):
        self.goto(0, 0)
