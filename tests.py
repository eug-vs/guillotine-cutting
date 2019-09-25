from toolkit import *
from unittest import TestCase, main


class SlicerTestCase(TestCase):
    def setUp(self):
        surface = Shape(4, 5)
        blocks = [Shape(3, 2), Shape(2, 2), Shape(2, 1), Shape(2, 3), Shape(1, 2)]
        self.slicer = Slicer(surface, blocks)

    def test_slice_pair_horizontal(self):
        assert self.slicer.slice_pair_horizontal() == [
            (Shape(3, 2), Shape(1, 2)),
            (Shape(2, 2), Shape(2, 1)),
            (Shape(2, 2), Shape(2, 3)),
            (Shape(2, 1), Shape(2, 3)),
        ], "Horizontal slice doesn't work"

    def test_slice_pair_vertical(self):
        assert self.slicer.slice_pair_vertical() == [
            (Shape(3, 2), Shape(2, 3)),
            (Shape(2, 2), Shape(2, 3)),
            (Shape(2, 3), Shape(1, 2)),
        ], "Vertical slice doesn't work"


if __name__ == '__main__':
    main()
