from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-230, 260)
        self.hideturtle()
        self.level = 1

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", False, "center", FONT)

    def refresh_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", False, "center", FONT)