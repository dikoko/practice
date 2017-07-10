# String C is said to be interleaving of string A and B
# if it contains all the characters of A and B
# and the relative order of characters of both the string is preserved in C.
# Given three string A, B and C, write a function to check
# if third string is the interleaving of first and second string.
# e.g.
# A = xyz B = abcd C = xabyczd → True
# A = bcc B = bbca C = bbcbcac → True
# A = bcc B = bbca C = bbbbcac → False

def is_interleaved(A, B, C):
    if not A or not B or not C: return
    len_a = len(A)
    len_b = len(B)
    len_c = len(C)
    
    if len_a + len_b != len_c:
        return False
    
    T = [[False]*(len_b+1) for _ in range(len_a+1)]
    T[0][0] = True
    for i in range(1, len_a+1):
        T[i][0] = T[i-1][0] if A[i-1] == C[i-1] else False
    for j in range(1, len_b+1):
        T[0][j] = T[0][j-1] if B[j-1] == C[j-1] else False
        
    for i in range(1, len_a+1):
        for j in range(1, len_b+1):
            if A[i-1] == C[i+j-1] and B[j-1] != C[i+j-1]:
                T[i][j] = T[i-1][j]
            elif A[i-1] != C[i+j-1] and B[j-1] == C[i+j-1]:
                T[i][j] = T[i][j-1]
            elif A[i-1] == C[i+j-1] and B[j-1] == C[i+j-1]:
                T[i][j] = T[i-1][j] or T[i][j-1]
            else:
                False
    
    return T[len_a][len_b]



if __name__ == '__main__':
    a1 = 'xyz'
    b1 = 'abcd'
    c1 = 'xabyczd' # TRUE
    
    a2 = 'bcc'
    b2 = 'bbca'
    c2 = 'bbcbcac' # TRUE
    
    a3 = 'bcc'
    b3 = 'bbca'
    c3 = 'bbbbcac' # FALSE

    print(is_interleaved(a1, b1, c1))
    print(is_interleaved(a2, b2, c2))
    print(is_interleaved(a3, b3, c3))        