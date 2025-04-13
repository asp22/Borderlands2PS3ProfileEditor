import payload_lib.string_to_list as string_to_list
import payload_lib.list_to_string as list_to_string
import math

class BarStats:
    def __init__(self, items):
        self._init_item(items)
        self._init_stat_points()

    @staticmethod
    def pts_to_pct(pts):
        pct = round(pow(pts, 0.75) * 10) / 10
        return pct

    def _pct_to_pts(self, pct):
        y = math.log(pct,10) / 0.75
        pts = round(pow(10,y))
        return int(pts)

    def _init_item(self, items):
        # we want item with id 143
        self.item = None
        for i in items:
            if i.id == 143:
                self.item = i
                break
        assert self.item is not None

    def _init_stat_points(self):
        decoder = string_to_list.Decoder()
        self.stat_points = decoder.decode(self.item.get())

    def stats_as_pct(self):
        return [BarStats.pts_to_pct(f) for f in self.stat_points]

    def set_stats(self, floats):
        pcts = self.stats_as_pct()
        for i, pct in enumerate(pcts):
            if floats[i] is not None:
                pcts[i] = floats[i]

        self.stat_points = [self._pct_to_pts(f) for f in pcts]
        encoder = list_to_string.Encoder()
        text = encoder.encode(self.stat_points)
        self.item.set(text)