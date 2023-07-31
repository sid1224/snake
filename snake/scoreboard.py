from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Times New Roman", 20, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update()

    def gameOver(self):
        self.goto(0,0)
        self.write("Game over", align="center", font=20)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

