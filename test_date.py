from unittest import TestCase
from date import Date


class TestDate(TestCase):
    def test_init_types(self):
        with self.assertRaises(TypeError):
            Date(year=1.0, month=1, day=1)
        with self.assertRaises(TypeError):
            Date(1, "1", 1)
        with self.assertRaises(TypeError):
            Date(1, 1, True)
        with self.assertRaises(ValueError):
            Date(year=2022, month=1, day=32)
        with self.assertRaises(ValueError):
            Date(year=2022, month=13, day=1)
        with self.assertRaises(ValueError):
            Date(year=2022, month=1, day=0)
        with self.assertRaises(ValueError):
            Date(year=2022, month=-1, day=1)

    def test_day_property(self):
        d = Date(year=1, month=1, day=1)
        self.assertEqual(d.day, 1)
        d.day = 20
        self.assertEqual(d.day, 20)

    def test_month_property(self):
        d = Date(year=1, month=1, day=1)
        self.assertEqual(d.month, 1)
        d.month = 10
        self.assertEqual(d.month, 10)

    def test_year_property(self):
        d = Date(year=2000, month=1, day=1)
        self.assertEqual(d.year, 2000)
        d.year = 2010
        self.assertEqual(d.year, 2010)

    def test_is_leap_year(self):
        d = Date(year=2020, month=1, day=1)
        self.assertTrue(d.is_leap_year)
        d = Date(year=2022, month=1, day=1)
        self.assertFalse(d.is_leap_year)

    def test_valid_date(self):
        d = Date(year=2020, month=1, day=1)
        self.assertTrue(d.is_valid_date)
        d = Date(year=2020, month=1, day=31)
        self.assertTrue(d.is_valid_date)
        d = Date(year=2020, month=2, day=29)
        self.assertTrue(d.is_valid_date)
        d = Date(year=2021, month=2, day=29)
        self.assertFalse(d.is_valid_date)
        d = Date(year=2020, month=4, day=31)
        self.assertFalse(d.is_valid_date)
