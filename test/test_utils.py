from unittest import TestCase

from constants import CARDINAL_POINTS
from utils import CircularList


class UtilsTest(TestCase):
    def test_circular_list(self):
        cardinality = CircularList(CARDINAL_POINTS)

        current_cardinal_point = 'N'
        current_cardinal_point = cardinality.previous(current_cardinal_point)
        current_cardinal_point = cardinality.previous(current_cardinal_point)
        self.assertEqual(current_cardinal_point, 'S')

        current_cardinal_point = 'E'
        current_cardinal_point = cardinality.previous(current_cardinal_point)
        current_cardinal_point = cardinality.next(current_cardinal_point)
        current_cardinal_point = cardinality.next(current_cardinal_point)
        current_cardinal_point = cardinality.next(current_cardinal_point)
        self.assertEqual(current_cardinal_point, 'W')
