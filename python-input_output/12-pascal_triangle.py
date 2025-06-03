#!/usr/bin/python3
'''
This line tells the system to use Python 3 to run this script
'''


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n.
    """
    if n <= 0:
        return []
        '''
        Return an empty list if n is not positive
        '''

    triangle = [[1]]
    '''
    Initialize the triangle with the first row [1]
    '''

    for i in range(1, n):
        prev_row = triangle[-1]
        '''
        Get the previous row to build the new one
        '''
        new_row = [1]
        '''
        Every new row starts with 1
        '''

        for j in range(len(prev_row) - 1):
            new_row.append(prev_row[j] + prev_row[j + 1])
            '''
            Add the sum of two adjacent numbers from the previous row
            '''

        new_row.append(1)
        '''
        Every new row ends with 1
        '''
        triangle.append(new_row)
        '''
        Add the new row to the triangle
        '''

    return triangle
    '''
    Return the complete triangle
    '''
