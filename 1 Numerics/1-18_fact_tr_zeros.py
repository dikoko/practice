# Given an integer n, return the number of trailing zeroes in n!.
# Note: Your solution should be in logarithmic time complexity.
# e.g. :
# n = 5
# n! = 120
# Number of trailing zeros = 1

def factorial_trailing_zeros(N):
    # N = /25 24 23 22 21 /20 19 18 17 16 /15 14 13 12 11 /10 9 8 7 6 /5 4 3 2 1
    # number of 5 factors (because 2s are always more than 5s)
    count = 0
    while N > 0:
        N //= 5
        count += N
        
    return count
        

if __name__ == '__main__':
    N1 = 5
    N2 = 32
    print(factorial_trailing_zeros(N1))
    print(factorial_trailing_zeros(N2))
