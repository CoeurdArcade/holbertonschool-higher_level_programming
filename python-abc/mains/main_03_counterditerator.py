#!/usr/bin/env python3
from task_03_countediterator import CountedIterator

# Sample data
data = [1, 2, 3, 4]

# Create a CountedIterator object
counted_iter = CountedIterator(data)

# Iterate over the CountedIterator
for item in counted_iter:
    # Print the current item and the total count of items iterated
    print(f"Got {item}, total {counted_iter.get_count()} items iterated.")

# Print a message when iteration is complete
print("No more items.")

