import turtle
from scoreboard import ScoreBoard
from turtle import Turtle, Screen
from food import Food


class Snake(ScoreBoard):
    screen = Screen()

    def __init__(self):
        super().__init__()
        self.turtleList = [turtle]
        self.create_snake()
        self.food = Food()
        self.head = self.turtleList[0]

    def move(self):
        for i in range(len(self.turtleList) - 1, 0, -1):
            new_x = self.turtleList[i - 1].xcor()
            new_y = self.turtleList[i - 1].ycor()
            self.turtleList[i].goto(new_x, new_y)
        self.turtleList[0].forward(20)
        self.foodEaten()

    def foodEaten(self):
        print(f"YENİ YEMEK: {self.food.pos}")
        if round(self.turtleList[0].pos()[0]) == round(self.food.pos[0]) and round(
                self.turtleList[0].pos()[1]) == round(self.food.pos[1]):
            self.food.createFood()
            self.growSnake()

    def growSnake(self):
        x = self.turtleList[len(self.turtleList) - 1]
        y = self.turtleList[len(self.turtleList) - 2]
        correctCordinateX = self.correctCordinate(x.xcor(), x.ycor())
        correctCordinateY = self.correctCordinate(y.xcor(), y.ycor())

        if correctCordinateX[0] == correctCordinateY[0]:
            self.addElementToTail(correctCordinateX[0], correctCordinateX[1] + 20)
            self.screen.update()
        else:
            self.addElementToTail(correctCordinateX[0] + 20, correctCordinateX[1])
            self.screen.update()
        self.increase_scoreboard()


    def addElementToTail(self, x, y):
        turtle = Turtle(shape="square")
        turtle.penup()
        # turtle.shapesize(1.5)
        turtle.color("white")
        turtle.goto(x, y)
        turtle.speed("slowest")
        self.turtleList.append(turtle)

    def create_snake(self):
        for i in range(3):
            turtle = Turtle(shape="square")
            turtle.penup()
            # turtle.shapesize(1.5)
            turtle.color("white")
            turtle.goto(x=-i * 20, y=0)
            turtle.speed("slowest")
            self.turtleList.append(turtle)
        self.screen.update()

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def correctCordinate(self, x_cor, y_cor):
        newX = int(x_cor / 20)
        newY = int(y_cor / 20)
        return (newX * 20, newY * 20)

    def checkCollesion(self):
        for i in range(4, len(self.turtleList), 1):

            if self.correctCordinate(self.head.xcor(), self.head.ycor()) == self.correctCordinate(
                    self.turtleList[i].xcor(), self.turtleList[i].ycor()):
                self.collesion()
                return True
        return False

    def isGameOver(self):
        new_x = self.turtleList[0].xcor()
        new_y = self.turtleList[0].ycor()
        print(new_x)
        print(new_y)
        if abs(new_x) > 300 or abs(new_y) > 300:
            self.clear()
            self.gameOver()
            return False

        return True
