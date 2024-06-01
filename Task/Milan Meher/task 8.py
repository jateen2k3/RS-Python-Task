# program to count the freq... of elements of input list in dictionary order.

list = [2,"mango",8.3,6,6,43,"gun",7,"mango",2,4.8,4,2]    # list as input
freq = {ele : list.count(ele) for ele in list }
print(freq)