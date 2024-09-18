#!/usr/bin/python3
Square = __import__('102-square').Square

# Create square objects
s_5 = Square(5)
s_6 = Square(6)

# Define a dictionary of comparison operators and their corresponding strings
comparisons = {
    '<': 'Square 5 < Square 6',
    '<=': 'Square 5 <= Square 6',
    '==': 'Square 5 == Square 6',
    '!=': 'Square 5 != Square 6',
    '>': 'Square 5 > Square 6',
    '>=': 'Square 5 >= Square 6'
}

# Iterate over the comparisons and print the results
for op, message in comparisons.items():
    if eval(f's_5 {op} s_6'):
        print(message)

