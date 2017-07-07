# Each cell value means the number of steps you can jump. Find the minimum number of steps to reach end.
# e.g. nums = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1] → 4 steps : 0, 1, 4, 5, 9

from collections import defaultdict
import math

def min_jumps(nums):
    
    _prevs = defaultdict(lambda: None)
    len_nums = len(nums)
    
    _minjumps = [math.inf]*len_nums
    _minjumps[0] = 0
    
    for i in range(1, len_nums):
        for j in range(i):
            if i - j <= nums[j]: # we can jump j to i
                if _minjumps[i] > _minjumps[j]+1:
                    _minjumps[i] = _minjumps[j]+1
                    _prevs[i] = j
    path = []
    node = len_nums-1
    while node is not None:
        path.append(node)
        node = _prevs[node]
    
    return _minjumps[len_nums-1], list(reversed(path))
    

if __name__ == '__main__':
    nums = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
    print(min_jumps(nums))