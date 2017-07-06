# Give a function that takes an unsigned integer and returns the number of 1 bits.
# e.g. 11 (0b1011) -> 3

def num_of_1bits(N):
    if N <= 0: return 0
    count = 0
    for _ in range(32):
        if N & 1: 
            count += 1
        N >>= 1
    return count
        

if __name__ == '__main__':
    N = 11
    print(num_of_1bits(N))
