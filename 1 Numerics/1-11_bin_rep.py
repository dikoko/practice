import math

# no conseq ones has a property n and 1 shift n is 0
def not_consec_ones(n):
    return n & (n << 1) == 0

# a brute force solution
def bin_count_bf(N):
    count = 0
    for i in range(N+1):
        if not_consec_ones(i):
            count += 1
    return count

# the number of nonconsec integers of d length binary digits
# is a Fibonacci number
# because it can be thought as
# '0' + D[d-1] and '10' + D[d-2]
# e.g. 1 digit -> 0, 1 (2)
#      2 digits -> 00, 01, 10 (3)
#      3 digits -> 0 + 00, 01, 10 -> 000, 001, 010 and 10 + 0,1 -> 100, 101 (3+2=5)
def D(d):
    if d < 1: return 0
    if d == 1: return 2
    if d == 2: return 3
    
    prev_prev = 2
    prev = 3
    count = 0
    for _ in range(3, d+1):
        count = prev_prev + prev
        prev_prev = prev
        prev = count
    
    return count
    

def bin_count(N):
    if N <= 0: return 0
    
    d = int(math.log(N,2))+1 # get the digit length of N
    count = D(d-1) # get the base count
    for i in range(2**(d-1), N+1):
        if not_consec_ones(i):
            count += 1
    
    return count
    

if __name__ == '__main__':
    N1 = 4
    N2 = 323
    print(bin_count_bf(N1))
    print(bin_count(N1))    
    print(bin_count_bf(N2))
    print(bin_count(N2))        