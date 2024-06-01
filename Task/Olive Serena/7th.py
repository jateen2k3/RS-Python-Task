N=int(input("Enter the number of item: "))

for i in range(1,N+1):
  A=[]
  R = int(input(f"Enter the MRP of item {i}: "))
  f=fact(R)
  p=R-f
  print("Amount Roy pays = Rs.",p)
  print("Amount Alfie pays = Rs.",f)

def fact(N):
  for i in range(2,N+1) :
    if(N%i==0):
      if isprime(i):
        return i
  return N

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
