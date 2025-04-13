import curses
from ui.ui_state import UIState
import datetime

class IntegerMenuUi:
    def __init__(self, stdscr, name, getter, setter, limits):
        self.stdscr = stdscr
        self.name   = name
        self.getter = getter
        self.setter = setter
        self.limits = limits

        self.pad_height = 2
        self.pad_width = 200
        self.pad = curses.newpad(self.pad_height, self.pad_width)

    def ui(self):
        self.stdscr.clear()

        value = self.getter()

        def update_ui_state():
            stored_value = self.getter()
            if value != stored_value:
                self.setter(value)
                UIState.saveable = True

        def draw_menu():
            self.pad.addstr(0, 0, self.name)
            self.pad.addstr(1, 0, f'{value}', curses.A_REVERSE)
            self.pad.clrtoeol()

            menu_page_format(1)

        def menu_page_format(select_idx):
            h = min(self.pad_height, UIState.height) - 1
            w = min(self.pad_width,  UIState.width) - 1

            n_page = select_idx // UIState.height

            self.stdscr.clear()
            self.stdscr.refresh()
            self.pad.refresh(n_page * UIState.height,0, 0,0, h, w)

        last_key = None
        last_key_time = None
        interval = 1

        def key_held_down_check(c):
            nonlocal last_key, last_key_time, interval
            if last_key == c:
                if current_key_time > datetime.timedelta(seconds=0.1) + last_key_time:
                    # reset
                    interval = 1
                    last_key_time = current_key_time
                else: # key has been held down 
                    if last_key_time + datetime.timedelta(seconds=0.5) > current_key_time:
                        interval *= 1.2
                        interval = int(interval) + 1
                        last_key_time = current_key_time
            else:
                last_key = c
                last_key_time = current_key_time
                interval = 1

        while True:
            UIState.update_width_hight(self.stdscr)
            draw_menu()
            self.stdscr.refresh()

            c = self.stdscr.getch()
            current_key_time = datetime.datetime.now()

            if c == ord('q') or c in [curses.KEY_LEFT]:
                break
            elif c == curses.KEY_DOWN:
                key_held_down_check(c)
                value -= interval
                value = max(value, self.limits[0])
            elif c == curses.KEY_UP:
                key_held_down_check(c)
                value += interval
                value = min(value, self.limits[1])
            elif c in [curses.KEY_ENTER, 10, 13, 0x1cb]:
                update_ui_state()
                break;
            else:
                last_key = None
                interval = 1
        return True
