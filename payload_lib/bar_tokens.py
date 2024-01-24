class BarTokens:
    def __init__(self, items):
        self._init_item(items)

    def _init_item(self, items):
        self.item = None
        for i in items:
            if i.id == 138:
                self.item = i
                break
        assert self.item is not None

    def get(self):
        return self.item.get()

    def set(self, v):
        self.item.set(v)