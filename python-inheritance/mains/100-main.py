#!/usr/bin/python3

# Import the MyInt class from the module '100-my_int'
MyInt = __import__('100-my_int').MyInt

# Create an instance of MyInt with the value 3
my_i = MyInt(3)

# Print the value of the MyInt instance
print(my_i)

# Print the result of the equality comparison between my_i and 3
print(my_i == 3)

# Print the result of the inequality comparison between my_i and 3
print(my_i != 3)

