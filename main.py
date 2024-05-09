# This is a sample Python script.
from turtle import Screen
from snake import Snake, SEGMENT_SIZE
from food import Food
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600

scr = Screen()


def set_up():
    scr.setup(WIDTH, HEIGHT)
    scr.bgcolor("black")
    scr.tracer(0)


def main():
    set_up()
    s = Snake()
    f = Food()
    sb = Scoreboard()
    scr.update()
    screen_listen(s)
    game_loop(s, f, sb)
    scr.exitonclick()


def screen_listen(s):
    scr.listen()
    scr.onkey(s.up, "Up")
    scr.onkey(s.down, "Down")
    scr.onkey(s.left, "Left")
    scr.onkey(s.right, "Right")


def game_loop(s, f, sb):
    game_is_running = True
    while game_is_running:
        s.move()
        scr.update()
        if check_food_collision(s, f):
            f.refresh()
            scr.update()
            s.increment()
            sb.increment()
        if check_wall_collision(s) or detect_snake_collision(s):
            game_is_running = False
    sb.game_over_msg()


def check_food_collision(s, f):
    return s.snake[0].distance(f) <= SEGMENT_SIZE


def check_wall_collision(s):
    is_collided = False
    if s.snake[0].xcor() > WIDTH / 2 - SEGMENT_SIZE:
        is_collided = True
    if s.snake[0].xcor() < -WIDTH / 2 + SEGMENT_SIZE:
        is_collided = True
    if s.snake[0].ycor() > HEIGHT / 2 - SEGMENT_SIZE:
        is_collided = True
    if s.snake[0].ycor() < -HEIGHT / 2 + SEGMENT_SIZE:
        is_collided = True
    return is_collided


def detect_snake_collision(s):
    for seg in s.snake[1:]:
        if s.snake[0].distance(seg) < SEGMENT_SIZE // 2:
            return True
    return False

main()
