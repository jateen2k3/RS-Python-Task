
s= 'RoboticsSociety'
x=list(s)
# print(x)
y=sorted(x)
# print(y)

frequency={}
 
for item in y:
    if item in frequency:
        frequency[item]+=1
    else:
        frequency[item]=1
print(frequency)
