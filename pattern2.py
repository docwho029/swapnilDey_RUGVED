n = int(input("enter n:"))

for i in range(1, n):
    for j in range(i):
        print('*', end='')
    for k in range( 2 * (n-i) - 1 ):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()

print('*'*(2*n-1))

for i in range(n-1, 0, -1):
    for j in range(i):
        print('*', end='')
    for k in range(2*(n-i)-1):
        print(' ', end='')
    for l in range(i):
        print('*', end='')
    print()
    