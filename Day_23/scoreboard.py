from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.actual_level = 1
        self.penup()
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.actual_level}", font=FONT)

    def increase_level(self):
        self.actual_level += 1
        self.update_level()

    def game_over(self):
        self.hideturtle()
        self.goto(-26, 0)
        self.write("GAME OVER")

