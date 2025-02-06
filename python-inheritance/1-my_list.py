#!/usr/bin/python3
class MyList(list):
    """A custom list class that inherits from the built-in list class."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
