s = input("Enter a string(s) : ")
t = input("Enter a string(t) : ")
l1 = len(s)
l2 = len(t)
flag = 0
print("Length of s ",l1)
print("Length of t ",l2)
if(l1==l2):
  for i in range(97,123):
    c1=0
    c2=0
    for j in s:
      if j==chr(i):
        c1=c1+1
    for k in t:
      if k==chr(i):
        c2=c2+1
    if c1!=c2:
      flag=1
      break
  if flag==0:
    print("Anagram")
  else:
    print("Not Anagram")
else:
  print("Not Anagram")
