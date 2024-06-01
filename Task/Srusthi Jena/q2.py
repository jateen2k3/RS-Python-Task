A= "String"
z = len(A)
Ab = list(A) 
b=[0]*26
c=[0]*26

for i in range(0,z, 1):

   D= Ab[i]
   for j in range(65,92,1):
      if (ord(D)==j):

          K=b[j-65]
          K+=1
          b[j-65]=K

      if (ord(D) ==j+32):

         K=c[j-65]
         K+=1
         c[j-65]=K

for o in range(0, 26,1):
   if (b[o]>0):
      D=chr(o+65) 
      print (D, "->", b[o]) 

for p in range(0, 26,1):
   if (c[p]>0):
      D=chr(p+97) 
      print(D, "->", c[p]) 