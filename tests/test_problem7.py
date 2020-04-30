import os
import sys

from Problem7 import nth_prime

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


def test_nth_prime():
    assert nth_prime(6).bit_length() > 0
    assert nth_prime(6) == 13
    assert nth_prime(10) == 29
    assert nth_prime(100) == 541
    assert nth_prime(1000) == 7919
    assert nth_prime(10001) == 104743
