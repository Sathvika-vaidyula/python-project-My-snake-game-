import random
from turtle import Turtle, Screen
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off auto screen updates

# Create initial snake body
segments = []
for i in range(3):
    new_segment = Turtle("square")
    new_segment.color("black")
    new_segment.penup()
    new_segment.goto(x=-20 * i, y=0)  # Offset each segment
    segments.append(new_segment)


# Movement logic
def move():
    for i in range(len(segments) - 1, 0, -1):
        new_x = segments[i - 1].xcor()
        new_y = segments[i - 1].ycor()
        segments[i].goto(new_x, new_y)
    segments[0].forward(20)


# Control direction
def go_up():
    if segments[0].heading() != 270:
        segments[0].setheading(90)


def go_down():
    if segments[0].heading() != 90:
        segments[0].setheading(270)


def go_left():
    if segments[0].heading() != 0:
        segments[0].setheading(180)


def go_right():
    if segments[0].heading() != 180:
        segments[0].setheading(0)


# Food class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.goto(new_x, new_y)


# Scoreboard class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()  # Clears the previous score
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 16, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', move=False, align='center', font=('Arial', 16, 'normal'))


# Create food object and scoreboard
food = Food()
score = Scoreboard()

# Key bindings
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    move()

    # Detect collision with food
    if segments[0].distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        new_segment = Turtle("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)
        score.increase_score()  # Increase score after eating food

    # Detect collision with boundary
    if (segments[0].xcor() > 288 or segments[0].ycor() < -280 or
            segments[0].xcor() < -288 or segments[0].ycor() > 288):
        game_is_on = False
        score.game_over()

    # Detect collision with own body
    for segment in segments[1:]:
        if segments[0].distance(segment) < 10:  # Check if head collides with any body segment
            game_is_on = False
            score.game_over()

screen.exitonclick()
