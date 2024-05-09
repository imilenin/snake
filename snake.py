from turtle import Turtle
import time

SEGMENT_SIZE = 20
INIT_SIZE = 3
DELAY = 0.05
SCR_WIDTH = 600
SCR_HEIGHT = 600


class Snake:
    snake = []

    def __init__(self):
        for i in range(0, INIT_SIZE):
            t = Turtle(shape="square", visible=True)
            t.color("white")
            t.penup()
            t.goto(-i * SEGMENT_SIZE, 0)
            self.snake.append(t)
        self.length = INIT_SIZE

    def move(self):
        is_head = True
        prev_segment_location = [0, 0]
        for t in self.snake:
            if is_head:
                prev_segment_location = t.pos()
                t.forward(SEGMENT_SIZE)
                is_head = False
            else:
                tmp = t.pos()
                t.goto(prev_segment_location)
                prev_segment_location = tmp
            time.sleep(DELAY)

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def increment(self):
        t = Turtle(shape="square", visible=True)
        t.color("white")
        t.penup()
        t.goto(-self.length * SEGMENT_SIZE, 0)
        self.snake.append(t)
        self.length += 1


