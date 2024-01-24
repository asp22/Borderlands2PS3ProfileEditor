import struct

# Takes a list of ints
# and converts it to a string
class Encoder:
    def __init__(self):
        self.magic = 0x9A3652D9
        self.alpha = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"

    def swap32(self,i):
        return struct.unpack("<I", struct.pack(">I", i))[0]

    def encode(self, numbers):
        text = ""

        index = 0
        shift = 0

        # 1; swap byte order
        numbers = [self.swap32(i) for i in numbers]

        for value in numbers:
            value ^= self.magic

            if (shift > 0):
                index = ((index | (value << shift)) & 0x1F)
                shift = 5 - shift
                text += self.alpha[index]

            while shift < 28:
                index = ((value >>shift) &0x1f)
                text += self.alpha[index]
                shift += 5

            index = value >> shift;
            shift = 32 - shift

        if shift > 0:
            text += self.alpha[index]

        return text