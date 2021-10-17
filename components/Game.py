import sys
import time
import turtle
from components.Snake import Snake
from components.Food import Food


class Game:

    _size = None
    _font_size = None

    _window = None
    _score_board = None
    _snake = None
    _food = None

    _delay = 0.1
    _score = 0
    _high_score = 0

    def __init__(self, size : int):
        self._size = size
        if size >= 20:
            self._font_size = 24
        elif size >= 12:
            self._font_size = 12
        else:
            self._font_size = 9
        self._window = turtle.Screen()
        self._window.title('PySnake')
        self._window.bgcolor('honeydew')
        self._window.setup(width = self._size * 20 + 50, height = self._size * 20 + 50)
        self._window.tracer(0)

        self._snake = Snake(self._size)
        self._food = Food(self._size)

        self._create_score_board()
        self._update_score_board()

    def _create_score_board(self):
        self._score_board = turtle.Turtle()
        self._score_board.speed(0)
        self._score_board.shape('square')
        self._score_board.color('black')
        self._score_board.penup()
        self._score_board.hideturtle()
        self._score_board.goto(0, self._size * 10 - 20)

    def _start(self):
        self._snake.spawn()
        self._food.spawn()
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

    def _lose(self):
        self._window.bgcolor('orange')
        time.sleep(1)
        self._window.bgcolor('honeydew')
        self._snake.clear_body()
        self._snake.spawn()
        self._food.spawn()
        self._score = 0
        self._delay = 0.1
        self._score_board.clear()
        self._update_score_board()

    def _get_score(self):
        self._food.spawn()
        self._snake.add_segment_of_body()
        self._delay -= 0.001
        self._score += 1
        if self._score > self._high_score:
            self._high_score = self._score
        self._score_board.clear()
        self._update_score_board()

    def run(self):
        self._start()
        while True:
            self._window.update()
            snake_x_pos, snake_y_pos = self._snake.get_coordinates()
            if (
                snake_x_pos > self._size * 10
                or snake_x_pos < -self._size * 10
                or snake_y_pos > self._size * 10
                or snake_y_pos < -self._size * 10
            ):
                self._lose()
            food_x, food_y = self._food.get_coordinates()
            if self._snake.get_distance(food_x, food_y) < 20:
                self._get_score()
            self._snake.move_snake()
            self._snake.move()
            if self._snake.check_collision():
                self._lose()
            time.sleep(self._delay)
        self._window.mainloop()

    def _update_score_board(self):
        self._score_board.write(
            'score: {}  High score: {}'.format(self._score, self._high_score),
            align = 'center',
            font = ('consolas', self._font_size, 'normal'),
        )