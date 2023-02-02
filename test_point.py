from unittest import TestCase

from point import Point


class TestPoint(TestCase):
    def test_point_creation_x(self):
        p = Point(2.0, 4.0)
        self.assertTrue(p.x == 2, 'Point\'s x coordinate does not match what is set')

    def test_point_creation_y(self):
        p = Point(2.0, 4.0)
        self.assertTrue(p.y == 4, 'Point\'s y coordinate does not match what is set')

    def test_point_str(self):
        p = Point(2.0, 4.0)
        self.assertTrue(str(p) == '(2.0, 4.0)')

    def test_point_x_is_readonly(self):
        p = Point(2.0, 4.0)
        with self.assertRaises(AttributeError):
            p.x = 3

    def test_point_y_is_readonly(self):
        p = Point(2.0, 4.0)
        with self.assertRaises(AttributeError):
            p.y = 3
