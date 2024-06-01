string=input("enter a string: ")
string=string.replace(" ","")
new=""
for i in string:
    if i not in new:
        new=new+i
b=sorted(new)
for i in b:
    print(i,"->",string.count(i))
