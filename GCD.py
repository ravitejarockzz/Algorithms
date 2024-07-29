"""SIR EUCLID'S ALGORITHM (Iterative)"""
# Without using Division and Remainder operators

n1 = int(input("Enter the Number1: "))
n2 = int(input("Enter the Number2: "))

num1 = n1
num2 = n2

while (n1!=n2):
    if n1>n2:
        n1 = n1-n2
    else:   #n1<n2
        n2 = n2-n1
else:
    print (f"GCD of {num1}, {num2} is {n1}")