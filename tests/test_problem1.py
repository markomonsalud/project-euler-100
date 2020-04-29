import os
import sys

from Problem1 import multiples_of3and5

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


def test_multiples_of3and5():
    assert multiples_of3and5(10).bit_length() > 0
    assert multiples_of3and5(49) == 543
    assert multiples_of3and5(1000) == 233168
    assert multiples_of3and5(8456) == 16687353
    assert multiples_of3and5(19564) == 89301183