
print('Enter row: ',sep='')
row = int(input().strip())

print('Enter col: ',sep='')
col = int(input().strip())

mat = []
for i in range(row):
    mat.append([int(tmp) for tmp in input().strip().split()])

print(mat)

tra_mat = []

for i in range(col):
    tmp = []
    for j in range(row):
        tmp.append(mat[j][i])

    tra_mat.append(tmp)


print('Transpose of matrix:',tra_mat)



