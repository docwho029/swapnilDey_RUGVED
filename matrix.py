# 15) Rotate an n*n matrix by 90° clockwise.Take a user input for a matrix and print the elements in spiral order

#first we rotate

mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

def rotate(m):
    r = len(m)
    c = len( m[0] )
    # transpose, then reverse each row
    for i in range( r ):
        for j in range ( i, c ):
            m[i][j] , m[j][i] = m[j][i] , m[i][j]
    
    for rowNo, row in enumerate(m):
        m[rowNo] = row[::-1]
    
    return m

def spiral(m):
    x = []
    top, bottom = 0, len(m) - 1
    left, right = 0, len(m[0]) - 1
    
    while top <= bottom and left <= right:

        for i in range(left, right + 1):  # upper boundary
            x.append( m[top][i] )
        top = top + 1

        for i in range(top, bottom + 1):  # rightward boundry
            x.append(m[i][right])
        right = right - 1

        if top <= bottom: 
            for i in range(right, left - 1, -1):  # lower boundary
                x.append(m[bottom][i])
            bottom = bottom - 1

        if left <= right:
            for i in range(bottom, top - 1, -1):  # leftward boundary
                x.append(m[i][left])
            left = left + 1

    return x

#print( rotate(mat) )
print ( spiral( rotate(mat) ) )
