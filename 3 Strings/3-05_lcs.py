# A subsequence of a string S, is a set of characters that appear in the string in left-to-right order,
# but not necessarily consecutively.
# A string of length n can have 2^n subsequences (including the null sequence and the entire array.)
# Given two strings, write a function that returns the total number of characters
# in their Longest Common Subsequences (LCS). And print the LCS
# e.g
# ex1)
# s1 = ABCD
# s2 = AEBD
# LCS = ABD / 3
# ex2)
# s1 = AAACCGTGAGTTATTCGTTCTAGAA
# s2 = CACCCCTAAGGTACCTTTGGTTC
# LCS = ACCTAGTATTGTTC / 14

def lcs(s1, s2):
    if not s1 or not s2: return
    
    len1 = len(s1)
    len2 = len(s2)
    
    T = [[0]*(len2+1) for _ in range(len1+1)]
    
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if s1[i-1] == s2[j-1]:
                T[i][j] = T[i-1][j-1] + 1
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])
    
    i = len1
    j = len2
    out_list = []
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            out_list.append(s1[i-1])
            i -= 1
            j -= 1
        else:
            if T[i-1][j] > T[i][j-1]:
                i -= 1
            else:
                j -= 1
    
    return T[len1][len2], "".join(reversed(out_list))


if __name__ == '__main__':
    s1 = 'ABCD'
    s2 = 'AEBD' # LCS = ABD / 3

    s3 = 'AAACCGTGAGTTATTCGTTCTAGAA'
    s4 = 'CACCCCTAAGGTACCTTTGGTTC' # LCS = ACCTAGTATTGTTC / 14
    
    print(lcs(s1,s2))
    print(lcs(s3,s4))
