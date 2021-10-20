import turtle
from utils.constants import *

class Message:

    _message = None
    _size = None
    _is_dark = None


    def __init__(self, size : int, is_dark : bool):
        self._size = size
        self._is_dark = is_dark
        self._message = turtle.Turtle()
        self._message.speed(0)
        self._message.penup()
        self._message.hideturtle()
        self._message.goto(size * 10, size * 10)

    def write(self, is_win : bool, is_pause : bool = False):
        if not is_pause:
            if is_win:
                self._message.color(WIN_TEXT_COLOR)
                self._message.write(
                    'YOU WIN',
                    align = 'center',
                    font = (FONT_STYLE, self._size * 2, 'bold'),
                )
            else:
                self._message.color(LOSE_TEXT_COLOR)
                self._message.write(
                    'YOU LOSE',
                    align = 'center',
                    font = (FONT_STYLE, self._size * 2, 'bold'),
                )
        else:
            if self._is_dark:
                self._message.color(TEXT_COLOR_DARK)
            else:
                self._message.color(TEXT_COLOR)
            self._message.write(
                'PAUSE',
                align = 'center',
                font = (FONT_STYLE, self._size * 2, 'bold'),
            )


    def hide_message(self):
        self._message.clear()

