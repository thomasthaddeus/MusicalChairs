"""with_sort.py

This module provides two standalone functions to help determine the seating
arrangement in a hall based on a sequence of people entering and the widths
of the rows.

The arrange_seats function follows these rules:
- Boys choose a row where both seats are free, and out of those rows,
  they pick the smallest one.
- Girls choose a row where one seat is taken by a boy, and out of those rows,
  they pick the largest one.

This module is intended to be a more bare-bones, standalone implementation of
the seating arrangement algorithm, and it doesn't use any classes or priority
queues. Instead, it simply sorts the seats and iterates through them for each
person in the sequence.
"""

def with_sort(width):
    """Sorts the seats according to their widths.

    Args:
        width (list): The widths of each row.

    Returns:
        list: The sorted list of seats with their current seat status.
    """
    seats = [[w, False, False] for w in width]
    seats.sort()  # Sorting seats based on width in ascending order
    return seats


def arng_seats(num_row, seq, seats):
    """Arranges the seating according to the given rules.

    Boys choose a row where both seats are free, and out of those rows,
    they pick the smallest one. Girls choose a row where one seat is taken
    by a boy, and out of those rows, they pick the largest one.

    Args:
        num_row (int): The number of rows.
        seq (str): The sequence of people entering.
        seats (list): The sorted list of seats with their current seat status.

    Returns:
        list: The list of rows with their current seat status.
    """
    for person in seq:
        if person == '0':  # Boy
            for seat in seats:
                if not seat[1] and not seat[2]:  # Both seats are empty
                    seat[1] = True  # Boy sits in the first seat
                    break
        else:  # Girl
            widest_seat = None
            for seat in seats:
                if seat[1] and not seat[2]:  # One seat is occupied by a boy
                    widest_seat = seat  # Track the widest seat
            if widest_seat:
                widest_seat[2] = True  # Girl sits in the second seat
    return seats
