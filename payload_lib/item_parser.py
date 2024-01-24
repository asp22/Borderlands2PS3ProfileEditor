from payload_lib.item import *

# This processes uncompressed bytes, from uncompress_decoded_payload
# and creates and adds Items to a list
class Parser:
    def __init__(self, uncompressed_bytes):
        self.data = uncompressed_bytes
        self.n_items = int.from_bytes(uncompressed_bytes[0:4])
        self._handlers = {
                1 : ItemInt32,
                4 : ItemString,
                5 : ItemFloat,
                6 : ItemBinary,
                8 : ItemInt8
            }
        self.items = self._read_items()

    def _read_items(self):
        items = []
        offset = 4 # read beyond count
        rem = len(self.data) - 4
        while rem > 0:
            data_type = self.data[offset+5]
            item_type = self._handlers[data_type]
            items.append(item_type(self.data, offset))
            next_offset = items[-1].next_offset

            read_size = next_offset - offset

            rem -= read_size
            offset = next_offset

        assert self.n_items == len(items)
        return items

    def get(self):
        return self.items

    def __str__(self):
        out = f"n_items:{self.n_items}\n"
        for i in self.items:
            out += f'{i}\n'
        return out