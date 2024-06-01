def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def difference(A):
    primes = [num for num in A if is_prime(num)]
    
    if not primes:
        return "No prime numbers present"
    
    return max(primes) - min(primes)

A = [1, 2, 3, 4, 5]
print(difference(A))





