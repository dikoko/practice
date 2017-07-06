# 1-02. Prime Factors
#
# Given a number N, return the prime factor multiplication.
# e.g. 90 = 2*3*3*5 -> [2, 3, 3, 5]

def prime_factors(N):
    if N <= 1:
        return []
    if N == 2 or N == 3:
        return [N]
    
    out_list = []
    
    while N % 2 == 0: # if it is even number
        out_list.append(2)
        N //= 2
    
    # now N is odd number
    for p in range(3, N, 2):
        while N % p == 0 and N != 1:
            out_list.append(p)
            N //= p
        if N == 1:
            return out_list
    
    if N != 1: # if the remaining N is the prime number itself
        out_list.append(N)
    
    return out_list
    
            
if __name__ == '__main__':
    N1 = 90
    N2 = 432
    N3 = 73
    
    print(prime_factors(N1))
    print(prime_factors(N2))
    print(prime_factors(N3))
    
    