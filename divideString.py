# 8) Write a python program to divide a given string into equal parts containing n(user input) characters of same sequence. Example: string=“abcdabcdabcdabcd” n=4 output: “abcd”, “abcd”, “abcd”, “abcd” If the division is not possible or the sequence cannot be same, print out the appropriate error.

def main():
    #s = 'abcdabcdabcd' 
    #n = 4
    s = str(input("enter string:"))
    n = int(input("enter integer:"))
    a = s[:n]

    if len(s)%n != 0:
        print('division not feasible')
        return
    
    while s != '':
        if s[n:2*n] == '':
            break
        if s[:n] != s[n:2*n]:
            print('segments equal in length but not identical')
            return
        s = s[n:]

    for i in range(n):
        print(a, end=' ')

if __name__ == "__main__":
    main()
