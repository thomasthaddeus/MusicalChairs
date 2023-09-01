"""with_zip_sorted.py

This module provides a function, zip_seat_arrange, that determines the seating
arrangement in a hall based on a sequence of people entering and the widths of
the rows.

The function uses Python's built-in zip function to iterate over the sequence
of people and the rows in parallel. The algorithm follows these rules:
- Boys choose a row where both seats are free, and out of those rows, they pick
  the smallest one.
- Girls choose a row where one seat is taken by a boy, and out of those rows,
  they pick the largest one.

The rows are sorted by their widths at the start, and this ordering is used to
select the smallest free row for each boy and the largest occupied row for each girl.

This module offers an alternative, Pythonic approach to the seating arrangement
problem that takes advantage of Python's built-in functions and data structures.
"""

# def zip_seat_arrange(num_row, seq, width):
#     """Finds the seating arrangement according to the given rules.

#     Uses the zip function to iterate over the people and rows in parallel.
#     Boys choose a row where both seats are free, and out of those rows,
#     they pick the smallest one. Girls choose a row where one seat is taken
#     by a boy, and out of those rows, they pick the largest one.

#     Args:
#         num_row (int): The number of rows.
#         seq (str): The sequence of people entering.
#         width (List[int]): The widths of each row.

#     Returns:
#         List[str]: The list of rows with their current seat status.
#     """
#     # Create the list of rows, each represented by a tuple (width, index)
#     rows = sorted((w, i) for i, w in enumerate(width))
#     seats = [None]*num_row  # Initialize the seating arrangement

#     # Create two lists, boys_rows and girls_rows
#     boys_rows, girls_rows = [], []
#     for person, (width, index) in zip(seq, rows):
#         if person == '0':  # Boy
#             boys_rows.append(index)
#             seats[index] = 'B'  # Boy sits here
#         else:  # Girl
#             boys_rows.pop()  # Remove this row from boys_rows
#             girls_rows.append(index)
#             seats[index] += 'G'  # Girl sits here

#     return seats

def zip_seat_arrange(num_row, seq, width):
    # Create the list of rows, each represented by a tuple (width, index)
    rows = sorted((w, i) for i, w in enumerate(width))
    seats = [[w, False, False] for w in width]
    for person, (_, index) in zip(seq, rows):
        if person == '0':  # Boy
            seats[index][1] = True
        else:  # Girl
            seats[index][2] = True
    return seats
