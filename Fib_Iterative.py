"""This is the code for printing Fibonacci sequence until a user specified limit"""
# Iterative Process

Fib = []
Fib.append(1)
Fib.append(1)

n = int(input("Enter the limit: "))
for i in range(2,n):
    Fib.append(Fib[i-2]+Fib[i-1])

print(Fib)