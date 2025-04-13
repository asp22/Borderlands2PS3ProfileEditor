import curses
import argparse
from pathlib import Path
from ui.ui_state import UIState, Processer
from ui.main_menu import MainMenuUI

def make_argparse():
    parser = argparse.ArgumentParser(prog="PS3 Borderlands2 Profile Updater",
                                     description="Allows you to update parts of the PAYLOAD file.",
                                     epilog='!!! Please first decrypt PAYLOAD using Bruteforce Save Data before using this tool !!!')

    #parser.add_argument('-c', '--config', required=True, help="config file")
    parser.add_argument('-p', '--payload', required=True, help="PAYLOAD file")
    return parser

def make_ui(payload_filename):

    def ui(stdscr):
        stdscr.clear()
        stdscr.refresh()
        UIState.payload_filename = payload_filename
        UIState.ui_stack.append(MainMenuUI(stdscr))

        UIState.processor = Processer(payload_filename)


        while len(UIState.ui_stack):
            res = UIState.ui_stack[-1].ui()
            if res:
                UIState.ui_stack.pop()

    return ui



if __name__ == "__main__":
    parser = make_argparse()
    args = parser.parse_args()

    ui = make_ui(Path(args.payload))

    curses.wrapper(ui)
