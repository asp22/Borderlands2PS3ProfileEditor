import pytest
from payload_lib.config_parser import Config
import tempfile
import os

class TestConfig:
    def test_parse_bar_stats(self):
        # make bar config
        fd, filename = tempfile.mkstemp()
        try:
            with open(filename, 'w') as f:
                f.write("""
[BarStats]
MaxHealth   = 100.0
ShieldCap   = 100.0
ShieldRate  = 100.0
#ShieldDelay = 1.0
MeleeDamage = 100.0 
GrenadeDmg  = 100.0
GunAcc      = 100.0
GunDmg      = 100.0
FireRate    = 100.0
Recoil      = 100.0
#Reload      = 1.0
ElemChance  = 100.0
ElemDmg     = 100.0
Crit        = 100.0
""")
            c = Config(filename)
            stats = c.requested_bar_stats()
            expected = [100.0, 100.0, 100.0, None, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, None, 100.0, 100.0, 100.0 ]
            assert stats == expected
        finally:
            os.close(fd)

    def test_parse_golden_keys_count_missing(self):
        fd, filename = tempfile.mkstemp()
        try:
            with open(filename, 'w') as f:
                f.write("""
[GoldenKeys]
""")
            c = Config(filename)
            assert None == c.requested_golden_keys()
        finally:
            os.close(fd)

    def test_parse_golden_keys_count(self):
        fd, filename = tempfile.mkstemp()
        try:
            with open(filename, 'w') as f:
                f.write("""
[GoldenKeys]
count = 4
""")
            c = Config(filename)
            assert 4 == c.requested_golden_keys()
        finally:
            os.close(fd)

            
    def test_parse_bar_rank_value_missing(self):
        fd, filename = tempfile.mkstemp()
        try:
            with open(filename, 'w') as f:
                f.write("""
[BarRank]
""")
            c = Config(filename)
            assert None == c.requested_bar_rank()
        finally:
            os.close(fd)

    def test_parse_bar_rank_value(self):
        fd, filename = tempfile.mkstemp()
        try:
            with open(filename, 'w') as f:
                f.write("""
[BarRank]
value = 40
""")
            c = Config(filename)
            assert 40 == c.requested_bar_rank()
        finally:
            os.close(fd)

    def test_parse_bar_tokens_count_missing(self):
        fd, filename = tempfile.mkstemp()
        try:
            with open(filename, 'w') as f:
                f.write("""
[BarTokens]
""")
            c = Config(filename)
            assert None == c.requested_bar_tokens()
        finally:
            os.close(fd)

    def test_parse_bar_tokens_count(self):
        fd, filename = tempfile.mkstemp()
        try:
            with open(filename, 'w') as f:
                f.write("""
[BarTokens]
count = 400
""")
            c = Config(filename)
            assert 400 == c.requested_bar_tokens()
        finally:
            os.close(fd)

    def test_parse_fov_value_missing(self):
        fd, filename = tempfile.mkstemp()
        try:
            with open(filename, 'w') as f:
                f.write("""
[FOV]
""")
            c = Config(filename)
            assert None == c.requested_fov()
        finally:
            os.close(fd)

    def test_parse_fov_value_count(self):
        fd, filename = tempfile.mkstemp()
        try:
            with open(filename, 'w') as f:
                f.write("""
[FOV]
value = 70
""")
            c = Config(filename)
            assert 70 == c.requested_fov()
        finally:
            os.close(fd)

    def test_parse_empty(self):
        # make bar config
        fd, filename = tempfile.mkstemp()
        try:
            c = Config(filename)
            stats = c.requested_bar_stats()
            expected = [None for i in range(0,14)]
            assert stats == expected
            assert None == c.requested_golden_keys()
            assert None == c.requested_bar_rank()
            assert None == c.requested_bar_tokens()
            assert None == c.requested_fov()
        finally:
            os.close(fd)