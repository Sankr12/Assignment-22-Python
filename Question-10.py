# Write a recursive python function to find the Nth term of the fibonacci series.

def fibbo_series(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return fibbo_series(n-1)+fibbo_series(n-2)

num = int(input("Enter a number: "))
result = fibbo_series(num)
print("The {}th term of fibonacci series is {}".format(num,result))