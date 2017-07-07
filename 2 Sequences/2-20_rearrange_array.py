# Gives an array of unsorted int (may have negative number),
# rearrange the array such that the num at the 
# odd index is greater than the num at the even index.

import math

def find_kth(nums, k):
    if not nums: return
    
    def _findk(subnums, k):
        if not subnums: return
        if k <0 or k >= len(subnums): return 
        
        pivot = subnums[0]
        left = []
        right = []
        for i in range(1, len(subnums)):
            if pivot > subnums[i]:
                left.append(subnums[i])
            else:
                right.append(subnums[i])
        if len(left) == k:
            return pivot
        elif len(left) > k:
            return _findk(left, k)
        else:
            return _findk(right, k - len(left)-1)
    return _findk(nums, k)
    
def rearrange(nums):
    if not nums: return
    
    len_nums = len(nums)
    mid = len_nums//2
    
    mid_val = find_kth(nums, mid)
    
    evens = []
    odds = []
    for i in range(len_nums):
        if nums[i] > mid_val:
            odds.append(nums[i])
        if nums[i] < mid_val:
            evens.append(nums[i])
            
    if len_nums % 2 == 1:
        evens.append(mid_val)
    else:
        odds.append(mid_val)
        
    for i in range(len(evens)):
        nums[2*i] = evens[i]
    for i in range(len(odds)):
        nums[2*i+1] = odds[i]
        
    return nums
        

if __name__ == '__main__':
    nums1 = [5, 2, 3, 4, 1]
    nums2 = [1, 3, 6, -1, 5, 4, -3, 2, 8]
    
    print(rearrange(nums1))
    print(rearrange(nums2))