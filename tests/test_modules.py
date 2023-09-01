"""test_modules.py

This module contains unit tests for various seating arrangement functions and
classes. The tests ensure that given a seating configuration and weights, the
seating arrangement methods return the expected results.

The module imports several seating arrangement methods from different modules:
- SeatingArrangement class from 'with_classes'
- sort_seats and arrange_seats functions from 'with_standalone'
- hq_seat_arrange function from 'with_heapq'
- zip_seat_arrange function from 'with_zip_sorted'

Each test function in this module corresponds to one of the imported seating
arrangement methods. The tests are designed to verify the correctness of the
seating arrangement logic implemented in each method.

Note:
    It's recommended to run these tests after making changes to any of the
    seating arrangement methods to ensure their continued correctness.
"""

from types import MethodType
import pytest
from with_sort import with_sort, arng_seats
from with_heapq import hq_seat_arrange
from with_zip_sorted import zip_seat_arrange
from with_classes import SeatingArrangement

@pytest.mark.parametrize("method", MethodType) # type: ignore
def test_seating_arrangement_class():
    """
    Test the SeatingArrangement class for correct seat arrangement.

    Given a seating configuration and weights, this test ensures that
    the SeatingArrangement class correctly arranges the seats.
    """
    N = 2
    S = '0011'
    W = [2, 1]
    arrangement = SeatingArrangement(N, S, W)
    assert arrangement.arrange_seats() == [[1, True, True], [2, True, True]]

def test_zip_seat_arrange():
    """
    Test the zip_seat_arrange function for correct seat arrangement.

    Given a seating configuration and weights, this test ensures that
    the zip_seat_arrange function correctly arranges the seats.
    """
    N = 2
    S = '0011'
    W = [2, 1]
    assert zip_seat_arrange(N, S, W) == ['BG', 'BG']

def test_seating_arrangement_functions():
    """
    Test the standalone seating arrangement functions for correct seat arrangement.

    Given a seating configuration and weights, this test ensures that
    the standalone functions correctly arrange the seats.
    """
    N = 2
    S = '0011'
    W = [2, 1]
    seats = with_sort(W)
    assert arng_seats(N, S, seats) == [[1, True, True], [2, True, True]]

def test_hq_seat_arrange():
    """
    Test the hq_seat_arrange function for correct seat arrangement.

    Given a seating configuration and weights, this test ensures that
    the hq_seat_arrange function correctly arranges the seats.
    """
    N = 2
    S = '0011'
    W = [2, 1]
    assert hq_seat_arrange(N, S, W) == ['BG', 'BG']
