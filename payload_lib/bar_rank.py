class BarRank:
    def __init__(self, items):
        self.item1 = self._find_item(items, 136)
        self.item2 = self._find_item(items, 137)

    def _find_item(self, items, id):
        for i in items:
            if i.id == id:
                return i
        assert False

    def _combine(self):
        res = (self.item1.get() + self.item2.get()) // 10
        return res

    def _split(self, v):
        res = (v*10) // 2
        return res

    def get(self):
        return self._combine()

    def set(self, v):
        x = self._split(v)
        self.item1.set(x)
        self.item2.set(x)