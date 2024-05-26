def incremented_list(listofint):
    listofstring=map(str,listofint)
    list2=list(listofstring)
    makeitint="".join(list2)
    makeitint=int(makeitint)
    sum=makeitint+1
    add=str(sum)
    list1=list(add)
    return list1
listofint=[1,2,3]
incremented_list(listofint)
