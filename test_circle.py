import math
from unittest import TestCase

from circle import Circle


class TestCircle(TestCase):
    def test_non_positive_radius_raises_AssertionError_1(self):
        with self.assertRaises(AssertionError):
            c = Circle(-1.0)

    def test_non_positive_radius_raises_AssertionError_2(self):
        with self.assertRaises(AssertionError):
            c = Circle(0.0)

    def test_nonnumerical_radius_raises_AssertionError(self):
        with self.assertRaises(AssertionError):
            c = Circle('1.0')

    def test_property_radius_for_type_enforcing(self):
        self.c1 = Circle(10.0, 'Yellow')
        with self.assertRaises(TypeError):
            self.c1.radius = 10

    def test_property_radius_for_value_enforcement(self):
        self.c1 = Circle(10.0, 'Yellow')
        with self.assertRaises(ValueError):
            self.c1.radius = 0.0

    def test_get_area(self):
        self.assertAlmostEqual(Circle(10.0).get_area(), math.pi * 100)


    def test_get_circumference(self):
        self.assertAlmostEqual(Circle(10.0).get_circumference(), math.pi * 20)

    def test_str(self):
        self.c1 = Circle(10.0, 'Yellow')
        self.assertIn(str(self.c1.radius), str(self.c1))
        # assert str(self.c1.radius) in str(self.c1)

    def test_property_color(self):
        c1 = Circle(10.0, 'Yellow')
        with self.assertRaises(TypeError):
            c1.color = 123
        c1.color = 'Red'
        self.assertEqual(c1.color, 'Red')


