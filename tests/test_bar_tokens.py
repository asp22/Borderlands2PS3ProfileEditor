import pytest
from pathlib import Path
from payload_lib.bar_tokens import BarTokens
from payload_lib.uncompress_decoded_payload import Uncompressor
from payload_lib.item_parser import Parser

class TestBarTokens:
    payload_path = Path(r"tests\assets\PAYLOAD")

    def test_get_tokens_from_item(self):
        u = Uncompressor(self.payload_path)
        items = Parser(u.get()).get()
        token_item = None
        for i in items:
            if i.id == 138:
                token_item = i

        t = BarTokens(items)
        assert token_item == t.item
        assert t.get() == 112233

    def test_set_tokens(self):
        u = Uncompressor(self.payload_path)
        items = Parser(u.get()).get()
        token_item = None
        for i in items:
            if i.id == 138:
                token_item = i

        t = BarTokens(items)
        t.set(123)
        assert t.get() == 123
        assert token_item.get() == 123