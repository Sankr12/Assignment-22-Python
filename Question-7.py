# Write a recursive python function to calculate sum of the digits of a given number

def sum_of_digits(num):
    if num<10:
        return num
    return (num%10)+sum_of_digits(num//10)

number = int(input("Enter a number: "))
print(sum_of_digits(number))