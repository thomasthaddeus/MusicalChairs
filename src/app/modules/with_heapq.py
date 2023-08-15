"""with_heapq.py

This module contains a function, hq_seat_arrange, that implements a specific
seating arrangement algorithm for a hall. The algorithm is based on the widths
of the rows and the sequence of people (boys and girls) entering the hall.

The seating algorithm works as follows:
- Boys choose a row where both seats are free, and out of those rows, they pick
  the one with the smallest width. This is implemented using a min heap.
- Girls choose a row where one seat is already occupied by a boy, and out of
  those rows, they pick the one with the largest width. This is implemented
  using a max heap.

The hq_seat_arrange function uses two priority queues (implemented as heaps)
to efficiently find the best row for each boy and girl.

Returns:
    hq_seat_arrange (function): A function that takes the number of rows in the
        hall, the sequence of people entering, and the widths of the rows, and
        returns the final seating arrangement after all people have entered.
"""

import heapq


def hq_seat_arrange(N, S, W):  # pylint: disable=invalid-name
    """Finds the optimal seating arrangement in a hall using a heap-based algorithm.

    Args:
        N (int): The number of rows in the hall.
        S (str): The sequence of people (represented as a string of '0's and
                 '1's, where '0' represents a boy and '1' represents a girl)
                 entering the hall.
        W (list): A list of integers representing the widths of the rows in the
                  hall.

    Returns:
        list: A list of strings representing the final seating arrangement in
        each row. Each string contains 'B' if the first seat is occupied by a
        boy and 'BG' if both seats are occupied (the first by a boy and the
        second by a girl).
    """
    # Initialize two heaps
    boys_heap = [[w, i] for i, w in enumerate(W)]  # Min heap for boys
    girls_heap = []  # Max heap for girls, currently empty

    # Convert boys_heap into a heap (i.e., partially ordered, root element is smallest)
    heapq.heapify(boys_heap)

    # Initialize an empty seating arrangement
    seats = [None]*N
    for person in S:
        if person == '0':  # Boy
            # Get the row with minimum width from boys_heap
            _, row = heapq.heappop(boys_heap)

            # Mark this row as occupied by a boy
            seats[row] = 'B'

            # Push this row into girls_heap
            # We use -W[row] because Python's heapq provides min heap
            heapq.heappush(girls_heap, [-W[row], row])
        else:  # Girl
            # Get the row with maximum width from girls_heap
            _, row = heapq.heappop(girls_heap)
            seats[row] += 'G'  # Mark this row as also occupied by a girl

    return seats
