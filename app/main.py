"""main.py
This module benchmarks four implementations of a seating arrangement algorithm.

The algorithm determines the seating arrangement of people entering a hall
based on:
    - Boys choosing a row where both seats are free, selecting the smallest row.
    - Girls choosing a row where one seat is occupied by a boy, selecting the
      largest row.

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
from with_sort import sort_seats, arng_seats
from modules.with_zip_sorted import zip_seat_arrange

# Constants
N = 2  # number of rows
S = "0011"  # sequence
W = [2, 1]  # width of rows


def run_and_log(method, logger, *args):
    """
    Execute a method, log its output and execution time.

    Args:
        method (callable): The method to be executed.
        logger (logging.Logger): Logger to log the results and execution time.
        *args: Variable length argument list for the method.
    """
    try:
        start = timeit.default_timer()
        result = method(*args)
        end = timeit.default_timer()
        logger.info(result)
        logger.info("Execution time: %s", end - start)
    except (IndexError, TypeError, ValueError) as err:
        logger.error(f"Error executing method: {err}")


def benchmark_methods(test_runs, pause_time, loggers):
    """
    Benchmark the seating arrangement methods and log their outputs and execution times.

    Args:
        test_runs (int): Number of times each method is executed.
        pause_time (float): Time in seconds to pause between each method execution.
        loggers (dict): Dictionary of loggers for each method.
    """
    for i in range(test_runs):
        for _, logger in loggers.items():
            logger.info("\nTest run %s:", i + 1)

        # Using the class:
        run_and_log(lambda: SeatingArrangement(N, S, W).arrange_seats(), loggers["class"])
        time.sleep(pause_time)

        # Using heapq:
        run_and_log(hq_seat_arrange, loggers["hq"], N, S, W)
        time.sleep(pause_time)

        # Using standalone functions:
        seats = sort_seats(W)
        run_and_log(arng_seats, loggers["standalone"], N, S, seats)
        time.sleep(pause_time)

        # Using zip and sorted:
        run_and_log(zip_seat_arrange, loggers["zip"], N, S, W)
        time.sleep(pause_time)


def main() -> None:
    """
    Executes and compares the outputs of four implementations of a seating
    arrangement algorithm.

    The implementations are executed with the same input, and their outputs and
    execution times are logged into separate files.
    """
    # adjust this to change the number of times each test is run
    test_runs = 5
    # adjust this to change the length of the pause between tests (in seconds)
    pause_time = 1

    # set up a separate logger for each method
    loggers = {
        "class": logging.getLogger("class"),
        "hq": logging.getLogger("hq"),
        "standalone": logging.getLogger("standalone"),
        "zip": logging.getLogger("zip")
    }

    handlers = {
        "class": logging.FileHandler("src/app/logs/class.log"),
        "hq": logging.FileHandler("src/app/logs/hq.log"),
        "standalone": logging.FileHandler("src/app/logs/standalone.log"),
        "zip": logging.FileHandler("src/app/logs/zip.log")
    }

    for name, logger in loggers.items():
        logger.setLevel(logging.INFO)
        logger.addHandler(handlers[name])

    # Run the benchmark
    benchmark_methods(test_runs, pause_time, loggers)

    # close the handlers at the end of the script
    for handler in handlers.values():
        handler.close()


if __name__ == "__main__":
    main()
