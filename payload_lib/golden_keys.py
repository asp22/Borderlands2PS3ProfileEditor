class GoldenKeys:
    class KeyStruct:
        def __init__(self, data):
            self.source_id = data[0]
            self.n_keys = data[1]
            self.n_used = data[2]

        def set(self, v):
            v = min(v, 255)
            self.n_keys = v
            self.n_used = 0

        def add(self):
            if self.n_keys == 255:
                return
            self.n_keys += 1

        def as_bytes(self):
            b = b""
            b += self.source_id.to_bytes(1)
            b += self.n_keys.to_bytes(1)
            b += self.n_used.to_bytes(1)
            return b

        def count(self):
            return self.n_keys - self.n_used

    def __init__(self, items):
        self._init_item(items)
        self._init_keys()

    def _init_item(self, items):
        # we want item with id 162
        self.item = None
        for i in items:
            if i.id == 162:
                self.item = i
                break
        assert self.item is not None

    def _init_keys(self):
        keys = []
        data = self.item.get()
        n_entries = len(data) // 3
        for i in range(0, n_entries):
            begin = i*3
            end = begin+3
            d = data[begin:end]
            keys.append(GoldenKeys.KeyStruct(d))

        self.keys = keys

    def get(self):
        count = 0
        for k in self.keys:
            count += k.count()
        return count

    def set(self, v):
        v = min(255*3, v)
        per_key = v // 3
        remainder = v % 3
        for k in self.keys:
            k.set(per_key)

        i = 0
        while i != remainder:
            self.keys[i].add()
            i += 1

        b = b""
        for k in self.keys:
            b += k.as_bytes()

        self.item.set(b)