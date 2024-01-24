import ctypes
import struct

# takes a string and turns it into 
# a list of ints
class Decoder:
    def __init__(self):
        self.magic = 0x9A3652D9
        self.alpha = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"

    def swap32(self,i):
        return struct.unpack("<I", struct.pack(">I", i))[0]

    def decode(self, text):
        res = []

        index = 0
        value = self.magic
        shift = 0

        for c in text:
            index = self.alpha.index(c)
            value ^= (index << shift)
            value = ctypes.c_ulong(value).value
            shift += 5

            if (shift > 31):
                res.append(self.swap32(value))
                shift &= 7
                value = self.magic ^ index >> 5 - shift
                value = ctypes.c_ulong(value).value

        return res