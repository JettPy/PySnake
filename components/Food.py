import turtle
from random import randrange, randint

from utils.constants import *


class Food:

    _size = None
    _food = None

    def __init__(self, size : int):
        self._size = size
        self._food = turtle.Turtle()
        self._food.speed(0)
        self._food.shape(FOOD_SHAPE)
        self._food.color(FOOD_COLOR)
        self._food.penup()

    def spawn(self):
        x = randint(1, self._size) * 20 - 10
        y = randint(1, self._size) * 20 - 10
        self._food.goto(x, y)

    def get_coordinates(self):
        return self._food.xcor(), self._food.ycor()
