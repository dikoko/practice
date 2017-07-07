# The set [1,2,3,…,n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3 ) :
# (1)"123”, (2)"132", (3)"213", (4)"231", (5)"312", (6)"321"
# Given n and k, return the kth permutation sequence.

import math

def permutation_seq_bf(N, K):
    
    n_list = [n for n in range(1,N+1)]
    len_n = len(n_list)
    
    def _permute(sublist):
        if not sublist:
            return [[]]
        len_s = len(sublist)
        out_list = []
        for i in range(len_s):
            picked = sublist[i]
            picked_results = _permute(sublist[:i]+sublist[i+1:])
            for item in picked_results:
                item.append(picked)
            out_list += picked_results
        
        return out_list
        
    results = _permute(n_list) # [[3,2,1], [ ] ...
    results = [int("".join(map(str,item))) for item in results]
    results.sort()
    
    return results[K-1]

def permutation_seq_better(N, K):
    n_list = [n for n in range(1, N+1)]
    len_n = len(n_list)
    
    out_list = []
    digit = N
    k = K
    while digit > 0:
        cindex = (k-1) // math.factorial(digit-1) + 1
        out_list.append(n_list[cindex-1])
        n_list.remove(n_list[cindex-1])
        k %= math.factorial(digit-1)
        digit -= 1
    
    return int("".join(map(str,out_list)))

if __name__ == '__main__':
    n = 3 
    k = 4
    n2 = 8
    k2 = 62 # 12367485
    print(permutation_seq_bf(n, k))
    print(permutation_seq_bf(n2, k2))
    print(permutation_seq_better(n, k))
    print(permutation_seq_better(n2, k2))
    