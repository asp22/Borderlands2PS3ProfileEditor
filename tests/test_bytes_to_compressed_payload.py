import pytest
from pathlib import Path
from payload_lib.bytes_to_compressed_payload import Compressor
from payload_lib.items_to_bytes import Encoder
from payload_lib.uncompress_decoded_payload import Uncompressor
from payload_lib.item_parser import Parser

class TestCompressor:
    payload_path = Path(r"tests\assets\PAYLOAD")

    @staticmethod
    def filebytes(file):
        with open(file, 'rb') as f:
            return f.read()

    def test_to_bytes(self):
        u = Uncompressor(self.payload_path)
        items = Parser(u.get()).get()
        encoder = Encoder()
        encoded = encoder.encode(items)

        c = Compressor(encoded)
        assert c.get() == TestCompressor.filebytes(self.payload_path)