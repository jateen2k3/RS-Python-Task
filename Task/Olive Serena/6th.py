n=int(input("Enter the number of elements : "))
A=[]
min=0
max=0
for i in range(n):
  c=int(input("Enter the element : "))
  A.append(c)

X=sorted(A)
for i in range(n):
  if isprime(X[i]):
   min=X[i]
   break
for i in range(n-1,0,-1):

  if isprime(X[i]):
    max=X[i]
if max==min and max!=0 and min!=0:
  print("Difference = ",(max-min))
else:
  print("Difference = ",min)
if max==min and max==0:
  print(1)
