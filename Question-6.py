# Write a recursive python function to calculate the factorial of a number

def factorial_(n):
    if n==1:
        return 1
    return n*factorial_(n-1)

num = int(input("Enter a number: "))
print(factorial_(num))