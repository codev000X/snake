import turtle
from turtle import Turtle
import random

start_position=[(0,0),(-10,0),(-20,0)]
class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()

    def add(self, seg):
        turtle.colormode(255)
        colour_list = ["black", "midnight blue", "dark blue", "navy", "dark green", "forest green", "dark red","maroon",
                       "saddle brown", "dark slate gray", "dim gray", "dark olive green", "dark cyan", "dark magenta","indigo"]

        sq = Turtle("circle")
        sq.shapesize(0.9)
        sq.color(random.choice(colour_list))
        sq.penup()
        sq.goto(seg)
        self.segment.append(sq)

    def create_snake(self):
        for seg in start_position:
            self.add(seg)

    def extend(self):
        self.add(self.segment[-1].position())

    def move(self):
        for current_segment in range(len(self.segment)-1,0,-1):
            new_x=self.segment[current_segment-1].xcor()
            new_y=self.segment[current_segment-1].ycor()
            self.segment[current_segment].goto(new_x,new_y)
        self.segment[0].fd(20)


    # Controlling Procedure
    def left(self):
        if self.segment[0].heading()!=0:
            self.segment[0].setheading(180)
    def right(self):
        if self.segment[0].heading()!=180:
            self.segment[0].setheading(0)

    def up(self):
        if self.segment[0].heading()!=270:
            self.segment[0].setheading(90)

    def down(self):
        if self.segment[0].heading()!=90:
            self.segment[0].setheading(270)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()


