import pytest
from seating_arrangement_zip import seating_arrangement  # Assuming your function is defined in this module

def test_seating_arrangement_zip():
    N = 2
    S = '0011'
    W = [2, 1]
    assert seating_arrangement(N, S, W) == ['BG', 'BG']
