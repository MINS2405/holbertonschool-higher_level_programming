#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples."""
    a = list(tuple_a)
    b = list(tuple_b)

    # Ensure both tuples have at least 2 elements
    while len(a) < 2:
        a.append(0)
    while len(b) < 2:
        b.append(0)

    # Add the first two elements of each tuple
    return (a[0] + b[0], a[1] + b[1])


if __name__ == "__main__":
    tuple_a = (89, 100)
    tuple_b = (2, 89)
    tuple_c = (1, 89)
    result = add_tuple(tuple_a, tuple_b, tuple_c)
    print("Result:", result)  # Output: Result: (90, 189)
