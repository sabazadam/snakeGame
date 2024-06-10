from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", align="center", font=('Courier', 24, 'normal'))

    def increase_scoreboard(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def gameOver(self):
        self.update_scoreboard()
        self.goto(0,0)
        self.write(f"Game Over!", align="center", font=('Courier', 24, 'normal'))
    def collesion(self):
        self.update_scoreboard()
        self.goto(0,0)
        self.write("Collesion Happened! Game is over", align="center", font=('Courier', 24, 'normal'))

