# Given an even number which is greater than 2,
# find 2 prime numbers whose sum will be equal to the even number.
# The solution will always exists according to the Goldbach's conjecture. e.g. 4 → [2, 2]
# If there are more than one solutions, return the lexicographically smaller solution.
# If [a, b] is one solution with a <= b, and [c,d] is another solution with c <= d,
# then [a, b] < [c, d] If a < c OR a==c AND b < d.

def gen_primes(N):
    if N <= 1: return []
    if N == 2 or N == 3: return [N]
    
    p = 2
    prime_table = [True]*(N+1)
    while p*p <= N:
        if prime_table[p]:
            for q in range(2*p, N+1, p):
                prime_table[q] = False
        p += 1
    
    return [i for i in range(2, N+1) if prime_table[i]]


def goldbach_pair(N):
    if N <= 2: return
    if N % 2 != 0: return 
    
    prime_table = gen_primes(N)
    for p in prime_table:
        q = N - p
        if q in prime_table:
            return p, q
            
    return -1, -1
    

if __name__ == '__main__':
    num1 = 1534894
    num2 = 16777214 # it will take about 4 sec...
    print(goldbach_pair(num1))
    print(goldbach_pair(num2))
