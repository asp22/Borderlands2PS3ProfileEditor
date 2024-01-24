import argparse
from pathlib import Path
from payload_lib.config_parser import Config
from payload_lib.uncompress_decoded_payload import Uncompressor
from payload_lib.item_parser import Parser as ItemParser
from payload_lib.items_to_bytes import Encoder
from payload_lib.bytes_to_compressed_payload import Compressor
from payload_lib.bar_rank import BarRank
from payload_lib.bar_stats import BarStats
from payload_lib.bar_tokens import BarTokens
from payload_lib.golden_keys import GoldenKeys
from payload_lib.fov import Fov

def make_argparse():
    parser = argparse.ArgumentParser(prog="PS3 Borderlands2 Profile Updater",
                                     description="Allows you to update parts of the PAYLOAD file.",
                                     epilog='!!! Please first decrypt PAYLOAD using Bruteforce Save Data before using this tool !!!')

    parser.add_argument('-c', '--config', required=True, help="config file")
    parser.add_argument('-p', '--payload', required=True, help="PAYLOAD file")
    return parser

class Processer:
    def __init__(self, config_file, payload_file):
        self.original_profile = Path(payload_file)
        self.modified_profile = self.original_profile.parent / 'PAYLOAD.new'
        self.config = Config(config_file)

    def process(self):
        u = Uncompressor(self.original_profile)
        items = ItemParser(u.get()).get()

        fov = Fov(items)
        bar_rank = BarRank(items)
        bar_stats = BarStats(items)
        bar_tokens = BarTokens(items)
        golden_keys = GoldenKeys(items)

        x = self.config.requested_fov()  
        if x is not None:
            fov.set(x)

        x = self.config.requested_bar_rank()
        if x is not None:
            bar_rank.set(x)

        x = self.config.requested_bar_tokens()
        if x is not None:
            bar_tokens.set(x)

        x = self.config.requested_golden_keys()
        if x is not None:
            golden_keys.set(x)

        x = self.config.requested_bar_stats()
        bar_stats.set_stats(x)

        e = Encoder()
        encoded = e.encode(items)

        c = Compressor(encoded)
        c.write_payload(self.modified_profile)

if __name__ == "__main__":
    parser = make_argparse()
    args = parser.parse_args()
    p = Processer(args.config, args.payload)
    p.process()