#!/usr/bin/env python3
from task_02_verboselist import VerboseList

def main():
    # Initialize VerboseList with initial elements
    vl = VerboseList([1, 2, 3])

    # Append an element
    vl.append(4)

    # Extend the list with additional elements
    vl.extend([5, 6])

    # Remove an element if it exists
    try:
        vl.remove(2)
    except ValueError as e:
        print(f"Error: {e}")

    # Pop the last element
    try:
        vl.pop()
    except IndexError as e:
        print(f"Error: {e}")

    # Pop the first element
    try:
        vl.pop(0)
    except IndexError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

