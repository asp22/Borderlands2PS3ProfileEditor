import pytest
from pathlib import Path
from payload_lib.golden_keys import GoldenKeys
from payload_lib.uncompress_decoded_payload import Uncompressor
from payload_lib.item_parser import Parser

class TestGoldenKeys:
    payload_path = Path(r"tests\assets\PAYLOAD")

    def test_get_keys_from_item(self):
        u = Uncompressor(self.payload_path)
        items = Parser(u.get()).get()
        golden_key_item = None
        for i in items:
            if i.id == 162:
                golden_key_item = i

        g = GoldenKeys(items)
        assert golden_key_item == g.item
        assert g.get() == 12

    def test_set_golden_keys(self):
        u = Uncompressor(self.payload_path)
        items = Parser(u.get()).get()
        golden_key_item = None
        for i in items:
            if i.id == 162:
                golden_key_item = i

        old_bytes = golden_key_item.get()

        g = GoldenKeys(items)
        assert golden_key_item == g.item
        g.set(255)
        assert g.get() == 255
        assert g.item.get() != old_bytes

    def test_set_golden_keys2(self):
        u = Uncompressor(self.payload_path)
        items = Parser(u.get()).get()
        golden_key_item = None
        for i in items:
            if i.id == 162:
                golden_key_item = i

        old_bytes = golden_key_item.get()

        g = GoldenKeys(items)
        assert golden_key_item == g.item
        g.set(644)
        assert g.get() == 644
        assert g.item.get() != old_bytes
