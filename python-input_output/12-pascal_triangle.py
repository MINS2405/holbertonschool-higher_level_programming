#!/usr/bin/python3
'''
This line tells the system to use Python 3 to run this script
'''


def pascal_triangle(n):
    if n <= 0:
        return []
        '''
        Return an empty list if n is not positive
        '''

    triangle = []
    '''
    Initialize the triangle as an empty list
    '''

    for row_num in range(n):
        row = [1]
        '''
        Every row starts with 1
        '''

        if triangle:
            '''
            If this is not the first row
            '''
            last_row = triangle[-1]
            '''
            Get the previous row to calculate the new values
            '''
            for i in range(1, row_num):
                row.append(last_row[i-1] + last_row[i])
                '''
                Add the sum of two numbers above for
                the middle elements
                '''
            row.append(1)
            '''
            Every row ends with 1
            '''

        triangle.append(row)
        '''
        Add the current row to the triangle
        '''

    return triangle
    '''
    Return the complete triangle
    '''
