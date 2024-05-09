from turtle import Turtle

TOP = 250
LEFT = -20


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(LEFT, TOP)
        self.write_text()

    def increment(self):
        self.score += 1
        self.clear()
        self.write_text()

    def write_text(self):
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def write_go_text(self):
        self.write(arg=f"GAME OVER. Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over_msg(self):
        self.clear()
        self.write_go_text()
