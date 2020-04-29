import os
import sys

from Problem3 import largest_prime_factor

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


def test_largest_prime_factor():
    assert largest_prime_factor(2).bit_length() > 0
    assert largest_prime_factor(2) == 2
    assert largest_prime_factor(3) == 3
    assert largest_prime_factor(5) == 5
    assert largest_prime_factor(7) == 7
    assert largest_prime_factor(13195) == 29
    assert largest_prime_factor(600851475143) == 6857
