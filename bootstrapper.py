import curses
import random
import time
from os import system as system
import os
import locale
import ctypes
locale.setlocale(locale.LC_ALL, '')

ctypes.windll.kernel32.SetConsoleTitleW("Cicada - Loading")


def src(stdscr):
    if os.path.exists('src.exe'):
        system('start src.exe')
    else:
        system('start src.py')

def matrix_screen(stdscr):
    # Initialize colors
    
    # Clear screen and hide cursor
    stdscr.clear()
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(50)

    sh, sw = stdscr.getmaxyx()
    w = sw // 2
    chars = "0101"
    drops = [0] * w

    start_time = time.time()

    while True:
        stdscr.clear()

        for i in range(w):
            if drops[i] == sh or (drops[i] > 0 and random.random() > 0.95):
                drops[i] = 0
            char = random.choice(chars)
            stdscr.addstr(drops[i], i * 2, char, curses.color_pair(1))
            drops[i] += 1

        stdscr.refresh()
        time.sleep(0.015)

        elapsed_time = time.time() - start_time
        if elapsed_time > 5:
            src(stdscr)
            break

def load():
    curses.wrapper(matrix_screen)

if __name__ == "__main__":
    load()
