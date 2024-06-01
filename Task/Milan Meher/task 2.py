"""program to display the frequency of each character of the string(uppercase 
letter and lowercase letter both) enter by user in lexicographical order."""

str = input("enter the string : ")
s = sorted(str)
freq = {ele : s.count(ele) for ele in s}
print(freq)