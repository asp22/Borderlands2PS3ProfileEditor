import pytest
from pathlib import Path
from payload_lib.bar_stats import BarStats
from payload_lib.uncompress_decoded_payload import Uncompressor
from payload_lib.item_parser import Parser

class TestBarStats:
    payload_path = Path(r"tests\assets\PAYLOAD")

    def test_get_stats_from_item(self):
        u = Uncompressor(self.payload_path)
        items = Parser(u.get()).get()
        bar_item = None
        for i in items:
            if i.id == 143:
                bar_item = i

        b = BarStats(items)
        assert bar_item == b.item
        assert b.stats_as_pct() == [100000.0, 100000.0, 1.0, 100000.0, 100000.0, 100000.0, 100000.0, 100000.0, 1000.0, 100000.0, 1000.0, 100000.0, 100000.0, 100000.0 ]

    def test_update_stats(self):
        new_stats = [1.0 for i in range(0,14)]
        u = Uncompressor(self.payload_path)
        items = Parser(u.get()).get()
        bar_item = None
        for i in items:
            if i.id == 143:
                bar_item = i

        old_value = bar_item.get()

        b = BarStats(items)
        assert bar_item == b.item

        b.set_stats(new_stats)
        assert b.stats_as_pct() == new_stats
        assert old_value != b.item.get()

    def test_ignore_none(self):
        new_stats = [None for i in range(0,14)]
        u = Uncompressor(self.payload_path)
        items = Parser(u.get()).get()

        b = BarStats(items)
        old_stats = b.stats_as_pct()

        b.set_stats(new_stats)
        assert b.stats_as_pct() == old_stats