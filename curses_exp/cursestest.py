# import curses
# from curses import wrapper
# 
# # def main(stdscr):
# #     stdscr.clear()
# #     for i in range(10):
# #         v=i-10
# #         stdscr.addstr(i,i,'10 divided by {} is {}'.format(v,10/v))
# #     stdscr.refresh()
# #     stdscr.getkey()
# # 
# # wrapper(main)
# def main(stdscr):
#     stdscr.clear()
#     stdscr.keypad(True)
#     curses.init_pair(1,curses.COLOR_RED,curses.COLOR_WHITE)
#     stdscr.addstr("Pretty text",curses.color_pair(1))
#     stdscr.refresh()
#     stdscr.getkey()
# 
# wrapper(main)
import curses
from curses.textpad import Textbox, rectangle

def main(stdscr):
    stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")

    editwin = curses.newwin(5,30, 2,1)
    rectangle(stdscr, 1,0, 1+5+1, 1+30+1)
    stdscr.refresh()

    box = Textbox(editwin)

    # Let the user edit until Ctrl-G is struck.
    box.edit()

    # Get resulting contents
    message = box.gather()

curses.wrapper(main)
