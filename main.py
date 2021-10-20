import sys
from components.Game import Game

dark_mode = False
loop_mode = False
god_mode = False
first_time = True
size = 30

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        if sys.argv[i].isdigit() and first_time:
            if int(sys.argv[i]) > 0:
                size = int(sys.argv[i])
                first_time = False
        elif sys.argv[i] == 'd':
            dark_mode = True
        elif sys.argv[i] == 'i':
            loop_mode = True
        elif sys.argv[i] == 'g':
            god_mode = True
        else:
            print('Invalid parametr. Use natural numerals for the field size, \"d\" for dark mode, \"i\" for loop mode or \"g\" for god mode')

if size > 45:
    print('Size is too large')
    size = 30

try:
    py_snake = Game(size, loop_mode, dark_mode, god_mode)
    py_snake.run()
except Exception:
    pass
