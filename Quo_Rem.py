"""Division without using division operator"""

dnd=int(input("Enter the Dividend: "))
div=int(input("Enter the Divisor: "))

quo = 0
rem = dnd

while(rem>=div):
    rem -= div
    quo += 1
print(quo,rem)