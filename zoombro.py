import curses
import argparse
from src import input_service, zoom_service


def zoombro(stdscr):
    parser = argparse.ArgumentParser()
    parser.add_argument("--show", action="store_true", help="run in non-headless mode")
    args = parser.parse_args()

    selected_option, name, zoom_link = input_service.load_input(stdscr)

    zoom_service.join_zoom_call(zoom_link, name, selected_option, stdscr, headless=not args.show)


curses.wrapper(zoombro)
