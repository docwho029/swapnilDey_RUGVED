# 5) Find the fabonacci of a given number using recursion.

n = int(input("enter n: "))

def f(a):
    if a==1:
        return 0
    if a==2:
        return 1
    return f(a-1) + f(a-2)

print( f(n) )