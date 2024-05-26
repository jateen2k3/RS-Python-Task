import array as arr
le=int(input("enter the length of no:"))
pr1=[]

num=arr.array('i',[])
for i in range(0,le):
    element=int(input("enter the no:"))
    num.append(element)
print(num)

pr=list(num)
pr.sort()
for i in range(0,len(pr)):
    a=0
    for j in range(2,pr[i]):

        if pr[i]%j==0:
            a=1
            break
    if a==0:
            pr1.append(pr[i])
    
    
print(pr1) 
if pr1[0]==2:
    diff=pr1[-1]-pr1[1]
elif pr1[0]!=2:
    diff=pr1[-1]-pr[0]
print(diff)    
