import curses
from ui.ui_state import UIState
from ui.stats_menu import StatsMenuUi

class BarStatsMenuUi:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.menu_current_idx = 0
        self.max_menu_current_idx = 13
        self.bar_stats = UIState.processor.get_bar_stats()

        self.names = ['Max Health',
          'Shield Capacity',
          'Shield Recharge Rate',
          'Shield Recharge Delay',
          'Melee Damage',
          'Grenade Damage',
          'Gun Accuracy',
          'Gun Damage',
          'Fire Rate',
          'Recoil Reduction',
          'Reload Rate',
          'Elemental Chance',
          'Elemental Damage',
          'Critical Damage']

        self.pad_height = self.max_menu_current_idx + 1
        self.pad_width = 200
        self.pad = curses.newpad(self.pad_height, self.pad_width)

    def ui(self):

        self.stdscr.clear()

        def draw_menu(select_idx):
            stats = self.bar_stats.stat_points
            pct = self.bar_stats.stats_as_pct()

            # covert to strs
            stats = [f'{i:>10}' for i in stats]
            pct   = [f'{i:>10}' for i in pct]

            for i in range(13):
                self.pad.addstr(i, 0, f'{self.names[i]:<25}: {stats[i]}, {pct[i]} %',curses.A_REVERSE if select_idx == i else curses.A_NORMAL)
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
            def _update(name, idx):
                def setter(points):
                    self.bar_stats.stat_points[idx] = points
                def getter():
                    return self.bar_stats.stat_points[idx]
                UIState.ui_stack.append(StatsMenuUi(self.stdscr, name, getter, setter, [0, 0x7fffffff]))

            _update(self.names[self.menu_current_idx], self.menu_current_idx)

        while True:
            UIState.update_width_hight(self.stdscr)
            self.stdscr.refresh()
            draw_menu(self.menu_current_idx)

            c = self.stdscr.getch()
            if c == ord('q') or c in [curses.KEY_LEFT]:
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
