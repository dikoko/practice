# The gray code is a binary numeral system where two successive values differ in only one bit.
# Given a non-negative integer n representing the total number of bits in the code,
# print the sequence of gray code. A gray code sequence must begin with 0.
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2

def gray_code(N):
    if N < 1: return []
    
    def _gen_gray(n):
        if n == 1:
            return [0, 1]
        
        # n > 2
        first_half = _gen_gray(n-1)
        second_half = [1 << (n-1) | num for num in reversed(first_half)]
        
        return first_half + second_half
    
    return _gen_gray(N)

if __name__ == '__main__':
    N = 5
    print(gray_code(N))
