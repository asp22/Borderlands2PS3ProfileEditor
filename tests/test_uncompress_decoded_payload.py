import pytest
from pathlib import Path
from payload_lib.uncompress_decoded_payload import Uncompressor

class TestUncompressor:
    payload_path = Path(r"tests\assets\PAYLOAD")
    expected_sha1 = Path(r"tests\expected\sha1")
    expected_length = Path(r"tests\expected\length")
    expected_compressed_bytes = Path(r"tests\expected\compressed_bytes")
    expected_uncompressed_bytes = Path(r"tests\expected\uncompressed_bytes")

    @staticmethod
    def filebytes(file):
        with open(file, 'rb') as f:
            return f.read()

    def test_sha1(self):
        u = Uncompressor(self.payload_path)
        assert u.sha1 == TestUncompressor.filebytes(self.expected_sha1)

    def test_length(self):
        u = Uncompressor(self.payload_path)
        assert u.uncompressed_length_bytes == TestUncompressor.filebytes(self.expected_length)
        assert int.from_bytes(u.uncompressed_length_bytes) == u.uncompressed_length

    def test_compressed_bytes(self):
        u = Uncompressor(self.payload_path)
        assert u.compressed_bytes == TestUncompressor.filebytes(self.expected_compressed_bytes)

    def test_uncompressed_bytes(self):
        u = Uncompressor(self.payload_path)
        assert u.uncompressed_bytes == TestUncompressor.filebytes(self.expected_uncompressed_bytes)
        assert u.uncompressed_length == len(TestUncompressor.filebytes(self.expected_uncompressed_bytes))
        assert u.get() == u.uncompressed_bytes