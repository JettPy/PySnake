import turtle
from utils.constants import *

class ScoreBoard:

    _size = None
    _font_size = None
    _board = None
    _score = None
    _high_score = None

    def __init__(self, size : int, is_dark : bool):
        self._size = size
        if size > 21:
            self._font_size = 24
        elif size > 15:
            self._font_size = 16
        else:
            self._font_size = 10
        self._score = 0
        self._high_score = 0
        self._board = turtle.Turtle()
        self._board.speed(0)
        self._board.shape('square')
        if is_dark:
            self._board.color(TEXT_COLOR_DARK)
        else:
            self._board.color(TEXT_COLOR)
        self._board.penup()
        self._board.hideturtle()
        self._board.goto(self._size * 10, self._size * 20 - self._get_indent())
        self._update_board()

    def _get_indent(self):
        coefficient = 0
        if self._size <= 15:
            coefficient = 10
        return self._font_size * 2 // 10 * 10 + coefficient

    def increase_score(self):
        self._score += 1
        if self._score > self._high_score:
            self._high_score = self._score
        self._board.clear()
        self._update_board()

    def clear_board(self):
        self._score = 0
        self._board.clear()
        self._update_board()

    def get_score(self):
        return self._score

    def _update_board(self):
        if self._size > 9:
            self._board.write(
                'score: {} High score: {}'.format(self._score, self._high_score),
                align = 'center',
                font = (FONT_STYLE, self._font_size, 'normal'),
            )
        else:
            self._board.write(
                '{}/{}'.format(self._score, self._high_score),
                align = 'center',
                font = (FONT_STYLE, self._font_size, 'normal'),
            )
