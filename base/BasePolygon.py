from itertools import chain
import itertools


class BasePolygon:
    """
    默认为封闭的多边形
    """

    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def get_points(self):
        return self.points

    def export(self):
        return ",".join(map(lambda x: "%d" % x, chain.from_iterable(self.points)))

    def load(self, cols):
        if len(self.points) != 0:
            raise Exception('将会覆盖当前多边形')
        assert len(cols) == 8,'坐标数不对'
        self.points = list(itertools.zip_longest(cols[::2],cols[1::2]))
        return self
