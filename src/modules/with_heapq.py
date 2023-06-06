"""with_heapq.py

_summary_

_extended_summary_

Returns:
    _type_: _description_
"""

import heapq


def hq_seat_arrange(N, S, W):
    """Finds the seating arrangement according to the given rules.

    Uses two priority queues (heaps) to efficiently find the best row for each
    boy and girl. Boys choose a row where both seats are free, and out of those rows,
    they pick the smallest one. Girls choose a row where one seat is taken
    by a boy, and out of those rows, they pick the largest one.

    Parameters:
    ----------
    N : int
        The number of rows.
    S : str
        The sequence of people entering.
    W : list
        The widths of each row.

    Returns:
    ----------
    list
        The list of rows with their current seat status.
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
            seats[row] = 'B'  # Mark this row as occupied by a boy
            # Push this row into girls_heap
            heapq.heappush(girls_heap, [-W[row], row])  # We use -W[row] because Python's heapq provides min heap
        else:  # Girl
            # Get the row with maximum width from girls_heap
            _, row = heapq.heappop(girls_heap)
            seats[row] += 'G'  # Mark this row as also occupied by a girl

    return seats
