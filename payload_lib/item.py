import payload_lib.data_types

class Item:
    def __init__(self, data, offset) -> None:
        self.pos = offset
        self.start_byte = data[offset]
        offset += 1

        self.id = int.from_bytes(data[offset:offset+4])
        offset += 4

        self.data_type = data[offset]
        offset += 1

        self.end_byte = None

    def bytes(self):
        b = b""
        b += self.start_byte.to_bytes(1)
        b += self.id.to_bytes(4)
        b += self.data_type.to_bytes(1)
        b += self.value_as_bytes()
        b += self.end_byte.to_bytes()
        return b

    def set(self, v):
        self.value = v

class ItemInt32(Item):
    def __init__(self, data, offset):
        super().__init__(data, offset)
        offset += 6

        byte_array = data[offset:offset+4]
        self.value = int.from_bytes(byte_array)
        offset += 4

        self.end_byte = data[offset]
        offset += 1

        self.next_offset = offset

    def next_offset(self):
        return self.next_offset

    def get(self):
        return self.value

    def value_as_bytes(self):
        return self.value.to_bytes(4)

    def __str__(self):
        return f"pos: {self.pos} id: {self.id} Int32: {self.value}"


class ItemString(Item):
    def __init__(self, data, offset):
        super().__init__(data, offset)
        offset += 6

        length = int.from_bytes(data[offset:offset+4])
        offset += 4
        byte_array = data[offset:offset+length]
        self.value = byte_array.decode('ascii')
        offset += length

        self.end_byte = data[offset]
        offset += 1

        self.next_offset = offset

    def next_offset(self):
        return self.next_offset

    def get(self):
        return self.value

    def value_as_bytes(self):
        bytes = b""
        length = len(self.value)
        bytes += length.to_bytes(4)
        bytes += self.value.encode()
        return bytes

    def __str__(self):
        return f"pos: {self.pos} id: {self.id} string: {self.value}"

class ItemFloat(Item):
    def __init__(self, data, offset):
        super().__init__(data, offset)
        offset += 6

        byte_array = data[offset:offset+4]
        self.value = float.from_bytes(byte_array)
        offset += 4

        self.end_byte = data[offset]
        offset += 1

        self.next_offset = offset

    def next_offset(self):
        return self.next_offset

    def get(self):
        return self.value

    def value_as_bytes(self):
        return self.value.to_bytes(4)

    def __str__(self):
        return f"pos: {self.pos} id: {self.id} float: {self.value}"

class ItemBinary(Item):
    def __init__(self, data, offset):
        super().__init__(data, offset)
        offset += 6

        length = int.from_bytes(data[offset:offset+4])
        offset += 4
        byte_array = data[offset:offset+length]
        self.value = byte_array
        offset += length

        self.end_byte = data[offset]
        offset += 1

        self.next_offset = offset

    def next_offset(self):
        return self.next_offset

    def get(self):
        return self.value

    def value_as_bytes(self):
        bytes = b""
        length = len(self.value)
        bytes += length.to_bytes(4)
        bytes += self.value
        return bytes

    def __str__(self):
        return f"pos: {self.pos} id: {self.id} binary: {self.value}"

class ItemInt8(Item):
    def __init__(self, data, offset):
        super().__init__(data, offset)
        offset += 6

        self.value = int(data[offset])
        offset += 1

        self.end_byte = data[offset]
        offset += 1

        self.next_offset = offset

    def next_offset(self):
        return self.next_offset

    def get(self):
        return self.value

    def value_as_bytes(self):
        return self.value.to_bytes(1)

    def __str__(self):
        return f"pos: {self.pos} id: {self.id} int8: {self.value}"