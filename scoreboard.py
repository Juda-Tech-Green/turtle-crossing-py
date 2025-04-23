from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial",16,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.player_score = 0
        self.goto(-260, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Level {self.player_score}', False, ALIGNMENT, FONT)


    def pass_level(self):
        self.player_score += 1

    def game_over(self):
        self.clear()
        self.goto(0,100)
        self.write(f'Game Over', False, ALIGNMENT, ("Arial",25,"normal"))
        self.goto(0,-100)
        self.write(f'Reached level: {self.player_score}', False, ALIGNMENT, ("Arial",25,"normal"))
        self.goto(0, -200)
        self.write(f"Press 'space' to reset the game", False, ALIGNMENT, ("Arial", 25, "normal"))
        self.goto(-260, 260)