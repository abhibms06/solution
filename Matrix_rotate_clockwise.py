
# Rotate square matrix clockwise


print('Enter square matrix size : ')
n = int(input().strip())

mat =  []
for i in range(n):
    mat.append([int(tmp) for tmp in input().strip().split()])

print(mat)

for x in range(int(n/2)):
    y = x
    while y < n-1-x:

        top = mat[x][y]

        #TL (Move BL to TL)
        mat[x][y] = mat[n-1-y][x]

        #BL (Move BR to BL)
        mat[n-1-y][x] = mat[n-1-x][n-1-y]

        #BR(Move TR to BR)
        mat[n-1-x][n-1-y] = mat[y][n-1-x]

        #TR (Move TL to TR)
        mat[y][n-1-x] = top

        y = y + 1



for i in range(n):
    for j in range(n):
        print(mat[i][j],sep='')
    print()



