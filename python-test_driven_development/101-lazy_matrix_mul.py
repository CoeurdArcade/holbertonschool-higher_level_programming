#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Returns:
        list of lists of ints/floats: The resulting matrix.

    Raises:
        TypeError: If m_a or m_b is not a list of lists of ints/floats.
        ValueError: If m_a or m_b is empty, or if the matrices cannot be multiplied.
    """

    # Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    # Check if all elements in m_a and m_b are ints or floats
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")

    # Check if all rows in m_a and m_b have the same length
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Convert lists to numpy arrays
    m_a_np = np.array(m_a)
    m_b_np = np.array(m_b)

    # Check if the matrices can be multiplied
    if m_a_np.shape[1] != m_b_np.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = np.matmul(m_a_np, m_b_np)

    # Convert the result back to a list of lists
    return result.tolist()

