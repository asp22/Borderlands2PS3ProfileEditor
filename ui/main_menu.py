import curses
from tkinter import W
from ui.ui_state import UIState
from ui.bar_stats_menu import BarStatsMenuUi
from ui.integer_menu import IntegerMenuUi

class MainMenuUI:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.menu_current_idx = 0
        self.max_menu_current_idx = 5 # todo len(UIState.hero_sd_views) + 1

        self.pad_height = self.max_menu_current_idx + 1
        self.pad_width = 200
        self.pad = curses.newpad(self.pad_height, self.pad_width)

    def ui(self):

        self.stdscr.clear()

        def draw_menu(select_idx):
            self.pad.addstr(0, 0, 'BarStats',  curses.A_REVERSE if select_idx == 0 else curses.A_NORMAL)
            self.pad.addstr(1, 0, f'GoldenKeys: {UIState.processor.get_golden_keys().get()}', curses.A_REVERSE if select_idx == 1 else curses.A_NORMAL)
            self.pad.clrtoeol()
            self.pad.addstr(2, 0, f'BarRank   : {UIState.processor.get_bar_rank().get()}', curses.A_REVERSE if select_idx == 2 else curses.A_NORMAL)
            self.pad.clrtoeol()
            self.pad.addstr(3, 0, f'BarTokens : {UIState.processor.get_bar_tokens().get()}', curses.A_REVERSE if select_idx == 3 else curses.A_NORMAL)
            self.pad.clrtoeol()
            self.pad.addstr(4, 0, f'FOV       : {UIState.processor.get_fov().get()}', curses.A_REVERSE if select_idx == 4 else curses.A_NORMAL)
            self.pad.clrtoeol()
            self.pad.addstr(5, 0, f'Saveable  : {UIState.saveable}', curses.A_REVERSE if select_idx == 5 else curses.A_NORMAL)
            self.pad.clrtoeol()

            menu_page_format(select_idx)

        def menu_page_format(select_idx):
            h = min(self.pad_height, UIState.height) - 1
            w = min(self.pad_width,  UIState.width) - 1

            n_page = select_idx // UIState.height

            self.stdscr.clear()
            self.stdscr.refresh()
            self.pad.refresh(n_page * UIState.height,0, 0,0, h, w)

        def update_ui_state():
            if self.menu_current_idx == 0:
                UIState.ui_stack.append(BarStatsMenuUi(self.stdscr))
            elif self.menu_current_idx == 1:
                def setter(value):
                    UIState.processor.get_golden_keys().set(value)
                def getter():
                    return UIState.processor.get_golden_keys().get()
                UIState.ui_stack.append(IntegerMenuUi(self.stdscr, 'Golden Keys', getter, setter, [0,255*3]))
            elif self.menu_current_idx == 2:
                def setter(value):
                    UIState.processor.get_bar_rank().set(value)
                def getter():
                    return UIState.processor.get_bar_rank().get()
                UIState.ui_stack.append(IntegerMenuUi(self.stdscr, 'Bar Rank', getter, setter, [0,0x7fffffff]))
            elif self.menu_current_idx == 3:
                def setter(value):
                    UIState.processor.get_bar_tokens().set(value)
                def getter():
                    return UIState.processor.get_bar_tokens().get()
                UIState.ui_stack.append(IntegerMenuUi(self.stdscr, 'Bar Tokens', getter, setter, [0,0x7fffffff]))
            elif self.menu_current_idx == 4:
                def setter(value):
                    UIState.processor.get_fov().set(value)
                def getter():
                    return UIState.processor.get_fov().get()
                UIState.ui_stack.append(IntegerMenuUi(self.stdscr, 'FOV', getter, setter, [10,180]))

            elif self.menu_current_idx == self.max_menu_current_idx:
                if UIState.saveable:
                    UIState.save()

        while True:
            UIState.update_width_hight(self.stdscr)
            self.stdscr.refresh()
            draw_menu(self.menu_current_idx)

            c = self.stdscr.getch()
            if c == ord('q'):
                break
            elif c == curses.KEY_DOWN and self.menu_current_idx < self.max_menu_current_idx:
                self.menu_current_idx += 1
            elif c == curses.KEY_UP and self.menu_current_idx > 0:
                self.menu_current_idx -= 1
            elif c in [curses.KEY_RIGHT, curses.KEY_ENTER, 10, 13, 0x1cb]:
                update_ui_state()
                return False
            #else:
            #    self.stdscr.addstr(21, 0, "Key pressed: {}            ".format(hex(c)))

        return True
