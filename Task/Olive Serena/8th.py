s= input("Enter a string : ")
l= len(s)
dict={}
for i in range(0,127):
  c=0
  for j in s:
    if j == chr(i):
     c=c+1
  if(c!=0):
   dict.update({chr(i): c})
print(dict)
