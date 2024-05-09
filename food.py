from turtle import Turtle
import random

HEIGHT = 600
WIDTH = 600


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.goto(random.randint(-WIDTH // 2 + 20, WIDTH // 2 - 20), random.randint(-HEIGHT // 2 + 20, HEIGHT // 2 - 20))

    def refresh(self):
        self.goto(random.randint(-WIDTH // 2 + 20, WIDTH // 2 - 20),
                  random.randint(-HEIGHT // 2 + 20, HEIGHT // 2 - 20))
