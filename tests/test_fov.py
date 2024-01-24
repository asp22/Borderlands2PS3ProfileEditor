import pytest
from pathlib import Path
from payload_lib.fov import Fov
from payload_lib.uncompress_decoded_payload import Uncompressor
from payload_lib.item_parser import Parser

class TestBarTokens:
    payload_path = Path(r"tests\assets\PAYLOAD")

    def test_get_fov_from_item(self):
        u = Uncompressor(self.payload_path)
        items = Parser(u.get()).get()
        fov_item = None
        for i in items:
            if i.id == 129:
                fov_item = i

        f = Fov(items)
        assert fov_item == f.item
        assert f.get() == 70

    def test_set_fov(self):
        u = Uncompressor(self.payload_path)
        items = Parser(u.get()).get()
        fov_item = None
        for i in items:
            if i.id == 129:
                fov_item = i

        f = Fov(items)
        f.set(110)
        assert f.get() == 110
        assert fov_item.get() == 110