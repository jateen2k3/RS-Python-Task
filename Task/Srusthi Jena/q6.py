from math import sqrt
array =[]
N =input('enter the number of elements')
N = int(N)
N1 =N
N2 =N
while N>0:
    element =input('enter the element')
    array.append(element)
    N = N-1
print(array)
array.sort()
print(array)

K=''
C=''
while N1>0:
    K=array[N1-1]
    K=int(K)
    prime_flag = 0
    for i in range(2, int(sqrt(K)) + 1):
        if (K % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        print(K)
        print('this is the largest prime')
        break
    N1=N1-1
K=int(K)

for el in range(N2):
    C=array[el]
    C=int(C)
    flag =0
    for i1 in range(2, int(sqrt(K)) + 1):
        if (C % i1 == 0):
            flag = 1
            break
    if (prime_flag == 0):
        print(C)
        print('this is the smallest prime')
        break
    N2=N2-1
C=int(C)
print('absolute difference between smallest and largest prime is ')
print(K-C)

