import sys

# Game Rules
COLUMNS = 15
ROWS = 15
CHECKERS = 12
GOAL = 4

# Logging
ALGO_LOGFILE = 'algo.log'

# Design
FIELD_BACKGROUND = 'grey'
COORDINATES = False
MENU_WIDTH = 15
MENU_BACKGROUND = 'red'
QUIT_BG = 'white'
QUIT_FG = 'gold'
QUIT_HEIGHT = 3
QUIT_PADY = 10
CALCULATE_BG = 'green3'
CALCULATE_HIGHT = 10
RESET_BG = 'yellow2'
DRAW_CLEAR_BG = 'CadetBlue1'
DB_HEIGHT = 1
DB_WIDTH = 1
DB_PAD = 3
if sys.platform == 'win32':
    DB_WIDTH *= 2
