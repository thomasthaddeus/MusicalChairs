"""main.py
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
import logging
from modules.with_classes import SeatingArrangement
from modules.with_heapq import hq_seat_arrange
from modules.with_standalone import sort_seats, arrange_seats
from modules.with_zip_sorted import zip_seat_arrange

# Constants
N = 2 # number of rows
S = "0011" # sequence
W = [2, 1] # width


def main() -> None:
    """
    Executes and compares the outputs of four implementations of a seating
    arrangement algorithm.

    The implementations are executed with the same input, their outputs and
    their execution times are logged into separate files.
    """

    # adjust this to change the number of times each test is run
    test_runs = 5
    # adjust this to change the length of the pause between tests (in seconds)
    pause_time = 1

    for i in range(test_runs):
        # set up a separate logger for each method
        class_logger = logging.getLogger("class")
        class_logger.setLevel(logging.INFO)
        hq_logger = logging.getLogger("hq")
        hq_logger.setLevel(logging.INFO)
        standalone_logger = logging.getLogger("standalone")
        standalone_logger.setLevel(logging.INFO)
        zip_logger = logging.getLogger("zip")
        zip_logger.setLevel(logging.INFO)

        # set up a file handler for each logger
        class_handler = logging.FileHandler("src/app/logs/class.log")
        hq_handler = logging.FileHandler("src/app/logs/hq.log")
        standalone_handler = logging.FileHandler("src/app/logs/standalone.log")
        zip_handler = logging.FileHandler("src/app/logs/zip.log")

        # add the handlers to the loggers
        class_logger.addHandler(class_handler)
        hq_logger.addHandler(hq_handler)
        standalone_logger.addHandler(standalone_handler)
        zip_logger.addHandler(zip_handler)

        # Using the class:
        class_logger.info("\nTest run %s:", i+1)
        start: float = timeit.default_timer()
        arrangement = SeatingArrangement(N, S, W)
        class_logger.info(arrangement.arrange_seats())
        end: float = timeit.default_timer()
        class_logger.info("Execution time: %s", end - start)

        time.sleep(pause_time)

        # Using heapq:
        hq_logger.info("\nTest run %s:", i+1)
        start = timeit.default_timer()
        hq_logger.info(hq_seat_arrange(N, S, W))
        end = timeit.default_timer()
        hq_logger.info("Execution time: %s", end - start)

        time.sleep(pause_time)

        # Using standalone functions:
        standalone_logger.info("\nTest run %s:", i+1)
        start = timeit.default_timer()
        seats = sort_seats(W)
        standalone_logger.info(arrange_seats(N, S, seats))
        end = timeit.default_timer()
        standalone_logger.info("Execution time: %s", end - start)

        time.sleep(pause_time)

        # Using zip and sorted:
        zip_logger.info("\nTest run %s:", i+1)
        start = timeit.default_timer()
        zip_logger.info(zip_seat_arrange(N, S, W))
        end = timeit.default_timer()
        zip_logger.info("Execution time: %s", end - start)

        time.sleep(pause_time)

        # remove the handlers at the end of each test run
        class_logger.removeHandler(class_handler)
        hq_logger.removeHandler(hq_handler)
        standalone_logger.removeHandler(standalone_handler)
        zip_logger.removeHandler(zip_handler)

        # close the handlers at the end of each test run
        class_handler.close()
        hq_handler.close()
        standalone_handler.close()
        zip_handler.close()


if __name__ == "__main__":
    main()
