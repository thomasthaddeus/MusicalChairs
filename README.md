# Seating Arrangement Comparison Project

This project contains implementations of a seating arrangement algorithm using four different approaches: using a class, using Python's heapq module, using standalone functions, and using Python's zip function along with the built-in sorted function.

## Directory Structure

The project has the following directory structure:

```markdown
.
├── README.md
├── src
│   ├── main.py
│   └── python
│       ├── __init__.py
│       ├── with_classes.py
│       ├── with_heapq.py
│       ├── with_standalone.py
│       └── with_zip_sorted.py
└── test
    ├── __pycache__
    │   ├── test_with_classes.cpython-311-pytest-7.3.1.pyc
    │   ├── test_with_heapq.cpython-311-pytest-7.3.1.pyc
    │   ├── test_with_standalone.cpython-311-pytest-7.3.1.pyc
    │   └── test_with_zip_sorted.cpython-311-pytest-7.3.1.pyc
    ├── test_with_classes.py
    ├── test_with_heapq.py
    ├── test_with_standalone.py
    └── test_with_zip_sorted.py
```

### Files Overview

- `README.md`: This file.
- `main.py`: This script executes each implementation and prints their outputs and execution times.
- `with_classes.py`: Implementation of the algorithm using a class.
- `with_heapq.py`: Implementation of the algorithm using Python's heapq module.
- `with_standalone.py`: Implementation of the algorithm using standalone functions.
- `with_zip_sorted.py`: Implementation of the algorithm using Python's zip function along with the built-in sorted function.
- `test_with_classes.py`, `test_with_heapq.py`, `test_with_standalone.py`, `test_with_zip_sorted.py`: These are pytest files for testing each of the four implementations.

### Running the Tests

To run the tests, you will need to install pytest (pip install pytest), and then you can run pytest command from your terminal at the root directory of the project.
