# program to check if two strings are anagram or not.

s = input("enter string 1 : ")
t = input("enter string 2 : ")

if (len(t) != len(s)):
    print(t ,"is not an anagram of" ,s)

else:
    if (sorted(t) == sorted(s)):
        print(t ,"is an anagram of" ,s)
    else:
        print(t ,"is not an anararm of" ,s)