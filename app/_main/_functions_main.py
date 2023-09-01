"""_functions_main.py

This module provides four implementations of a seating arrangement algorithm
and uses decorators to measure the execution time and handle logging.

The algorithm finds a possible arrangement of people entering a hall
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

import os
import time
import timeit
import logging
from logging import Logger, FileHandler
from modules.with_classes import SeatingArrangement
from modules.with_heapq import hq_seat_arrange
from with_sort import sort_seats, arng_seats
from modules.with_zip_sorted import zip_seat_arrange

# ensure the logs folder exists
os.makedirs("src/logs", exist_ok=True)

# Constants
N = 2
S = "0011"
W = [2, 1]


def setup_logger(name) -> tuple[Logger, FileHandler]:
    """Set up a logger with the specified name and return it."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(f"src/logs/{name}.log")
    logger.addHandler(handler)
    return logger, handler


def run_and_log(logger, function, *args, **kwargs):
    """
    Run a function, log its output and execution time, and return its output.
    """
    start: float = timeit.default_timer()
    output = function(*args, **kwargs)
    end: float = timeit.default_timer()
    logger.info(output)
    logger.info("Execution time: %s", end - start)
    return output


def cleanup_logger(logger, handler) -> None:
    """Remove the handler from the logger and close the handler."""
    logger.removeHandler(handler)
    handler.close()


def test_run(name, function, *args, **kwargs) -> None:
    """
    Perform a single test run of a function, including setup, execution,
    logging, and cleanup.
    """
    logger, handler = setup_logger(name)
    run_and_log(logger, function, *args, **kwargs)
    cleanup_logger(logger, handler)


def main() -> None:
    """
    Execute and compare the outputs of four implementations of a seating
    arrangement algorithm.
    """
    test_runs = 5
    pause_time = 1

    for _ in range(test_runs):
        # Using the class:
        test_run("class", SeatingArrangement(N, S, W).arrange_seats)
        time.sleep(pause_time)

        # Using heapq:
        test_run("hq", hq_seat_arrange, N, S, W)
        time.sleep(pause_time)

        # Using standalone functions:
        seats = sort_seats(W)
        test_run("standalone", arng_seats, N, S, seats)
        time.sleep(pause_time)

        # Using zip and sorted:
        test_run("zip", zip_seat_arrange, N, S, W)
        time.sleep(pause_time)


if __name__ == "__main__":
    main()
