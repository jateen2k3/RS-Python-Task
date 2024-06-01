X =   [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
     
result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

for row in result:
    print(row)
for column in result:
    print(column)    