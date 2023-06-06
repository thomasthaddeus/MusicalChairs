"""
This module provides four implementations of a seating arrangement algorithm.

The algorithm is used to find a possible arrangement of people entering a hall
according to the following rules:
- Boys choose a row where both seats are free, and out of those rows, they pick
  the smallest one.
- Girls choose a row where one seat is taken by a boy, and out of those rows,
  they pick the largest one.

The implementations use different strategies:
1. Using a class: SeatingArrangement
2. Using heapq: hq_seat_arrange
3. Using standalone functions: sort_seats, arrange_seats
4. Using zip and sorted: zip_seat_arrange
"""

import time
import timeit
from with_heapq import hq_seat_arrange
from with_classes import SeatingArrangement
from with_standalone import sort_seats, arrange_seats
from with_zip_sorted import zip_seat_arrange

N = 2
S = '0011'
W = [2, 1]


def main() -> None:
    """
    Executes and compares the outputs of four implementations of a seating
    arrangement algorithm.

    The implementations are executed with the same input, their outputs are
    printed to the console, and their execution times are measured and reported.
    """

    test_runs = 5  # adjust this to change the number of times each test is run
    pause_time = 1  # adjust this to change the length of the pause between tests (in seconds)

    for i in range(test_runs):
        print(f"\nTest run {i+1}:")

        # Using the class:
        start: float = timeit.default_timer()
        arrangement = SeatingArrangement(N, S, W)
        print(arrangement.arrange_seats())
        end: float = timeit.default_timer()
        print(f"Execution time (class approach): {end - start}")

        time.sleep(pause_time)

        # Using heapq:
        start = timeit.default_timer()
        print(hq_seat_arrange(N, S, W))
        end = timeit.default_timer()
        print(f"Execution time (heapq approach): {end - start}")

        time.sleep(pause_time)

        # Using standalone functions:
        start = timeit.default_timer()
        seats: list[list] = sort_seats(W)
        print(arrange_seats(N, S, seats))
        end = timeit.default_timer()
        print(f"Execution time (standalone functions approach): {end - start}")

        time.sleep(pause_time)

        # Using zip and sorted:
        start = timeit.default_timer()
        print(zip_seat_arrange(N, S, W))
        end = timeit.default_timer()
        print(f"Execution time (zip and sorted approach): {end - start}")

        time.sleep(pause_time)

if __name__ == '__main__':
    main()
