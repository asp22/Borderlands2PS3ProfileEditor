import pytest
from payload_lib.string_to_list import Decoder

class TestDecoder:

    def test_bar_string(self):
        text = "S65AYQ6VM8SZTCBAPS6KDAMWFDP9HJZNS65AYQ6VM8SZTCK25ZBKD952ACP9HJZNSPM2156VM8SZTCK25ZBKDAMWF5"
        expected = [4641589, 4641589, 1, 4641589, 4641589, 4641589, 4641589, 4641589, 10000, 4641589, 10000, 4641589, 4641589, 4641589]
        d = Decoder()
        assert expected == d.decode(text)

    def test_next_bar_string(self):
        text = "SPMC3C6VJJDWSCBAP17KD9S6JCP55VCJ"
        expected = [2, 4, 6, 8, 9]
        d = Decoder()
        assert expected == d.decode(text)