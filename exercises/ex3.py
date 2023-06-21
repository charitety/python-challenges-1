# Exercise 3: Loops
# TODO: Write code that prints all between 1 and n using a while loop
# TODO: Write code that prints all the even numbers between 1 and n using a for loop

def main(n):
    print("All numbers from 1 to n:")
    i = 0
    # use a while loop
    while i < n:
        i += 1
        print(i)

    print("Even numbers between 1 and n:")
    # even numbers from 1-n (for loop)
    for num in range(2,n+1,2):
        print(num)


    #While loop:
    # i = 0
    # while i < n:
    #     i += 1
    #     if i%2 == 0:
    #         print(i)



main(12)