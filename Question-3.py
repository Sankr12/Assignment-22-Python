# Write a recursive python function to calculate sum of first N even natural numbers

def even_sum(n):
    if n==1:
        return 2
    return (2*n)+even_sum(n-1)

num = int(input("Enter a number: "))
print(even_sum(num))