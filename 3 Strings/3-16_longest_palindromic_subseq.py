# Given a string, find longest palindromic subsequence in this string.
# instr = 'agbdba' → 'abdba'

def longest_palin_subseq(instr):
    len_s = len(instr)
    
    T = [[0]*len_s for _ in range(len_s)]
    
    for i in range(len_s):
        T[i][i] = 1
    
    for l in range(1,len_s+1):
        for i in range(len_s-l+1):
            for j in range(i+1, i+l):
                if instr[i] == instr[j]:
                    T[i][j] = T[i+1][j-1] + 2
                else:
                    T[i][j] = max(T[i+1][j], T[i][j-1])

    for i in range(len_s):
        print(T[i])
    print("")
    
    return T[0][len_s-1]

if __name__ == '__main__':
    instr = 'agbdba'
    print(longest_palin_subseq(instr))