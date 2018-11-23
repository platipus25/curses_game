import curses
from time import sleep
import random

stage = 1
window = curses.initscr()
curses.cbreak() # react to keys instantly, without requiring the Enter key to be pressed
curses.noecho()
window.clear()
#window.addstr("!")
window.timeout(-1)

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class sprite:
    def __init__(self, win, char="!"):
        size = win.getmaxyx()
        self.x = int(size[1]/2)
        self.y = int(size[0]/2)
        self.char = char
        self.win = win
    def add(self, x=0, y=0):
        self.x+=x
        self.y+=y
        self.draw()
    def draw(self):
        self.win.addstr(self.y, self.x, self.char, curses.COLOR_CYAN)#"X:{} Y:{}  {}".format(str(self.x),str(self.y), self.char))
        self.win.refresh()

sprite = sprite(window)
sprite.draw()

size = window.getmaxyx()
size_y = size[0]
size_x = size[1]
rand_x = random.randint(2, size_x-2)
rand_y = random.randint(2, size_y-2)

while True:
    window.clear()
    sprite.draw()

    #window size
    size = window.getmaxyx()
    size_y = size[0]
    size_x = size[1]
    #rand_x = random.randint(2, size_x-2)
    #rand_y = random.randint(2, size_y-2)


    window.addstr(rand_y, rand_x, "*", curses.A_BLINK)


    window.addstr(3,3, "stage {}".format(stage))
    if (sprite.y, sprite.x) == (rand_y, rand_x):
        window.addstr(3,3, "stage {} complete".format(stage), curses.A_BLINK)
        rand_x = random.randint(2, size_x-2)
        rand_y = random.randint(2, size_y-2)
        stage+=1
        sprite.x = int(size_x/2)
        sprite.y = int(size_y/2)
        sprite.draw()

    #moving sprite
    charles = ord(window.getkey())
    if(charles == 65):
        sprite.add(0, -1)
    if(charles == 66):
        sprite.add(0, 1)
    if(charles == 67):
        sprite.add(1)
    if(charles == 68):
        sprite.add(-1)

    #exit
    if charles == 113:
        window.refresh()
        curses.echo()
        curses.nocbreak()
        #curses.keypad(False)
        curses.endwin()
        break;
