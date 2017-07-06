# Reverse bits of a 32 bit unsigned integer.
# e.g. x = 3,
# 00000000000000000000000000000011
# → 11000000000000000000000000000000 (3221225472)

def get_kbit(N, k):
    return 1 if N & (1 << k) else 0

def set_kbit(N, k, val):
    if val == 0: # clear
        return N & ~(1 << k)
    else:
        return N | (1 << k)

def reverse_bits(N):
    low = 0
    high = 31
    
    while low < high:
        a = get_kbit(N, low)
        b = get_kbit(N, high)
    
        N = set_kbit(N, low, b)
        N = set_kbit(N, high, a)
        
        low += 1
        high -= 1
    
    return N

if __name__ == '__main__':
    N1 = 3 # 3221225472    
    print(reverse_bits(N1))
