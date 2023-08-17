# Write a recursive python function to calculate sum of first N natural numbers

def sum_natural(N):
    if N>0:
        return N+sum_natural(N-1)
    else:
        return 0

value = int(input("Enter a number: "))
a=sum_natural(value)
print(a)
