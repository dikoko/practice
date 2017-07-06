# Given an array of n numbers, give an algorithm for finding a contiguous subsequence A(i)...A(j)
# for which the sum of elements is maximum.
# e.g. [-2, 11, -4, 13, -5, 2] -> 20 [11, -4, 13]
# [1, -3, 4, -2, -1, 6] -> 7 [4, -2, -1, 6]

import math

# Kadane's algorithm
def maxsum_subarray(nums):
    len_n = len(nums)
    
    current_sum = nums[0]
    max_sum = -math.inf
    max_high = 0
    max_low = 0
    current_low = 0
    
    for i in range(1, len_n):
        if current_sum + nums[i] > nums[i]: # extends it
            current_sum += nums[i]
        else: # drop the previous 
            current_sum = nums[i]
            current_low = i
        
        if current_sum > max_sum:
            max_sum = current_sum
            max_high = i
            max_low = current_low
    
    return max_sum, nums[max_low:max_high+1]


if __name__ == '__main__':
    nums1 = [-2, 11, -4, 13, -5, 2] # 20
    nums2 = [1, -3, 4, -2, -1, 6] # 7
    nums3 = [-1, -2, -4, -8, -5] # This algorithm does not work when all nums are negative
    
    print(maxsum_subarray(nums1))
    print(maxsum_subarray(nums2))    
    print(maxsum_subarray(nums3))        