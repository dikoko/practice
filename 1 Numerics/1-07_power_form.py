# Given a positive integer which fits in a 32bit signed integer,
# Find if it can be expressed as A^P where P > 1 and A > 0. (A and P are both integers)
# e.g. 2562890625 → True, 15^8

import math

def power_form(N):
    if N == 1: return True # A == 1 case
    if N < 1: return False
    
    if N & (N-1) == 0: # 2^x form
        return True
    # N < 2^31, because it fits 32bit 'signed' form
    # A^2 < 2^31 when A is max, P should be 2
    # so, A < 2^(31/2) < 2^16    
    for a in range(3, 2**16):
        for p in range(2, int(math.log(N,a))+1): # A^P <= N
            if a**p > N:
                break
            if a**p == N:
                return True, a, p
    return False, 0, 0
            

if __name__ == '__main__':
    N = 2562890625
    print(power_form(N))