# Write a recursive python function to print binary of a given decimal number

def binary_num(num):
    if num<=1:
        return str(num)
    return binary_num(num//2)+str(num%2)

number = int(input("Enter a number: "))
binary_representation=binary_num(number)
print("Binary Representation of",number,"is",binary_representation)