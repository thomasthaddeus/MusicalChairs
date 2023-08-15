# Musical Chairs

[![Deploy Jekyll](https://github.com/thomasthaddeus/musical-chairs/actions/workflows/jekyll-gh-pages.yml/badge.svg)](https://github.com/thomasthaddeus/musical-chairs/actions/workflows/jekyll-gh-pages.yml) ![GitHub top language](https://img.shields.io/github/languages/top/thomasthaddeus/musical-chairs?logo=python&logoColor=yellow) ![GitHub repo size](https://img.shields.io/github/repo-size/thomasthaddeus/musical-chairs?logo=github)

## Table of Contents

<details markdown="1"><summary></summary>

- [Musical Chairs](#musical-chairs)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [The Musical Chairs Problem](#the-musical-chairs-problem)
  - [The Algorithm](#the-algorithm)
  - [The Web Application](#the-web-application)
  - [About the Project](#about-the-project)
    - [Built With](#built-with)
  - [Directory Structure](#directory-structure)
    - [Files Overview](#files-overview)
    - [Running the Tests](#running-the-tests)

</details>

## Introduction

This project is a simple web application that demonstrates the use of four different approaches to solving the musical chairs problem.

## The Musical Chairs Problem

Suppose that you are hosting a dinner party and have invited some number of guests. When the guests arrive, you realize that you don't have enough chairs for everyone. You decide to solve this problem by asking some of the guests to stand while the others sit. Your guests are all very close friends and have no preference for where they sit at the table, but you would like to maximize the number of guests sitting at the table.

## The Algorithm

The algorithm is implemented in four different ways. The basic idea is to sort the guests by their total number of friends. Then, starting with the guest with the most friends, assign them a seat at the table and remove them and all of their friends from the list of guests. Repeat this process until there are no guests remaining. The different implementations of the algorithm differ in how the guests are sorted.

## The Web Application

The web application is built using [Jekyll](https://jekyllrb.com). The source code for the web application is located in the `src` directory. The web application is deployed to GitHub Pages and can be accessed via the following link [Musical Chairs](https://apparellnstuff.me/musical-chairs/)

## About the Project

This project contains implementations of a seating arrangement algorithm using four different approaches:

1. using a class
2. using Python's `heapq` module
3. using standalone functions
4. using Python's `zip` function
   - with the built-in `sorted` function.

### Built With

- [Python](https://www.python.org/)
- [pytest](https://docs.pytest.org/en/6.2.x/)
- [Jekyll](https://jekyllrb.com)
<!-- - [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) -->

## Directory Structure

The project has the following directory structure:

```bash
.
├── .gitignore
├── LICENSE
├── README.md
└── src
    ├── app
    │   ├── main.py
    │   ├── pylint.rc
    │   ├── logs
    │   │   ├── class.log
    │   │   ├── hq.log
    │   │   ├── standalone.log
    │   │   └── zip.log
    │   ├── _main
    │   │   ├── _decorators_main.py
    │   │   └── _functions_main.py
    │   ├── modules
    │   │   ├── __init__.py
    │   │   ├── with_classes.py
    │   │   ├── with_heapq.py
    │   │   ├── with_standalone.py
    │   │   └── with_zip_sorted.py
    │   └── tests
    │       ├── __init__.py
    │       ├── test_main.py
    │       └── test_modules.py
    ├── css
    │   └── styles.css
    └── js
        ├── accordion.js
        ├── dropdown_enhancements.js
        ├── fetch.js
        ├── myModal.js
        └── smooth_scrolling.js
```

### Files Overview

- `README.md`: This file.
- `main.py`: This script executes each implementation and prints their outputs and execution times.
- `with_classes.py`: Implementation of the algorithm using a class.
- `with_heapq.py`: Implementation of the algorithm using Python's heapq module.
- `with_standalone.py`: Implementation of the algorithm using standalone functions.
- `with_zip_sorted.py`: Implementation of the algorithm using Python's zip function along with the built-in sorted function.
- `test_main.py`, `test_modules.py`: These are pytest files for testing each of the four implementations.

### Running the Tests

To run the tests, you will need to install pytest

   ```python
   pip install pytest
   ```

Then you can run pytest command from your terminal at the root directory of the project.
