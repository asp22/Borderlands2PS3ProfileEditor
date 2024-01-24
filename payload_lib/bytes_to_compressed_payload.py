import hashlib
import zlib

# Takes items that have been converted back to bytes
# and reconstructs a PAYLOAD and compresses it.
# The PAYLOAD is written to file via 'write_payload'
# The resulting file should be moved back to your profile
# save folder and encrypted using Bruteforce Save Data
class Compressor:
    def gen_sha1(self, rounds=80):
        message = self.uncompressed_length_bytes + self.compressed_bytes
        sha1 = hashlib.sha1(message, usedforsecurity=False)
        return sha1.digest()

    def __init__(self, data):
        self.decompressed_bytes = data
        self.uncompressed_length = len(data)
        self.uncompressed_length_bytes = self.uncompressed_length.to_bytes(4)

        self.compressed_bytes = zlib.compress(self.decompressed_bytes)
        self.sha1 = self.gen_sha1()

    def get(self):
        b = b""
        b += self.sha1
        b += self.uncompressed_length_bytes
        b += self.compressed_bytes
        return b

    def write_payload(self, filename):
        with open(filename, 'wb') as f:
            f.write(self.get())