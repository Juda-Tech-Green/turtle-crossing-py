from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape('turtle')
        self.setheading(90)
        self.goto(0,-280)

    def move_up(self):
        self.goto(self.xcor(),self.ycor()+10)

    def move_down(self):
        self.goto(self.xcor(),self.ycor()-10)

    def move_left(self):
        self.goto(self.xcor()-10,self.ycor())

    def move_right(self):
        self.goto(self.xcor()+10,self.ycor())

    def pass_level(self):
        self.goto(0,-280)