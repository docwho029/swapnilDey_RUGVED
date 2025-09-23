# 7) Write a program to print the Fibonacci Sequence till n-values where n is user input.

n = int(input("enter n: "))

def f(a):
    if a==1:
        return 0
    if a==2:
        return 1
    return f(a-1) + f(a-2)

for i in range(1, n+1):
    print( f(i) , end=' ')