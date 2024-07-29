"""Recursive code for printing first n(user specified) Fibonacci Numbers, No.of function calls."""

count = 0
def Fib(n):
    global count
    count += 1
    if n==1 or n==2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)

n = int(input("Enter the no. of Fibonacci numbers you want: "))
print(Fib(n))
print(count)