---
format: default
title: Musical Chairs
author: Thaddeus Thomas
---

[![Deploy Jekyll with GitHub Pages dependencies preinstalled](https://github.com/thomasthaddeus/musical-chairs/actions/workflows/jekyll-gh-pages.yml/badge.svg)](https://github.com/thomasthaddeus/musical-chairs/actions/workflows/jekyll-gh-pages.yml)

This project contains implementations of a seating arrangement algorithm using four different approaches: using a class, using Python's heapq module, using standalone functions, and using Python's zip function along with the built-in sorted function.

## Directory Structure

The project has the following directory structure:

```markdown
.
├── .gitignore
├── LICENSE.md
├── README.md
├── src
│   ├── logs
│   │   ├── class.log
│   │   ├── hq.log
│   │   ├── standalone.log
│   │   └── zip.log
│   ├── _main
│   │   ├── _decorators_main.py
│   │   └── _functions_main.py
│   ├── main.py
│   ├── modules
│   │   ├── __init__.py
│   │   ├── with_classes.py
│   │   ├── with_heapq.py
│   │   ├── with_standalone.py
│   │   └── with_zip_sorted.py
│   └── tests
│       ├── __init__.py
│       ├── __pycache__
│       ├── test_with_classes.py
│       ├── test_with_heapq.py
│       ├── test_with_standalone.py
│       └── test_with_zip_sorted.py
└── .vscode
    └── settings.json
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

To run the tests, you will need to install pytest 

```python
pip install pytest
```

Then you can run pytest command from your terminal at the root directory of the project.
