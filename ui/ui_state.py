import curses
from pathlib import Path

from payload_lib.config_parser import Config
from payload_lib.uncompress_decoded_payload import Uncompressor
from payload_lib.item_parser import Parser as ItemParser
from payload_lib.items_to_bytes import Encoder
from payload_lib.bytes_to_compressed_payload import Compressor
from payload_lib.bar_rank import BarRank
from payload_lib.bar_stats import BarStats
from payload_lib.bar_tokens import BarTokens
from payload_lib.golden_keys import GoldenKeys
from payload_lib.fov import Fov

class Processer:
    def __init__(self, payload_file):
        self.original_profile = Path(payload_file)
        self.modified_profile = self.original_profile.parent / 'PAYLOAD.new'
        self._uncompress()
        #self.config = Config(config_file)

    def _uncompress(self):
        u = Uncompressor(self.original_profile)
        self._items = ItemParser(u.get()).get()
        self._fov = Fov(self._items)
        self._bar_rank = BarRank(self._items)
        self._bar_stats = BarStats(self._items)
        self._bar_tokens = BarTokens(self._items)
        self._golden_keys = GoldenKeys(self._items)

    def get_bar_stats(self):
        return self._bar_stats

    def get_golden_keys(self):
        return self._golden_keys

    def get_bar_rank(self):
        return self._bar_rank

    def get_bar_tokens(self):
        return self._bar_tokens

    def get_fov(self):
        return self._fov

    def save(self):
        e = Encoder()
        encoded = e.encode(self._items)

        c = Compressor(encoded)
        c.write_payload(self.modified_profile)


class UIState:

    ui_stack = []
    processor = None
    width = None
    height = None

    saveable = False

    @classmethod
    def save(cls):
        if cls.saveable == True:
            cls.processor.save()

            cls.saveable = False
                

    @classmethod
    def update_width_hight(cls, stdscr):
        curses.curs_set(0)
        cls.height, cls.width = stdscr.getmaxyx()

