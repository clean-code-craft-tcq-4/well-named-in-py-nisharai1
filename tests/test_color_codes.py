from unittest import TestCase

from color_code_pairs.get_color_code_pair import (
    get_color_from_pair_number,
    get_pair_number
)


class TestColorCodePair(TestCase):
    def setUp(self):
        self.pair_number = 7
        self.expected_major_color = 'Red'
        self.expected_minor_color = 'Orange'
        self.expected_pair_number = 22
        self.major_color = 'Violet'
        self.minor_color = 'Orange'

    def test_number_to_pair(self):
        major_color, minor_color = get_color_from_pair_number(self.pair_number)
        self.assertEqual(self.expected_major_color.lower(), major_color)
        self.assertEqual(self.expected_minor_color.lower(), minor_color)

    def test_pair_to_number(self):
        pair_number = get_pair_number(self.major_color, self.minor_color)
        self.assertEqual(self.expected_pair_number, pair_number)
