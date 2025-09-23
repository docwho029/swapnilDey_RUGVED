#2) Write a python program to sort a string alphabetically and print the count of each character.
    
s = 'aabbb3211'
s = list(s)
s.sort()

a = list(set(s))
a.sort()

for i in a:
    print(i, '\'s count : ', s.count(i), sep='')