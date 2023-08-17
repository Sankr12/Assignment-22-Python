# Write a recursive python function to print octal of a given decimal number
def octal_num(num):
    if num < 8:
        return str(num)
    return octal_num(num // 8) + str(num % 8)

number = int(input("Enter a number: "))
octal_representation = octal_num(number)
print("Octal representation of", number, "is", octal_representation)
