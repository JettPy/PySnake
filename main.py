import sys
from components.Game import Game

try:
    size = int(sys.argv[1])
except ValueError:
    print('Invalid parameter. Starting in default mode')
    size = 30

if size <= 0:
    print('Invalid parameter. Starting in default mode')
    size = 30

dark_mode = False

if len(sys.argv) == 3:
    if sys.argv[2] == 'd':
        dark_mode = True
    else:
        print('Invalid parametr. Use \"d\" for dark mode')

try:
    py_snake = Game(size, dark_mode)
    py_snake.run()
except Exception:
    pass
