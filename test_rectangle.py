from unittest import TestCase
from point import Point
from rectangle import Rectangle


class TestRectangle(TestCase):
    def test_rectangle_init(self):
        point = Point(1.1, 1.2)
        non_point = 'a'
        with self.assertRaises(AssertionError):
            rect = Rectangle(point, non_point)
        with self.assertRaises(AssertionError):
            rect = Rectangle(non_point, point)

    def test_rectangle_bottom_left_property(self):
        p1 = Point(1.2, 1.4)
        p2 = Point(2.4, 2.3)
        rect = Rectangle(p1, p2)
        self.assertEqual(rect.bottom_left_corner, p1)

    def test_rectangle_top_right_property(self):
        p1 = Point(1.0, 1.0)
        p2 = Point(2.0, 2.0)
        rect = Rectangle(p1, p2)
        self.assertEqual(rect.top_right_corner, p2)

    def test_assertion_error_for_incorrect_type_init_p1(self):
        p2 = Point(1.4, 1.2)
        p1 = (2, 2)
        with self.assertRaises(AssertionError):
            Rectangle(p1, p2)

    def test_assertion_error_for_incorrect_type_init_p2(self):
        p1 = Point(1.5, 1.4)
        p2 = [2, 2]
        with self.assertRaises(AssertionError):
            Rectangle(p1, p2)

    def test_rectangle_top_left_corner_property(self):
        p1 = Point(1.0, 1.0)
        p2 = Point(2.0, 2.0)
        rect = Rectangle(p1, p2)
        self.assertEqual(str(rect.top_left_corner), str(Point(1.0, 2.0)))

    def test_rectangle_bottom_right_corner_property(self):
        p1 = Point(1.0, 1.0)
        p2 = Point(2.0, 2.0)
        rect = Rectangle(p1, p2)
        self.assertEqual(str(rect.bottom_right_corner), str(Point(2.0, 1.0)))

    def test_rectangle_area(self):
        p1 = Point(1.0, 4.0)
        p2 = Point(8.0, 20.0)
        rect = Rectangle(p1, p2)
        self.assertEqual(112, rect.area)

    def test_rectangle_perimeter(self):
        p1 = Point(1.0, 4.0)
        p2 = Point(8.0, 20.0)
        rect = Rectangle(p1, p2)
        self.assertEqual(46, rect.perimeter)
