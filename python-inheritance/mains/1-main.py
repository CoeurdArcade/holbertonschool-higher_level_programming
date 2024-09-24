#!/usr/bin/python3

# Import the MyList class from the '1-my_list' module
MyList = __import__('1-my_list').MyList

# Create an instance of MyList
my_list = MyList()

# Append elements to the list
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)

# Print the list to show the current state
print(my_list)

# Print the sorted version of the list
my_list.print_sorted()

# Print the list again to show that the original list remains unchanged
print(my_list)

