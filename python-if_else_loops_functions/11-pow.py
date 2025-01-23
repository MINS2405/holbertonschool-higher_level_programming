def pow(a, b):
    """
    Computes a to the power of b and returns the value.
    
    Args:
    a (int or float): The base number
    b (int): The exponent
    
    Returns:
    int or float: The result of a^b
    """
    # Base case: any number to the power of 0 is 1
    if b == 0:
        return 1
    
    # Handle negative exponents
    if b < 0:
        return 1 / pow(a, -b)
    
    # Recursive case
    return a * pow(a, b - 1)