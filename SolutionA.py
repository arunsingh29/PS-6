from copy import deepcopy

size = int(input())

matrix = []

for _ in range(size):
    matrix.append(input().rstrip().split())

mat = deepcopy(matrix)

for i in range(size):
    temp = 0
    for j in reversed(range(size)):
        if mat[j][i] == "D":
            temp += 1
            mat[j][i] = 1
        elif(temp != 0):
            mat[j+temp][i] = 0
            mat[j][i] = 1
        else:
            mat[j][i] = 0

S = deepcopy(mat)

for i in range(1, size):
    for j in range(1, size):
        if S[i][j] == 1:
            S[i][j] = min(S[i-1][j], S[i][j-1], S[i-1][j-1])+1
maxi1 = 0

for z in range(size):
    temp = max(S[z])
    if temp > maxi1:
        maxi1 = temp


mat = deepcopy(matrix)

for i in range(size):
    temp = 0
    for j in range(size):
        if mat[i][j] == "D":
            temp += 1
            mat[i][j] = 1
        elif(temp != 0):
            mat[i][j-temp] = 0
            mat[i][j] = 1
        else:
            mat[i][j] = 0
S = deepcopy(mat)

for i in range(1, size):
    for j in range(1, size):
        if S[i][j] == 1:
            S[i][j] = min(S[i-1][j], S[i][j-1], S[i-1][j-1])+1

maxi2 = 0

for z in range(size):
    temp = max(S[z])
    if temp > maxi2:
        maxi2 = temp

print(max(maxi1, maxi2))
