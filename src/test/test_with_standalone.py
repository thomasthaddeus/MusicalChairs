import pytest
from with_standalone import sort_seats, arrange_seats  # Assuming your functions are defined in this module

def test_seating_arrangement_functions():
    N = 2
    S = '0011'
    W = [2, 1]
    seats = sort_seats(W)
    assert arrange_seats(N, S, seats) == [[1, True, True], [2, True, True]]
