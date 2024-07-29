import math
list = [1,1,2,2,2,2,5,5,8]

"""
n = int(input("Enter the no. of elements: "))
for i in range(n):
    list.append(int(input(f'element {i+1}:')))
"""

x = int(input("Enter the element to be searched: "))

l = 0
r = len(list)-1
index = -1
while(r != (l+1)):
    m = math.ceil((l+r)/2)
    #print(l,r,"mid: ",m)
    if (list[m] < x):
        l=m
    elif (list[m]>x):
        r=m
    elif (list[m]==x):
        if list[m+1]>x:
            index = m
            break
        elif list[m+1]==x:
            l=m
    #print(l,r)
if (index==-1):
    """
    if list[l]==x:
        if list[r]==x:
            index=r
        elif list[r]>x:
            index=l
    elif list[r]==x:
        index=r
    """
    if list[r]==x:
        index = r
    elif list[l]==x:
        index = l
print("Index: ",index)