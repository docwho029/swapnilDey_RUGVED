# 11) Write a Python program that prints the grade level of a given text using Coleman-Liau formula.

# I've used the Harvard CS50 specifications given in their problem set.

s = str(input("Enter text: "))

words = len(s.split())
letters = sum(c.isalnum() for c in s)
sentences = s.count('. ') + s.count('?') + s.count('!')

# avg no of letters per 100 words
L = (letters*100) / words
# avg no of sentences per 100 words
S = (sentences*100) / words

index = 0.0588 * L - 0.296 * S - 15.8
print(index)
