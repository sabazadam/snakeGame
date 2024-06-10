import random
from turtle import Turtle,Screen
from scoreboard import ScoreBoard
screen = Screen()
class Food:
    foodList = []
    def createFood(self):
        if len(self.foodList) != 0:
            self.foodList[0].hideturtle()
            self.foodList.pop()
        index_x = random.choice(range(-280,280,20))
        index_y = random.choice(range(-280,280,20))
        self.pos = (index_x,index_y)
        self.food = Turtle("circle")
        self.food.penup()
        self.food.shapesize(0.6)
        self.food.color("AliceBLue")
        self.food.goto(index_x,index_y)
        screen.update()
        self.foodList.append(self.food)

    def __init__(self):
        self.createFood()