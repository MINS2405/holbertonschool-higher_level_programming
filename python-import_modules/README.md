# Python Import & Modules Project

## Description

This project is designed to help you practice importing functions, variables, and modules in Python, as well as handling command-line arguments.  
You will learn how to:

- Import functions or variables from other Python files
- Use arguments passed to the script via the command line (`sys.argv`)
- Understand and use the special variable `__name__` to prevent code from executing when imported
- Create and use Python modules
- Use the built-in `dir()` function to explore module attributes
- Follow the `pycodestyle` style guide

## Files Included

- `0-add.py`: Imports an addition function and prints the result of 1 + 2
- `1-calculation.py`: Imports several math functions and prints results for 10 and 5
- `2-args.py`: Prints the number and list of arguments passed to the script
- `3-infinite_add.py`: Adds all arguments passed to the script
- `4-hidden_discovery.py`: Prints all names defined in the compiled module `hidden_4.pyc` (excluding special names)
- `5-variable_load.py`: Imports and prints the value of a variable from another file

## Usage

To run a script, use:

python3 <script_name.py> [arguments]

Example:

python3 2-args.py Hello World


## Best Practices

- Always start your files with `#!/usr/bin/python3`
- Use `if __name__ == "__main__":` to prevent code from running on import
- Follow the `pycodestyle` standard (check with `pycodestyle <file.py>`)
- Never use `import *` or `__import__`
- Comment your code to explain each step

## Useful Resources

- [Python documentation on modules](https://docs.python.org/3/tutorial/modules.html)
- [Command-line arguments in Python](https://realpython.com/python-command-line-arguments/)
- [pycodestyle – Python style guide](https://pycodestyle.pycqa.org/en/latest/)

---

**Project completed as part of Holberton School – Higher Level Programming**

This README explains:

* The project goals

* The content of each file

* How to run the scripts

* Best practices for Python code

* Useful documentation links

You can adapt it as needed for your repository!
