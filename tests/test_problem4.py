import os
import sys

from Problem4 import largest_palindrome

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


def test_largest_palindrome():
    assert largest_palindrome(2).bit_length() > 0
    assert largest_palindrome(2) == 9009
    assert largest_palindrome(3) == 906609
