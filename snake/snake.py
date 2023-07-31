from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        turtle1 = Turtle(shape="square")
        turtle1.color("white")
        turtle1.penup()
        turtle1.goto(position)
        self.turtle_list.append(turtle1)

    def reset_snake(self):
        for seg in self.turtle_list:
            seg.goto(1000,1000)
        self.turtle_list.clear()
        self.create_snake()
        self.head = self.turtle_list[0]

    def extend(self):
        self.add_segment(self.turtle_list[-1].position())

    def move(self):
        for turtle_num in range(len(self.turtle_list)-1, 0, -1):
            new_x = (self.turtle_list[turtle_num - 1]).xcor()
            new_y = (self.turtle_list[turtle_num - 1]) .ycor()
            (self.turtle_list[turtle_num]).goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
