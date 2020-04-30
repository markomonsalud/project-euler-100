import os
import sys

from Problem6 import sum_square_difference

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


def test_sum_square_difference():
    assert sum_square_difference(5).bit_length() > 0
    assert sum_square_difference(10) == 2640
    assert sum_square_difference(20) == 41230
    assert sum_square_difference(100) == 25164150
