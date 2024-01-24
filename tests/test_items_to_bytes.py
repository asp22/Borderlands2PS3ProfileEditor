import pytest
from pathlib import Path
from payload_lib.items_to_bytes import Encoder
from payload_lib.uncompress_decoded_payload import Uncompressor
from payload_lib.item_parser import Parser

class TestEncoder:
    payload_path = Path(r"tests\assets\PAYLOAD")

    def test_to_bytes(self):
        u = Uncompressor(self.payload_path)
        items = Parser(u.get()).get()
        encoder = Encoder()
        encoded = encoder.encode(items)
        assert encoded == u.uncompressed_bytes