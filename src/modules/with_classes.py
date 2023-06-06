"""with_classes.py

A module that contains the SeatingArrangement class, which represents a seating
arrangement in a hall and implements a specific seating algorithm based on the
width of the rows and the sequence of people (boys and girls) entering the hall.

The seating algorithm works as follows:
- Boys choose a row where both seats are free, and out of those rows, they pick
  the one with the smallest width.
- Girls choose a row where one seat is already occupied by a boy, and out of
  those rows, they pick the one with the largest width.

Returns:
    SeatingArrangement: The main class of the module, which can be used to
        implement the seating arrangement algorithm.
"""


class SeatingArrangement:
    """A class to represent a seating arrangement in a hall.

    Attributes:
        N (int): The number of rows in the hall.
        S (str): The sequence of people (represented as a string of '0's and '1's,
            where '0' represents a boy and '1' represents a girl) entering the hall.
        W (list): A list of integers representing the widths of the rows in the hall.
        seats (list): A sorted list of lists, where each inner list represents a row
            and contains three elements: the width of the row, and two boolean values
            indicating whether the two seats in the row are occupied.

    Methods:
        arrange_seats(): Implements the seating arrangement algorithm and updates
            the `seats` attribute.
    """


    def __init__(self, num_row, seq, width):
        """The constructor for the SeatingArrangement class.

        Args:
            N (int): The number of rows in the hall.
            S (str): The sequence of people entering the hall.
            W (list): The widths of the rows in the hall.
        """
        self.num_row = num_row
        self.seq = seq
        self.width = width
        self.seats = [[w, False, False] for w in width]
        self.seats.sort()  # Sorting seats based on width in ascending order

    def arrange_seats(self):
        """Implements the seating arrangement algorithm.

        The algorithm works as follows:
        - Boys choose a row where both seats are free, and out of those rows, they
          pick the one with the smallest width.
        - Girls choose a row where one seat is already occupied by a boy, and out of
          those rows, they pick the one with the largest width.

        The method updates the `seats` attribute to reflect the implemented seating
        arrangement.

        Returns:
            list: The list of rows with their current seat status after implementing
                the seating arrangement.
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
