"""with_classes.py

_summary_

_extended_summary_

Returns:
    _type_: _description_
"""


class SeatingArrangement:
    """A class to represent a seating arrangement in a hall.

    Attributes:
    ----------
    N : int
        The number of rows.
    S : str
        The sequence of people entering.
    W : list
        The widths of each row.
    seats : list
        The sorted list of rows with their current seat status.

    Methods:
    ----------
    arrange_seats():
        Arranges the seating according to the given rules.
    """

    def __init__(self, num_row, seq, width):
        """The constructor for SeatingArrangement class.

        Parameters:
        ----------
        N : int
            The number of rows.
        S : str
            The sequence of people entering.
        W : list
            The widths of each row.
        """
        self.num_row = num_row
        self.seq = seq
        self.width = width
        self.seats = [[w, False, False] for w in width]
        self.seats.sort()  # Sorting seats based on width in ascending order

    def arrange_seats(self):
        """Arranges the seating according to the given rules.

        Boys choose a row where both seats are free, and out of those rows,
        they pick the smallest one. Girls choose a row where one seat is taken
        by a boy, and out of those rows, they pick the largest one.

        Returns:
        ----------
        list
            The list of rows with their current seat status.
        """
        for person in self.seq:
            if person == '0':  # Boy
                for seat in self.seats:
                    if not seat[1] and not seat[2]:  # Both seats are empty
                        seat[1] = True  # Boy sits in the first seat
                        break
            else:  # Girl
                widest_seat = None
                for seat in self.seats:
                    if seat[1] and not seat[2]:  # One seat is occupied by a boy
                        widest_seat = seat  # Track the widest seat
                if widest_seat:
                    widest_seat[2] = True  # Girl sits in the second seat
        return self.seats
