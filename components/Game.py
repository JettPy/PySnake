import time
import turtle
from components.ScoreBoard import ScoreBoard
from components.Snake import Snake
from components.Food import Food
from utils.constants import *

class Game:

    _size = None
    _is_loop = None
    _is_dark = None
    _is_god = None

    _is_pause = None

    _window = None
    _snake = None
    _food = None

    _delay = None

    def __init__(self, size : int, is_loop : bool, is_dark : bool, is_god : bool):
        self._size = size
        self._is_god = is_god
        if is_god:
            self._is_loop = True
        else:
            self._is_loop = is_loop
        self._is_dark = is_dark
        self._delay = 0.1
        self._is_pause = False
        self._window = turtle.Screen()
        self._window.title(TITLE)
        if is_dark:
            self._window.bgcolor(BG_COLOR_DARK)
        else:
            self._window.bgcolor(BG_COLOR)
        self._window.setup(self._size * 20, self._size * 20)
        self._window.setworldcoordinates(0, 0, self._size * 20, self._size * 20)
        self._window.tracer(0)
        self._snake = Snake(self._size, self._is_loop, is_dark)
        self._food = Food(self._size, is_dark)
        self._score_board = ScoreBoard(self._size, is_dark)

    def _start(self):
        self._snake.spawn()
        self._food.spawn(self._snake.get_body_coordinates())
        self._bind_keys()

    def _exit(self):
        self._window.bye()

    def _bind_keys(self):
        self._window.listen()
        self._window.onkeypress(self._snake.go_up, 'w')
        self._window.onkeypress(self._snake.go_up, 'Up')

        self._window.onkeypress(self._snake.go_down, 's')
        self._window.onkeypress(self._snake.go_down, 'Down')

        self._window.onkeypress(self._snake.go_left, 'a')
        self._window.onkeypress(self._snake.go_left, 'Left')

        self._window.onkeypress(self._snake.go_right, 'd')
        self._window.onkeypress(self._snake.go_right, 'Right')

        self._window.onkeypress(self._exit, 'Escape')

        self._window.onkeypress(self._lose, 'r')

        self._window.onkeypress(self._win, 'q')

        self._window.onkeypress(self._cheat, 'c')

        self._window.onkeypress(self._pause, 'p')

    def _clean_screen(self):
        self._snake.clear_body()
        self._snake.spawn()
        self._food.spawn(self._snake.get_body_coordinates())
        self._score_board.clear_board()

    def _lose(self):
        for i in range(10):
            self._window.bgcolor(LOSE_COLOR)
            time.sleep(0.1)
            if self._is_dark:
                self._window.bgcolor(BG_COLOR_DARK)
            else:
                self._window.bgcolor(BG_COLOR)
            time.sleep(0.1)
        self._clean_screen()

    def _win(self):
        for i in range(10):
            self._window.bgcolor(WIN_COLOR)
            time.sleep(0.1)
            if self._is_dark:
                self._window.bgcolor(BG_COLOR_DARK)
            else:
                self._window.bgcolor(BG_COLOR)
            time.sleep(0.1)
        self._clean_screen()

    def _cheat(self):
        x, y = self._snake.get_coordinates()
        direction = self._snake.get_direction()
        if direction == 'up':
            self._food.cheat_spawn([x, y + 20])
        if direction == 'down':
            self._food.cheat_spawn([x, y - 20])
        if direction == 'left':
            self._food.cheat_spawn([x - 20, y])
        if direction == 'right':
            self._food.cheat_spawn([x + 20, y])

    def _pause(self):
        self._is_pause = not self._is_pause
        self._game_pause()
        self._snake.pause(self._is_pause)
        self._food.pause(self._is_pause)

    def _game_pause(self):
        if self._is_dark:
            pass
        else:
            if self._is_pause:
                self._window.bgcolor(BG_COLOR_PAUSE)
            else:
                self._window.bgcolor(BG_COLOR)

    def _get_score(self):
        self._food.spawn(self._snake.get_body_coordinates())
        self._snake.add_segment_of_body()
        self._score_board.increase_score()

    def run(self):
        self._start()
        while True:
            self._window.update()
            if self._is_pause:
                continue
            snake_x_pos, snake_y_pos = self._snake.get_coordinates()
            if (
                (
                    (
                        snake_x_pos > self._size * 20
                        or snake_x_pos < 0
                        or snake_y_pos > self._size * 20
                        or snake_y_pos < 0
                    ) and not self._is_loop
                    or self._snake.check_collision()
                ) and not self._is_god
            ):
                self._lose()
            food_x, food_y = self._food.get_coordinates()
            if self._snake.get_distance(food_x, food_y) < 20:
                self._get_score()
            if self._score_board.get_score() == self._size ** 2:
                self._win()
            self._snake.move_snake()
            self._snake.move()
            time.sleep(self._delay)
        self._window.mainloop()
