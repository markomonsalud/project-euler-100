import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Problem1 import *

def test_multiplesOf3and5():
    assert multiplesOf3and5(10).bit_length() > 0  
    assert multiplesOf3and5(49) == 543
    assert multiplesOf3and5(1000) == 233168
    assert multiplesOf3and5(8456) == 16687353
    assert multiplesOf3and5(19564) == 89301183