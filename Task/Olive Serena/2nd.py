s= input("Enter a string : ")
l= len(s)
for i in range(65,91):
  c=0
  for j in s:
    if j == chr(i):
     c=c+1
  if(c!=0):
   print(chr(i)," - ",c)

for k in range(97,123):
  c=0
  for l in s:
    if l ==chr(k) :
      c=c+1
  if(c!=0):
   print(chr(k)," - ",c)

