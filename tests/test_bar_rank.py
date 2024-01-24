import pytest
from pathlib import Path
from payload_lib.bar_rank import BarRank
from payload_lib.uncompress_decoded_payload import Uncompressor
from payload_lib.item_parser import Parser

class TestBarRank:
    payload_path = Path(r"tests\assets\PAYLOAD")

    def test_get_bar_rank_from_items(self):
        u = Uncompressor(self.payload_path)
        items = Parser(u.get()).get()

        r = BarRank(items)
        assert r.get() == 20431

    def test_set_bar_rank(self):
        u = Uncompressor(self.payload_path)
        items = Parser(u.get()).get()

        r = BarRank(items)
        r.set(1)
        assert r.get() == 1
