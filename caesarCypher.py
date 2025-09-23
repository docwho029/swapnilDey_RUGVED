# 9) Write a python function to encrypt a string using Ceasar’s Cipher

s = list(str(input("enter message: ")))
shift = int(input("enter shift: "))

s = ''.join( [ chr(ord(x)+shift) if ord(x.lower())+shift in range(97, 123) else (chr(ord(x)+shift-26) if ord(x)+shift > 122 else chr(ord(x)+shift+26) ) if x.isalpha()  else x for x in s ] )

# hi, to whoever's checking my code - i thought i was being super clever by using compact one-line syntax, 
# this very evidently backfired, because this is not readable in the slightest. 
#however, it works. i've basically taken multiple nested if-else loops for each letter. 
# if letter ascii value > z, then subtract by 26. else add by 26.
# this is pretty much my logic. more than willing to explain in person if required. cheers.

print(s)

'''
z = 122
shift = 1
123 > 122
123 - 26

a = 97
shift = -1
96 < 97
''' 