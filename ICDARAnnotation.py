import os

from base.BaseAnnotation import BaseAnnotation
from base.BasePolygon import BasePolygon


class ICDARAnnotation(BaseAnnotation):
    """
    针对于icdar的标注
    即每组有4个点，然后跟上具体的文本
    """

    def __init__(self):
        self.polygons = []
        self.texts = []

    def export(self, location):
        """
        每次export都会覆盖当前文件中的内容
        :param location:    需要export的文件的路径
        """
        assert len(self.polygons) == len(self.texts), '多边形数量与文本数量不一致'
        assert all(map(lambda x: isinstance(x, BasePolygon), self.polygons)), '多边形的类型不对'
        with open(location, encoding='utf-8', mode='w+') as to_write:
            for m_polygon, m_text in zip(self.polygons, self.texts):
                to_write.write(f"{m_polygon.export()},{m_text}\n")

    def load(self, annotation_file):
        if os.path.exists(annotation_file):
            with open(annotation_file, encoding='utf-8') as to_read:
                for m_line in to_read:
                    cols = m_line.strip().split(",")
                    assert len(cols) == 9, f'[{m_line.strip()}]不符合ICDAR规范'
                    self.polygons.append(BasePolygon().load(cols[:8]))
                    self.texts.append(cols[-1])
        return self
