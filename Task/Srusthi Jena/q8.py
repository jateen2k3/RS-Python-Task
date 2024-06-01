mylist= []
length =input('the number of elements u wanna enter')
length = int(length)
l=length
l1 = length
while length>0:
    element =input('enetr the element')
    mylist.append(element)
    length = length-1
print(mylist)
k=''
c=''
my_list=[]
my_list = mylist.copy()

dict={}
while l>0:
    k=mylist[l-1]
    c=my_list.count(k) 
    mylist.remove(k)
    if k in mylist:
        l=l-1
        continue
    print(k,c)
    print('   ')
    dict[k] = c
    l=l-1

print(dict)
     

