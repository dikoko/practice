# 1-05. Total Number of Digits
# Given an integer N, count all non-negative integers equal or less than N in which digit 3 is appearing.
# e.g. N = 30 -> 4 (3, 13, 23, 30)

# a brute-force solution
def total_num_digit_bf(N):
    if N <= 0: return 
    
    count = 0
    for i in range(3, N+1):
        if '3' in str(i):
            count += 1
    
    return count

# better solution based on the geeksforgeeks
def total_num_digit(N):
    
    # number of integers with digit 3 of d-length digit 
    def _D(d):
        if d < 0: return 0
        if d == 1: # 0~9
            return 1
        return 9*_D(d-1) + 10**(d-1)
        
    def _totalnum(n):
        if n < 3: return 0
        if n >=3 and n < 10: return 1
        
        # find the length of digits of n
        d = len(str(n))
        # find the MSD (most significant digit)
        MSD = int(str(n)[0])
        
        if MSD < 3: # 0,1,2
            return MSD*_D(d-1) + _totalnum(n % 10**(d-1))
        elif MSD == 3: 
            return MSD*_D(d-1) + 1 + (n % 10**(d-1))
        else: # MSD > 3
            return (MSD-1)*_D(d-1) + 10**(d-1) + _totalnum(n % 10**(d-1))
    
    return _totalnum(N)
            

if __name__ == '__main__':
    N = 428
    print(total_num_digit_bf(N))
    print(total_num_digit(N))