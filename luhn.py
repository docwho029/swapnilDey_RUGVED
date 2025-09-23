# 10) Write a python function to check if a given credit card number is valid or not using Luhn’s Algorithm

s = str(input("enter credit card no. :")) 

#s = [ int(x) for x in list(s) ]          ---->   this does the same thing as line 5
s = list(map( lambda x: int(x), list(s) ))

# doubling every number whose index is odd (i.e position is even) in the reversed list ( as we need to take position from right ), and then reversing the list again.
s = [ number*2 if index%2 == 1 else number for index, number in enumerate(s[::-1]) ][::-1]

# sum digits of two-digit elements 
s = [ sum(list(map( lambda m : int(m), list(str(x)) ))) if x>9 else x for x in s ]
# s = [ sum( int(d) for d in str(x) ) if x>9 else x for x in s ]      ----->     this does the same thing as line 12

print( "valid" if sum(s)%10 == 0 else "invalid" )