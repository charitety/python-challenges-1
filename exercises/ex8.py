# Dicts
# Implement a function that takes a dictionary of student names and their ages as input 
# and returns the name of the oldest student.

def find_oldest_student(students):
    # Using a build-in method
    # return (max(students))
    oldest = 0
    for student in students:
        if student.value() > oldest:
            oldest = student.value




# Test the function
students = {"Alice": 18, "Bob": 20, "Charlie": 19, "David": 22}
print(find_oldest_student(students))  # Expected output: "David"
