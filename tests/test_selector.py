import unittest

from datetime import date

from consistentor import Selector


class TestSelector(unittest.TestCase):
    def setUp(self):
        self.items = ["pizza", "burger", "pasta", "chili"]
        self.selector = Selector(self.items)

    def test_selection_default_value(self):
        selected1 = self.selector.select_for_date()
        selected2 = self.selector.select_for_date()
        self.assertEqual(selected1, selected2)
        self.assertIn(selected1, self.items)

    def test_selection_with_date_input(self):
        selected1 = self.selector.select_for_date(date(2020, 4, 1))
        self.assertEqual("chili", selected1)