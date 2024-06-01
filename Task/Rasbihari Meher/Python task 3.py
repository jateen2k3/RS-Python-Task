list=[]
a=int(input("enter no of element to be entered: "))
for i in range(0,a):
    n=int(input("enter element of a list: "))
    list.append(n)
print(list)
list[-1]+=1
print(list)
