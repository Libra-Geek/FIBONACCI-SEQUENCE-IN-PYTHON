import math
n= int(input("enter how many numbers you want in this series:"))
first  = 0
second = 1
for i in range (n):
    print (first)
    step = first
    first = second
    second = step+second

