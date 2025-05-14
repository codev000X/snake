from turtle import Screen
from store import Boundary
from score import Score
from snake import Snake
from food import Food
import time

screen=Screen()
screen.bgcolor("PapayaWhip")
screen.setup(width=700,height=700)
screen.tracer(0)

boundary=Boundary()
score=Score()
food=Food()
snake=Snake()

screen.listen()
screen.onkey(snake.left,"j")
screen.onkey(snake.right,"l")
screen.onkey(snake.up,"i")
screen.onkey(snake.down,"k")


game_over=False
while not game_over:


    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.segment[0].distance(food)<15:
        food.refresh()
        snake.extend()
        score.in_score()
    if snake.segment[0].xcor()> 295 or snake.segment[0].xcor() < -295 or snake.segment[0].ycor() > 295 or snake.segment[0].ycor() < -295:
        score.reset()
        snake.reset()


    for segments in snake.segment[1:]:
        if snake.segment[0].distance(segments) < 10:
            score.reset()
            snake.reset()



screen.exitonclick()