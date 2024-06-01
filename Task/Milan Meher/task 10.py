#program to do transpose of a matrix.

M = [[1,2,3],[4,5,6],[7,8,9]]     # matrix M
T = [[0,0,0],[0,0,0],[0,0,0]]     # transpose matrix T

for i in range (len(M)):
    for j in range (len(M[0])):
        T[j][i] = M[i][j]
print(T)