from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.title('Turtle Crossing')
screen.colormode(255)
screen.tracer(0)
screen.listen()


crossing_player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

def reset_game():
    for car in car_manager.cars_list:
        car.hideturtle()
    crossing_player.goto(0, -280)
    car_manager.cars_list.clear()
    scoreboard.player_score = 0
    scoreboard.update_score()
    game_loop()


def game_loop():
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        scoreboard.update_score()
        car_manager.get_car()
        car_manager.move_cars()
        for car in car_manager.cars_list:
            if car.distance(crossing_player) < 20:
                scoreboard.game_over()
                return
        if crossing_player.ycor() >= 280:
            crossing_player.pass_level()
            scoreboard.pass_level()
            car_manager.upgrade_speed()


screen.onkey(key='w', fun=crossing_player.move_up)
screen.onkey(key='s', fun=crossing_player.move_down)
screen.onkey(key='a', fun=crossing_player.move_left)
screen.onkey(key='d', fun=crossing_player.move_right)
screen.onkey(key='space',fun=reset_game)
reset_game()
screen.mainloop()
