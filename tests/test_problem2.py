

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Problem2 import *

def test_fiboEvenSum():
    assert fiboEvenSum(10).bit_length() > 0 
    assert fiboEvenSum(10) == 10
    assert fiboEvenSum(60) == 44
    assert fiboEvenSum(1000) == 798
    assert fiboEvenSum(100000) == 60696
    assert fiboEvenSum(4000000) == 4613732
    assert fiboEvenSum(2000) % 2 == 0