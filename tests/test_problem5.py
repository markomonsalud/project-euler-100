import os
import sys

from Problem5 import smallest_multiple

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


def test_smallest_multiple():
    assert smallest_multiple(5).bit_length() > 0
    assert smallest_multiple(5) == 60
    assert smallest_multiple(7) == 420
    assert smallest_multiple(10) == 2520
    assert smallest_multiple(13) == 360360
    assert smallest_multiple(20) == 232792560
