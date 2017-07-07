# Given Number N find if its COLORFUL number or not.
# COLORFUL number: A number can be broken into different contiguous sub-subsequence parts.
# Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245 3245.
# And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different

from collections import defaultdict

def colorful(N):
    
    nstr = str(N)
    len_n = len(nstr)
        
    def calc_product(instr):
        nlist = list(instr)
        nlist = list(map(int, nlist))
        prod = 1
        for n in nlist:
            prod *= n
        return prod
    
    seqs = []
    for k in range(1, len_n+1):  
        for i in range(len_n - k + 1):
            seqs.append(nstr[i:i+k])
    
    seqs = list(map(calc_product, seqs))
    
    count = defaultdict(int)
    for item in seqs:
        count[item] += 1
    
    for cnt in count.values():
        if cnt > 1:
            return False
    
    return True

if __name__ == '__main__':
    N1 = 23
    N2 = 3245
    N3 = 1231
    
    print(colorful(N1))