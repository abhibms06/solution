
# Find longest path in matrix(In ascending order)
'''
9 10 11
6 6  8
2 1  1

Longest path is : 6    (Reason: 1->2->6->9->10->11)
'''

def getPath(i, j, m, n, arr, mat):

    if(i<0 or j<0 or i>=m or j>=n):
        return 0
    if ( mat[i][j] != None ):
        return mat[i][j]

    if ( (j < n-1) and arr[i][j] < arr[i][j+1] ):
        mat[i][j] = 1 + getPath(i,j+1,m,n,arr,mat)
        return mat[i][j]
    if(j > 0 and arr[i][j] > arr[i][j-1]):
        return 1 + getPath(i,j-1,m,n,arr,mat)
        #return mat[i][j]
    if (i > 0 and arr[i][j] > arr[i-1][j]):
        return 1 + getPath(i-1, j, m, n, arr, mat)
        #return mat[i][j]
    if ( i < n-1 and arr[i][j] > arr[i+1][j] ):
        return 1 + getPath(i+1, j, m, n, arr, mat)
        #return mat[i][j]

    #mat[i][j] = 1
    return mat[i][j]

'''
print('Enter matrix dimension (m x n) : ')
m,n = [int(tmp) for tmp in input().split() ]
'''
m = 2
n = 3

arr = [[9,10,9], [6,5,3]]


'''
for i in range(m):
    arr.insert(i,[])
    for j in range(n):
        arr[i].append(int(input().strip()))

'''


mat = []
for i in range(m):
    mat.insert(i,[None] * n)

print(mat)
result = 0
for i in range(m):
    for j in range(n):
        if ( mat[i][j] == None ):
            mat[i][j] = getPath(i,j,m,n,arr,mat)

        result = max(result,mat[i][j])

print("Result is : ", result)

for i in range(m):
    for j in range(n):
        print(arr[i][j], end='\t')
    print()

print(mat)
