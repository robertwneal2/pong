from turtle import Turtle
MOVE_DIST = 40
TOP_LIMIT = 490


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        width_stretch = 1
        height_stretch = 10
        self.shape('square')
        self.shapesize(height_stretch, width_stretch)
        self.color('white')
        self.penup()
        self.goto(x_pos, 0)

    def go_up(self):
        new_y = self.ycor() + MOVE_DIST
        if new_y > TOP_LIMIT:
            new_y = TOP_LIMIT
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DIST
        if new_y < -TOP_LIMIT:
            new_y = -TOP_LIMIT
        self.goto(self.xcor(), new_y)
