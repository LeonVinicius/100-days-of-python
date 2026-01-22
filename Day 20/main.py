from turtle import Screen, Turtle
from snack import Snack
import time


screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Snack Game")
screen.tracer(0)

snack = Snack()

screen.listen()
screen.onkey(snack.up, "Up")
screen.onkey(snack.down, "Down")
screen.onkey(snack.left, "Left")
screen.onkey(snack.right, "Right")




game_in_on = True

while game_in_on:
    screen.update()
    time.sleep(0.1)
    snack.move()



screen.exitonclick()