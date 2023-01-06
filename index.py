import curses
import curses.textpad


def init_curses():
    # Initialisieren
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    stdscr.bkgd(curses.color_pair(1))
    stdscr.refresh()
    return stdscr


def refresh_windows():
    for win in windows:
        win.refresh()


# Init
stdscr = init_curses()
maxy, maxx = stdscr.getmaxyx()
windows = []

# Darstellungsfenster Rand
display_border_win = curses.newwin(maxy - 3, maxx, 0, 0)
display_border_win.bkgd(curses.color_pair(1))
display_border_win.border()
display_border_win.addstr(0, 2, 'Dialogue')
windows.append(display_border_win)

# Darstellungsfenster Inhalt
display_win = curses.newwin(maxy - 5, maxx - 2, 1, 1)
display_win.bkgd(curses.color_pair(1))
windows.append(display_win)

# Edit-Fenster Rand
input_border_win = curses.newwin(3, maxx, maxy - 3, 0)
input_border_win.bkgd(curses.color_pair(2))
input_border_win.border()
input_border_win.addstr(0, 2, 'Message')
windows.append(input_border_win)

# Edit-Fenster Box
input_win = curses.newwin(1, maxx - 2, maxy - 2, 1)
input_win.bkgd(curses.color_pair(2))
windows.append(input_win)

# Textbox
textbox = curses.textpad.Textbox(input_win)

refresh_windows()
i = 0
while True:
    text = textbox.edit()

    # Text übernehmen
    display_win.addstr(i, 0, '[USER] ' + text + '\n')
    i += 1

    input_win.clear()
    refresh_windows()

# Ende
curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()
