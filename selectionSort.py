# 4) Write a python function to perform selection sort on a given string.

s = str(input("enter string: "))
l = [ord(i) for i in s]

for i in range( len(l) - 1 ):
    minIndex = l.index( min(l[i:]) , i)
    l[i], l[minIndex] = l[minIndex], l[i]

result = ''.join( map(lambda x : chr(x) , l) )

print(result)
