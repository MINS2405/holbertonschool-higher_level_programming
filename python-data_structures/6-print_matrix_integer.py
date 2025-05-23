#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers."""
    for row in matrix:
        for i in range(len(row)):
            print("{:d}".format(row[i]), end="")
            if i < len(row) - 1:
                print(" ", end="")
        print()


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix_integer(matrix)
