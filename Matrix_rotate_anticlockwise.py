# Rotate square matrix anticlockwise


print('Enter square matrix size : ')
n = int(input().strip())

mat =  []
for i in range(n):
    mat.append([int(tmp) for tmp in input().strip().split()])

print(mat)

for x in range(int(n/2)):
    y = x
    while y < n-1-x:

        # Save top left element
        top = mat[x][y]

        #TL (Move TR to TL)
        mat[x][y] = mat[y][n-1-x]

        #TR( Move BR to TR)
        mat[y][n-1-x] = mat[n-1-x][n-1-y]

        # BR (Move BL to BR)
        mat[n-1-x][n-1-y] = mat[n-1-y][x]

        # BL (Move TL to BL)
        mat[n-1-y][x] = top

        y = y + 1


for i in range(n):
    print(mat[i])



