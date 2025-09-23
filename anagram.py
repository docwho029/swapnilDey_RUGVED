# 6) Create a function that checks whether given string is an anagram or not?

s = str(input("enter string:"))
if s == s[::-1]:
    print("anagram")
else:
    print("not anagram")