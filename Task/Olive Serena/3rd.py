a=input("Enter a number : ")
l= len(a)
digits=[]
digits2=[]
for i in a :
  digits.append(int(i))
print(f"Original Digits = {digits}")
b=int(a)
b=b+1
b=str(b)
for i in b :
  digits2.append(int(i))
print(f"Original Digits = {digits2}")
