import os
import sys

from Problem2 import fib_even_sum

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


def test_fib_even_sum():
    assert fib_even_sum(10).bit_length() > 0
    assert fib_even_sum(10) == 10
    assert fib_even_sum(60) == 44
    assert fib_even_sum(1000) == 798
    assert fib_even_sum(100000) == 60696
    assert fib_even_sum(4000000) == 4613732
    assert fib_even_sum(2000) % 2 == 0
