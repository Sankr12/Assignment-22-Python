# Write a recursive python function to calculate sum of squares of first N natural numbers

def square_sum(n):
    if n==1:
        return 1
    return n**2+square_sum(n-1)

num = int(input("Enter a number: "))
print(square_sum(num))