# 14) Given an array arr[], find the first repeating element. The element should occur more than once and the index of its first occurrence should be the smallest.

n = eval(input("enter array: "))
#x = list(filter( lambda i : i != None , [ i if n.count(i)>1 else None for i in n ] ))     <---- initial attempt, didn't work bc it doesn't count first repeating element. counts first element whose first elem is the earliest index
for index, elem in enumerate(n):
    if elem in n[:index]:
        print(n[index])
        break
