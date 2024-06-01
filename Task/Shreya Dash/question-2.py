s=input("Enter the string:")
d=sorted(s)
l=len(d)
print(l)
for i in range(0,l):
    print(d[i],"-",s.count(d[i]))