import pytest
from with_heapq import hq_seat_arrange # Assuming your function is defined in this module

def test_hq_seat_arrange():
    N = 2
    S = '0011'
    W = [2, 1]
    assert hq_seat_arrange(N, S, W) == ['BG', 'BG']
