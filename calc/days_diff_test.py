import unittest
from calc.days_diff import DaysDiff
from datetime import datetime


class TestDaysDiff(unittest.TestCase):

    def test_diff(self):
        now = datetime(2017, 1, 1)
        end = datetime(2017, 1, 11)

        calc = DaysDiff()

        self.assertEqual(10, calc.diff(now, end))

    def test_diff_start_earlier_end_returns_negative_int(self):
        now = datetime(2018, 1, 1)
        end = datetime(2017, 1, 1)

        calc = DaysDiff()
        self.assertEqual(-365, calc.diff(now, end))
