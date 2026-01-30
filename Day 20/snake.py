from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN= 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction_locked = False

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)


    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x , new_y)
        self.head.forward(MOVE_DISTANCE)
        self.direction_locked = False

    def up(self):
        if self.head.heading() != DOWN and not self.direction_locked:
            self.head.setheading(UP)
            self.direction_locked = True

    def down(self):
        if self.head.heading() != UP and not self.direction_locked:
            self.head.setheading(DOWN)
            self.direction_locked = True

    def left(self):
        if self.head.heading() != RIGHT and not self.direction_locked:
            self.head.setheading(LEFT)
            self.direction_locked = True

    def right(self):
        if self.head.heading() != LEFT and not self.direction_locked:
            self.head.setheading(RIGHT)
            self.direction_locked = True

    def wrap_around(self):
        if self.head.xcor() > 300:
            self.head.setx(-300)
        elif self.head.xcor() < -300:
            self.head.setx(300)
        elif self.head.ycor() > 300:
            self.head.sety(-300)
        elif self.head.ycor() < -300:
            self.head.sety(300)