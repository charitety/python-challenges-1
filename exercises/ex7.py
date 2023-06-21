# Sets
# Implement a function that takes two sets of integers as input and returns 
# a new set containing the intersection of the two sets.

def find_intersection(set1, set2):
    # Your code here
    # Using build-in methods:
    # newSet = set1.intersection(set2)
    # return newSet
    newSet = []
    for i in set1:
        if i in set2:
            newSet.append(i)
    return set(newSet)


# Test the function
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(find_intersection(set1, set2))  # Expected output: {4, 5}


# ----------------------------------------------------------------------------------------------------------


# Implement a function that takes two sets of integers as input and returns a new set containing 
# the unique elements from both sets.

def merge_sets(set1, set2):
    # Your code here
    # Using built-in methods:
    # newSet = set1.union(set2)
    # return newSet

    newSet2 = list(set1)
    for i in set2:
        if i not in set1:
            newSet2.append(i)
    return set(newSet2)


# Test the function
print(merge_sets(set1, set2))  # Expected output: {1, 2, 3, 4, 5, 6, 7, 8}
