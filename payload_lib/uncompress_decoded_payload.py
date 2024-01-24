import zlib
import hashlib

# used to uncompress a PAYLOAD file (must first be decrypted using Bruteforce Save Data)
# Note on Bruteforce Save Data:
# Before decrypting anything, first verify the PFD
# If this fails, then the decrypted PAYLOAD will be incorrect
class Uncompressor:
    @staticmethod
    def _read_sha1(decrypted_payload):
        with open(decrypted_payload, 'rb') as f:
            sha1 = f.read(20)
        return sha1

    @staticmethod
    def _read_uncompressed_length(decrypted_payload):
        with open(decrypted_payload, 'rb') as f:
            sha1_and_length = f.read(24)
        return sha1_and_length[20:]

    @staticmethod
    def _read_compressed_bytes(decrypted_payload):
        with open(decrypted_payload, 'rb') as f:
            data = f.read()
        return data[24:]

    def __init__(self, decrypted_payload_path):
        X = Uncompressor
        self.sha1 = X._read_sha1(decrypted_payload_path)
        self.uncompressed_length_bytes = X._read_uncompressed_length(decrypted_payload_path)
        self.uncompressed_length = int.from_bytes(self.uncompressed_length_bytes, byteorder='big', signed = False)
        self.compressed_bytes = X._read_compressed_bytes(decrypted_payload_path)
        self.uncompressed_bytes = zlib.decompress(self.compressed_bytes, bufsize=self.uncompressed_length)

    def get(self):
        return self.uncompressed_bytes