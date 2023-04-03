import os
import curses


def select_option(stdscr, options):
    """
    Display a list of options to the user and capture arrow key input
    to select an option. Returns the index of the selected option.
    """
    current_row = 0
    stdscr.clear()
    while True:
        for i, option in enumerate(options):
            x = 2
            y = i + 1
            if i == current_row:
                stdscr.addstr(y, x, "> " + option, curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, "  " + option)
        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(options) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return current_row


def load_input(stdscr):
    path = os.path.join(os.getcwd(), "videos")
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    # Select an option from the list
    options = files
    option_index = select_option(stdscr, options)
    selected_option = options[option_index]

    stdscr.clear()
    stdscr.addstr(0, 0, "Selected option: {}".format(selected_option))
    stdscr.addstr(1, 0, "Name: ")

    curses.echo()
    name = stdscr.getstr(1, 6, 50).decode("utf-8")

    stdscr.addstr(2, 0, "Zoom link: ")
    zoom_link = stdscr.getstr(2, 11, 200).decode("utf-8")

    return selected_option, name, zoom_link
