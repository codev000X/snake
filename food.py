import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(0.75)
        self.penup()
        self.color("blue")
        self.refresh()
    def refresh(self):
        n_x=random.randint(-280,280)
        n_y=random.randint(-280,280)
        self.goto(n_x,n_y)