# Find longest bitonic subsequence in given array. Bitonic subsequence first increases then decreases.
# nums = [2, -1, 4, 3, 5, -1, 3, 2] → longest bitonic subsequence: 2, 3, 5, 3, 2 → 5

from collections import defaultdict
from operator import itemgetter

def longest_bitonic(nums):
    
    len_nums = len(nums)
    
    F = [1]*len_nums
    R = [1]*len_nums
    
    f_prevs = defaultdict(lambda:None)
    r_prevs = defaultdict(lambda:None)
    
    for i in range(1, len_nums):
        for j in range(i):
            if nums[j] < nums[i]:
                if F[i] < F[j]+1:
                    F[i] = F[j]+1
                    f_prevs[i] = j
            
            
    for i in reversed(range(len_nums-1)):
        for j in reversed(range(i+1,len_nums)):
            if nums[i] > nums[j]:
                if R[i] < R[j]+1:
                    R[i] = R[j]+1
                    r_prevs[i] = j
    
    M = [0]*len_nums
    for i in range(len_nums):
        M[i] = F[i]+R[i]-1
    
    print(F)
    print(R)
    print(M)
    
    max_i, max_val = max(enumerate(M), key=itemgetter(1))
        
    node = max_i
    path = []
    while node is not None:
        path.append(nums[node])
        node = f_prevs[node]
    path = list(reversed(path))
    path.pop()

    print(path)
    node = max_i
    while node is not None:
        path.append(nums[node])
        node = r_prevs[node]
    
    return max_i, path


if __name__ == '__main__':
    nums = [2, -1, 4, 3, 5, -1, 3, 2]
    
    print(longest_bitonic(nums))