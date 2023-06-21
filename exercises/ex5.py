# Lists 
# Implement a function that takes a list of numbers as input and returns the sum of all the even numbers in the list.

def sum_even_numbers(numbers):
    addNumber = 0
    i = 0
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            addNumber = addNumber+numbers[i]
        i += 1
    return addNumber

# Test the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_even_numbers(numbers))  # Expected output: 30
