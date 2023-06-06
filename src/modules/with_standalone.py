"""with_standalone.py

_summary_

_extended_summary_
"""

def sort_seats(width):
    """Sorts the seats according to their widths.

    Parameters:
    ----------
    width : list
        The widths of each row.

    Returns:
    ----------
    list
        The sorted list of seats with their current seat status.
    """
    seats = [[w, False, False] for w in width]
    seats.sort()  # Sorting seats based on width in ascending order
    return seats


def arrange_seats(num_row, seq, seats):
    """Arranges the seating according to the given rules.

    Boys choose a row where both seats are free, and out of those rows,
    they pick the smallest one. Girls choose a row where one seat is taken
    by a boy, and out of those rows, they pick the largest one.

    Parameters:
    ----------
    N : int
        The number of rows.
    S : str
        The sequence of people entering.
    seats : list
        The sorted list of seats with their current seat status.

    Returns:
    ----------
    list
        The list of rows with their current seat status.
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
