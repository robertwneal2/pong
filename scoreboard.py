from turtle import Turtle
FONT = ('Arial', 14, 'bold')


class Scoreboard(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.color('green2')
        self.penup()
        self.shapesize(5, 5)
        self.hideturtle()
        self.goto(pos[0], pos[1])
        self.score = 0
        self.display_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, 'center', FONT)

    def display_score(self):
        self.write(f'SCORE: {self.score}', False, 'center', FONT)
