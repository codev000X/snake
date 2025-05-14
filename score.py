from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt","r") as file:
            self.high_score=int(file.read())
        self.color("red")
        self.hideturtle()
        self.penup()
        self.game_score()

    def game_score(self):
        self.clear()
        self.goto(x=-200,y=300)

        self.write(f" Score : {self.score}     High Score:{self.high_score}",font=("Cursive",18,"bold"),align="center")


    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("data.txt", mode="w") as file:
                content = file.write(str(self.high_score))
        self.score=0
        self.game_score()


    def in_score(self):
        self.score+=1

        self.game_score()
