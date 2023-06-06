import pytest
from with_classes import SeatingArrangement  # Assuming your class is defined in this module

def test_seating_arrangement_class():
    N = 2
    S = '0011'
    W = [2, 1]
    arrangement = SeatingArrangement(N, S, W)
    assert arrangement.arrange_seats() == [[1, True, True], [2, True, True]]
