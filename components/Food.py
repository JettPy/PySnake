import turtle
from random import randrange

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
        x = randrange(-self._size * 10, self._size * 10, 20)
        y = randrange(-self._size * 10, self._size * 10, 20)
        self._food.goto(x, y)

    def get_coordinates(self):
        return self._food.xcor(), self._food.ycor()
