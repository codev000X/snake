from turtle import Turtle
class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x=295,y=0)
        self.pendown()
        self.pensize(20)
        self.goto(x=295,y=295)
        self.goto(x=-295,y=295)
        self.goto(x=-295,y=-295)
        self.goto(x=295,y=-295)
        self.goto(x=295,y=0)
