"""_decorators_main.py

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
from functools import wraps
from modules.with_classes import SeatingArrangement
from modules.with_heapq import hq_seat_arrange
from with_sort import with_sort, arrange_seats
from modules.with_zip_sorted import zip_seat_arrange

# ensure the logs folder exists
os.makedirs("src/logs", exist_ok=True)

# Constants
N = 2
S = "0011"
W = [2, 1]


def setup_logger(name):
    """Decorator to set up a logger.

    Args:
        name (str): The name of the logger.

    Returns:
        function: A wrapper function that sets up a logger, runs the decorated
        function, then removes the handler and closes it.
    """

    def logger_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(name)
            logger.setLevel(logging.INFO)
            handler = logging.FileHandler(f"src/logs/{name}.log")
            logger.addHandler(handler)
            result = func(logger, *args, **kwargs)
            logger.removeHandler(handler)
            handler.close()
            return result

        return wrapper

    return logger_decorator


def timer(func):
    """Decorator to measure the execution time of a function.

    Args:
        func (function): The function to be timed.

    Returns:
        function: A wrapper function that measures the execution time of the
        decorated function and logs it.
    """

    @wraps(func)
    def wrapper(logger, *args, **kwargs):
        start: float = timeit.default_timer()
        result = func(logger, *args, **kwargs)
        end: float = timeit.default_timer()
        logger.info("Execution time: %s", end - start)
        return result
    return wrapper


@setup_logger("class")
@timer
def run_class(logger):
    """Runs the SeatingArrangement class method.

    Args:
        logger (logging.Logger): The logger to log the execution time and result.

    Returns:
        list: The result of the SeatingArrangement class method.
    """
    return SeatingArrangement(N, S, W).arrange_seats()


@setup_logger("hq")
@timer
def run_hq(logger):
    """Runs the hq_seat_arrange method.

    Args:
        logger (logging.Logger): The logger to log the execution time and result.

    Returns:
        list: The result of the hq_seat_arrange method.
    """
    return hq_seat_arrange(N, S, W)


@setup_logger("standalone")
@timer
def run_standalone(logger):
    """Runs the sort_seats and arrange_seats methods.

    Args:
        logger (logging.Logger): The logger to log the execution time and result.

    Returns:
        list: The result of the arrange_seats method.
    """
    seats = with_sort(W)
    return arrange_seats(N, S, seats)


@setup_logger("zip")
@timer
def run_zip(logger):
    """Runs the zip_seat_arrange method.

    Args:
        logger (logging.Logger): The logger to log the execution time and result.

    Returns:
        list: The result of the zip_seat_arrange method.
    """
    return zip_seat_arrange(N, S, W)


def main():
    """Execute and compare the outputs of four implementations of a seating arrangement algorithm."""

    test_runs = 5
    pause_time = 1

    for _ in range(test_runs):
        # Using the class:
        run_class()
        time.sleep(pause_time)

        # Using heapq:
        run_hq()
        time.sleep(pause_time)

        # Using standalone functions:
        run_standalone()
        time.sleep(pause_time)

        # Using zip and sorted:
        run_zip()
        time.sleep(pause_time)


if __name__ == "__main__":
    main()
