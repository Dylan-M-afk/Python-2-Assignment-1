from unittest import TestCase

from point import Point
from line import Line
import math


class TestLine(TestCase):
    def test_line_init(self):
        p1 = Point(1.5, 1.2)
        p2 = Point(2.3, 2.5)
        line = Line(p1, p2)
        self.assertEqual(line.start_point, p1)
        self.assertEqual(line.end_point, p2)

    def test_line_length(self):
        p1 = Point(1.5, 1.2)
        p2 = Point(2.3, 2.5)
        line = Line(p1, p2)
        self.assertAlmostEqual(1.5264337522473748, line.length)

    def test_line_start_point_is_read_only(self):
        p1 = Point(1.5, 1.2)
        p2 = Point(2.3, 2.5)
        line = Line(p1, p2)
        with self.assertRaises(AttributeError):
            line.start_point = Point(3.1, 3.5)

    def test_line_end_point_can_be_modified(self):
        p1 = Point(1.5, 1.2)
        p2 = Point(2.3, 2.5)
        line = Line(p1, p2)
        new_end_point = Point(3.3, 3.2)
        line.end_point = new_end_point
        self.assertEqual(line.end_point, new_end_point)

    def test_len(self):
        p1 = Point(1.5, 1.2)
        p2 = Point(2.3, 2.5)
        line = Line(p1, p2)
        self.assertAlmostEqual(1.5264337522473748, line.length)

    def test_lt(self):
        p1 = Point(1.5, 1.2)
        p2 = Point(2.3, 2.5)
        l1 = Line(p1, p2)
        p3 = Point(-2.1, -4.1)
        p4 = Point(5.1, 2.3)
        l2 = Line(p3, p4)
        # print(l1.length, l2.length)
        self.assertTrue(l1 < l2)

    def test_gt(self):
        p1 = Point(1.5, 1.2)
        p2 = Point(2.3, 2.5)
        l1 = Line(p1, p2)
        p3 = Point(-2.1, -4.1)
        p4 = Point(5.1, 2.3)
        l2 = Line(p3, p4)
        # print(l1.length, l2.length)
        self.assertTrue(l2 > l1)

    def test_eq(self):
        p1 = Point(1.5, 1.2)
        p2 = Point(2.3, 2.5)
        l1 = Line(p1, p2)
        p3 = Point(-2.1, -4.1)
        p4 = Point(5.1, 2.3)
        l2 = Line(p3, p4)
        # print(l1.length, l2.length)
        self.assertTrue(l1 < l2)