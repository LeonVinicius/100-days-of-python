from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()