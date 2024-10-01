#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""

def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        return []

    # Initialize the triangle with the first row, which is always [1]
    triangles = [[1]]

    # Continue generating rows until we have n rows
    while len(triangles) != n:
        # Get the last row of the current triangle
        tri = triangles[-1]

        # Initialize the new row with the first element, which is always 1
        tmp = [1]

        # Calculate the elements of the new row
        for i in range(len(tri) - 1):
            # Each element is the sum of the two elements directly above it in the previous row
            tmp.append(tri[i] + tri[i + 1])

        # Add the last element of the new row, which is always 1
        tmp.append(1)

        # Append the new row to the triangle
        triangles.append(tmp)

    # Return the completed Pascal's Triangle
    return triangles

