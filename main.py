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
    
py_snake = Game(size)
py_snake.run()
