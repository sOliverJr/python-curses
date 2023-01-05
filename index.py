import curses
import curses.textpad

# Initialisieren
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLUE)
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
stdscr.bkgd(curses.color_pair(1))
maxy, maxx = stdscr.getmaxyx()
stdscr.refresh()

# Edit-Fenster Rand
win1 = curses.newwin(3, maxx, maxy - 3, 0)
win1.bkgd(curses.color_pair(2))
win1.border()
win1.refresh()

# Edit-Fenster box
win3 = curses.newwin(1, maxx, maxy - 2, 1)
win3.bkgd(curses.color_pair(2))

# Darstellungsfenster
win2 = curses.newwin(maxy - 3, maxx, 0, 0)
win2.bkgd(curses.color_pair(1))
win2.border()

win2.refresh()

# Textbox
textbox = curses.textpad.Textbox(win3)

i = 1
while True:
    text = textbox.edit()

    # Text übernehmen
    win2.addstr(i, 1, '[USER] ' + text + '\n')
    i += 1
    win2.refresh()

    win3.clear()
    win3.refresh()

# Ende
c = stdscr.getch()
curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()
