# Given an array find longest increasing subsequence in this array.
# e.g.
# [3, 4, -1, 0, 6, 2, 3] → [3, 4, -1, 0, 6, 2, 3] size 4
# [2, 5, 1, 8, 3] → [2, 5, 1, 8, 3] size 3

from operator import itemgetter
from collections import defaultdict

# A DP solution
def longest_inc_subsequence(nums):
    if not nums: return
    
    len_nums = len(nums)
    T = [1]*len_nums
    
    _prevs = defaultdict(lambda: None)
    for i in range(1, len_nums):
        for j in range(i):
            if nums[j] < nums[i]:
                if T[j] + 1 > T[i]:
                    T[i] = T[j] + 1
                    _prevs[i] = j
    
    print(T) ###
    
    max_i, max_val = max(enumerate(T), key=itemgetter(1))
    # max_i, max_val = max(enumerate(T), key=lambda x: x[1])
    
    node = max_i
    path = []
    while node is not None:
        path.append(nums[node])
        node = _prevs[node]
    
    return max_val, list(reversed(path))
                
    

if __name__ == '__main__':
    nums = [3, 4, -1, 0, 6, 2, 3]
    print(longest_inc_subsequence(nums))