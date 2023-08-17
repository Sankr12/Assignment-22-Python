# Write a recursive python function to calculate sum of cubes of first N natural numbers

def cubes_sum(n):
    if n==1:
        return 1
    return n**3+cubes_sum(n-1)

num = int(input("Enter a number: "))
print(cubes_sum(num))