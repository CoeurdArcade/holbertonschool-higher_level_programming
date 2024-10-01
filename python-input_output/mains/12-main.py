#!/usr/bin/python3
"""
12-main
"""

from pascal_triangle import pascal_triangle

def print_triangle(triangle: list[list[int]]) -> None:
    """
    Print the triangle.

    Args:
        triangle (list[list[int]]): A list of lists representing Pascal's triangle.
    """
    for row in triangle:
        # Use f-string for better readability and efficiency
        print(f"[{','.join(map(str, row))}]")

if __name__ == "__main__":
    # Generate Pascal's triangle with 5 rows and print it
    print_triangle(pascal_triangle(5))

