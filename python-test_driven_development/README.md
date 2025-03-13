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

