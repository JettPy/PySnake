import turtle


class Snake:

    _size = None
    _head = None
    _body = []

    def __init__(self, size : int):
        self._size = size
        self._head = turtle.Turtle()
        self._head.speed(0)
        self._head.shape('square')
        self._head.color('darkseagreen')
        self._head.penup()

    def spawn(self):
        self._head.goto(0, 0)
        self._head.direction = 'stop'

    def go_up(self):
        if self._head.direction != 'down':
            self._head.direction = 'up'

    def go_down(self):
        if self._head.direction != 'up':
            self._head.direction = 'down'

    def go_left(self):
        if self._head.direction != 'right':
            self._head.direction = 'left'

    def go_right(self):
        if self._head.direction != 'left':
            self._head.direction = 'right'

    def move(self):
        if self._head.direction == 'up':
            y = self._head.ycor()
            self._head.sety(y + 20)
        if self._head.direction == 'down':
            y = self._head.ycor()
            self._head.sety(y - 20)
        if self._head.direction == 'left':
            x = self._head.xcor()
            self._head.setx(x - 20)
        if self._head.direction == 'right':
            x = self._head.xcor()
            self._head.setx(x + 20)

    def get_coordinates(self):
        return self._head.xcor(), self._head.ycor()

    def get_distance(self, x: int, y: int):
        return self._head.distance(x, y)

    def clear_body(self):
        for segment in self._body:
            segment.goto(10000, 10000)
        self._body.clear()

    def add_segment_of_body(self):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('palegreen')
        new_segment.penup()
        self._body.append(new_segment)

    def move_snake(self):
        for i in range(len(self._body) - 1, 0, -1):
            x = self._body[i - 1].xcor()
            y = self._body[i - 1].ycor()
            self._body[i].goto(x, y)
        if len(self._body) > 0:
            x = self._head.xcor()
            y = self._head.ycor()
            self._body[0].goto(x, y)

    def check_collision(self):
        collision = False
        for segment in self._body:
            if segment.distance(self._head) < 20:
                collision = True
        return collision
