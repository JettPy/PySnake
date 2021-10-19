import turtle
from random import randrange, randint

from utils.constants import *


class Food:

    _size = None
    _food = None

    def __init__(self, size : int, mode : bool):
        self._size = size
        self._food = turtle.Turtle()
        self._food.speed(0)
        self._food.shape(FOOD_SHAPE)
        if mode:
            self._food.color(FOOD_COLOR_DARK)
        else:
            self._food.color(FOOD_COLOR)
        self._food.penup()

    def spawn(self, coordinates : list):
        free_space = False
        while not free_space:
            x = randint(1, self._size) * 20 - 10
            y = randint(1, self._size) * 20 - 10
            for segment in coordinates:
                if segment[0] == x and segment[1] == y:
                    free_space = False
                    break
                else:
                    free_space = True
        self._food.goto(x, y)

    def get_coordinates(self):
        return self._food.xcor(), self._food.ycor()
