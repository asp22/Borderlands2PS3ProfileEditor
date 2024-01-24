
# Takes an array of Items and
# converts this back to bytes (decompressed_bytes)
class Encoder:
    def __init__(self):
        pass

    def encode(self, items):
        bytes = b""

        # add size as uint32
        length = len(items).to_bytes(4)
        bytes += length

        for i in items:
            bytes += i.bytes()

        return bytes