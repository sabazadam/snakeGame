import time
from turtle import Turtle, Screen
from snake import Snake
from scoreboard import ScoreBoard
screen = Screen()
screen.bgcolor("black")
turtleList = []
screen.listen()
turningPointDict = {}
screen.setup(width=600, height=600)
screen.title("snake.py Game")
screen.tracer(0)
snake = Snake()


x = 0
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
while snake.isGameOver():
    snake.move()
    screen.update()
    time.sleep(0.08)
    if snake.checkCollesion():
        print("Collesion Happened! Game is over")
        break
screen.exitonclick()
"""

if x % 10 == 0:
    turtleList[0].setheading(turtleList[0].heading() + 90)
    turningPointDict[turtleList[0].pos()] = turtleList[0].heading()
    print(turtleList[0].heading())
    turtleList[0].forward(20)
else:
    turtleList[0].forward(20)
x += 1


def followFrontBox():
    index1 = 0
    index2 = 1
    for i in turtleList:
        if turtleList[index1].pos()[0] != turtleList[index2].pos()[0]:
            if turtleList[index2].pos() in turningPointDict.keys():
                turtleList[index2].setheading(turningPointDict[turtleList[index2].pos()])
                print(f"Ben kaplumva {index2} Döndüm! New Heading: {turningPointDict[turtleList[index2].pos()]}")
                turtleList[index2].forward(20)
            else:
                print(f"X yönünde hareket olacak {index2}. kaplumba")
                turtleList[index2].forward(20)
        elif turtleList[index2].pos()[1] != turtleList[index1].pos()[1]:
            if turtleList[index2].pos() in turningPointDict.keys():
                turtleList[index2].setheading(turningPointDict[turtleList[index2].pos()])
                print(f"Ben kaplumva {index2} Döndüm! New Heading: {turningPointDict[turtleList[index2].pos()]}")
                turtleList[index2].forward(20)
            else:
                turtleList[index2].forward(20)
                print(
                    f"Ben kaplumba {index2}. x konumu eşit y'ye göre ilerliyom ve ilerledim yönüm -> {turtleList[index2].heading()}")

        index2 += 1
        index1 += 1
        if index2 == len(turtleList): break

"""
