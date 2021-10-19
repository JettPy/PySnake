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
loop_mode = False
god_mode = False

if len(sys.argv) > 2:
    for i in range(2, len(sys.argv)):
        if sys.argv[i] == 'd':
            dark_mode = True
        elif sys.argv[i] == 'i':
            loop_mode = True
        elif sys.argv[i] == 'g':
            god_mode = True
        else:
            print('Invalid parametr. Use \"d\" for dark mode or \"i\" for loop mode or \"g\" for god mode')

try:
    py_snake = Game(size, loop_mode, dark_mode, god_mode)
    py_snake.run()
except Exception:
    pass
