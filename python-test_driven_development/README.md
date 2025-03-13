# holbertonschool-higher_level_programming - python-test_driven_development

This repository contains Python projects focusing on test-driven development (TDD). The projects emphasize writing thorough tests before implementing the code, following the principles of TDD to ensure robust and well-documented solutions.

## Learning Objectives

This project aims to reinforce the following concepts:

*   **Python Awesomeness:** Understand why Python is a powerful and versatile programming language.
*   **Interactive Testing:** What interactive tests are and how they aid development.
*   **Importance of Tests:** Why writing tests is crucial for code quality and reliability.
*   **Docstrings for Tests:**  How to utilize Docstrings to embed tests within the code.
*   **Module and Function Documentation:**  Write comprehensive documentation for Python modules and functions.
*   **Test Option Flags:** Understand and use basic option flags when creating tests.
*   **Edge Case Identification:**  Develop the ability to identify and handle edge cases in code.

## General Requirements

*   **Editors:** vi, vim, emacs
*   **Environment:** Ubuntu 20.04 LTS, Python 3.8.5
*   **File Conventions:**
    *   All files must end with a newline.
    *   The first line of each Python script should be `#!/usr/bin/python3`.
    *   A `README.md` file at the root of the project is mandatory.
*   **Code Style:** pycodestyle (version 2.7.*)
*   **File Permissions:** All files must be executable.
*   **Code Length:** Your code will be checked for excessive length using `wc`.

## Python Test Cases Requirements

*   **Editors:** vi, vim, emacs
*   **File Conventions:**
    *   All files must end with a newline.
    *   Test files reside in a directory named `tests`.
    *   Test files must be text files with the extension `.txt` (for doctests) or `.py` (for unittests).
*   **Test Execution:**  `python3 -m doctest ./tests/*` or `python3 -m unittest tests.your_test_file`
*   **Documentation:**
    *   All modules and functions must have meaningful docstrings explaining their purpose.

## Project Tasks

Here's a breakdown of the tasks completed in this project:

### 0. Integers Addition (90%)

*   **File:** `0-add_integer.py`, `tests/0-add_integer.txt`
*   **Description:** A function `add_integer(a, b=98)` that adds two integers. Handles `TypeError` if inputs are not integers or floats, and casts floats to integers.
*   **Prototype:** `def add_integer(a, b=98):`


### 1. Divide a Matrix (84.62%)

*   **File:** `2-matrix_divided.py`, `tests/2-matrix_divided.txt`
*   **Description:** A function `matrix_divided(matrix, div)` that divides all elements of a matrix by a given number, rounded to 2 decimal places.  Includes error handling for invalid input types and division by zero.
*   **Prototype:** `def matrix_divided(matrix, div):`

### 2. Say My Name (91.67%)

*   **File:** `3-say_my_name.py`, `tests/3-say_my_name.txt`
*   **Description:** A function `say_my_name(first_name, last_name="")` that prints "My name is <first name> <last name>".  Includes type validation to ensure names are strings.
*   **Prototype:** `def say_my_name(first_name, last_name=""):`

### 3. Print Square (44%)

*   **File:** `4-print_square.py`, `tests/4-print_square.txt`
*   **Description:** A function `print_square(size)` that prints a square with the character `#`.  Handles `TypeError` and `ValueError` for invalid sizes.
*   **Prototype:** `def print_square(size):`

### 4. Text Indentation (100%)

*   **File:** `5-text_indentation.py`, `tests/5-text_indentation.txt`
*   **Description:** A function `text_indentation(text)` that prints a text with 2 new lines after each of these characters: `.`, `?`, and `:`.  Handles `TypeError` if input is not a string.
*   **Prototype:** `def text_indentation(text):`

### 5. Max Integer - Unittest (100%)

*   **File:** `6-max_integer.py`, `tests/6-max_integer_test.py`
*   **Description:**  Includes the function `max_integer(list=[])` to find the maximum integer in a list.  `tests/6-max_integer_test.py` contains unittest test cases for thorough testing of the function.

## Project Score

*   **Overall Project Score:** 85.03%

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## Author

https://github.com/MINS2405/holbertonschool-higher_level_programming/

