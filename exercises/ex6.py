# Tuples
# Implement a function that takes a tuple of strings as input and returns a new tuple 
# containing only the strings that start with an uppercase letter.

def filter_uppercase_strings(strings):
    newList = []
    for element in strings:
        if element[0].isupper():
            newList.append(element)
    return tuple(newList)

# Test the function
strings = ("Apple", "banana", "Cat", "dog", "Elephant", "Frog")
print(filter_uppercase_strings(strings))  # Expected output: ("Apple", "Cat", "Elephant")
