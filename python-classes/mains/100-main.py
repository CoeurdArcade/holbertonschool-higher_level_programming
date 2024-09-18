#!/usr/bin/python3

# Import the SinglyLinkedList class from the module
from singly_linked_list import SinglyLinkedList

# Create an instance of SinglyLinkedList
sll = SinglyLinkedList()

# List of values to be inserted in the sorted order
values_to_insert = [2, 5, 3, 10, 1, -4, -3, 4, 5, 12, 3]

# Insert each value into the sorted linked list
for value in values_to_insert:
    sll.sorted_insert(value)

# Print the sorted linked list
print(sll)

