# 3) Write a python program to check if given number is a hill number

n = str(input("enter n: "))
m = "hill number" if n == n[0]*int(n[0]) else "not hill number"
print(m)