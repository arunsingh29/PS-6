def matrixRotation(m, n, matrix, r):
    mt = []
    k = min(m, n) // 2 
    
    for z in range(k):
        temp = []
        for i in range(z,n-z):
            temp.append(matrix[z][i])
        for i in range(z+1, m-1-z):
            temp.append(matrix[i][n-z-1])
        for i in reversed(range(z,n-z)):
            temp.append(matrix[m-z-1][i])
        for i in reversed(range(z+1, m-z-1)):
            temp.append(matrix[i][z]) 
        mt.append(temp)
        

    for z in range(k):
        row  = mt[z]
        
        idx = (r[z] % len(row))*((-1)**z)

        def inc(idx):
            idx = (idx + 1) % len(row)
            return idx

        for i in range(z,n-z):
            matrix[z][i] = row[idx]
            idx = inc(idx)
        for i in range(z+1, m-1-z):
            matrix[i][n-z-1] = row[idx]
            idx = inc(idx)
        for i in reversed(range(z,n-z)):
            matrix[m-z-1][i] = row[idx]
            idx = inc(idx)
        for i in reversed(range(z+1, m-z-1)):
            matrix[i][z] = row[idx]
            idx = inc(idx)

    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end = " ")
        print()

m,n = [int(x) for x in input().split()]
matrix = []
for W in range(m):
    matrix.append([int(x) for x in input().split()])

k = min(m,n)//2

r = [int(x) for x in input().rstrip().split()]


matrixRotation(m,n,matrix,r)
    
