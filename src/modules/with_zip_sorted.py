"""with_zip_sorted.py

_summary_

_extended_summary_
"""

def zip_seat_arrange(num_row, seq, width):
    """Finds the seating arrangement according to the given rules.

    Uses the zip function to iterate over the people and rows in parallel.
    Boys choose a row where both seats are free, and out of those rows,
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
    # Create the list of rows, each represented by a tuple (width, index)
    rows = sorted((w, i) for i, w in enumerate(width))
    seats = [None]*num_row  # Initialize the seating arrangement

    # Create two lists, boys_rows and girls_rows
    boys_rows, girls_rows = [], []
    for person, (width, index) in zip(seq, rows):
        if person == '0':  # Boy
            boys_rows.append(index)
            seats[index] = 'B'  # Boy sits here
        else:  # Girl
            boys_rows.pop()  # Remove this row from boys_rows
            girls_rows.append(index)
            seats[index] += 'G'  # Girl sits here

    return seats
