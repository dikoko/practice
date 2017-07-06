# 1-01. Prime Numbers
# Given a number N, find all prime numbers equal or less than N.

# generate prime numbers by Sieve of Eratosthenes
def primes(N):
    if N <= 1: return []
    if N == 2 or N == 3: return [N]
    
    prime_table = [True] * (N+1) # N+1 beacuse we are going to use 1 base (non zero) index
    p = 2
    while p*p <= N:
        if prime_table[p]:
            for q in range(2*p, N+1, p):
                prime_table[q] = False
        p += 1
    
    return [p for p in range(2,N+1) if prime_table[p]]


if __name__ == '__main__':
    N = 100
    print(primes(N))
    