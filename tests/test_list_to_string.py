import pytest
from payload_lib.list_to_string import Encoder

class TestEncoder:
    
    def test_bar_to_string(self):
        stats = [4641589, 4641589, 1, 4641589, 4641589, 4641589, 4641589, 4641589, 10000, 4641589, 10000, 4641589, 4641589, 4641589]
        expected = "S65AYQ6VM8SZTCBAPS6KDAMWFDP9HJZNS65AYQ6VM8SZTCK25ZBKD952ACP9HJZNSPM2156VM8SZTCK25ZBKDAMWF5"
        e = Encoder()
        assert expected == e.encode(stats)

    def test_next_stats_to_string(self):
        stats = [2, 4, 6, 8, 9]
        expected = "SPMC3C6VJJDWSCBAP17KD9S6JCP55VCJ"
        e = Encoder()
        assert expected == e.encode(stats)