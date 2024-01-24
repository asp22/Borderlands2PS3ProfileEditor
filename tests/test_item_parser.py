import pytest
from pathlib import Path
from payload_lib.item_parser import Parser
from payload_lib.uncompress_decoded_payload import Uncompressor
from payload_lib.item import ItemString, ItemBinary

class TestParser:
    payload_path = Path(r".\tests\assets\PAYLOAD")

    def test_item_count(self):
        u = Uncompressor(self.payload_path)
        p = Parser(u.uncompressed_bytes)
        items = p.get()
        assert len(items) == 66

    def test_bar_item(self):
        u = Uncompressor(self.payload_path)
        p = Parser(u.uncompressed_bytes)
        items = p.get()
        bar_item = None
        for i in items:
            if i.id == 143:
                bar_item = i
                break

        assert bar_item is not None
        assert type(bar_item) == ItemString
        assert bar_item.get() == "S65AYQ6VM8SZTCBAPS6KDAMWFDP9HJZNS65AYQ6VM8SZTCK25ZBKD952ACP9HJZNSPM2156VM8SZTCK25ZBKDAMWF5"

    def test_golden_keys(self):
        u = Uncompressor(self.payload_path)
        p = Parser(u.uncompressed_bytes)
        items = p.get()
        golden_item = None
        for i in items:
            if i.id == 162:
                golden_item = i
                break

        assert golden_item is not None
        assert type(golden_item) == ItemBinary
        assert golden_item.get() == b"\x00\x09\x00\xad\x0a\x08\xfe\x01\x00"

