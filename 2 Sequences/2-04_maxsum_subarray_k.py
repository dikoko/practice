# For a given array, find the subarray (containing at least k number) which has the largest sum.
# e.g.:
# nums1 = [-4, -2, 1, -3], k = 2 --> -1 [-2, 1]
# nums2 = [1, 1, 1, 1, 1, 1], k = 3 --> 6 [1, 1, 1, 1, 1, 1]
# Try to do it in O(n) time

import math

# The extended version of Kadane's algorithm
def maxsum_subarray_k(nums, K):
    if not nums: return
    len_n = len(nums)
    if K <= 0 or K > len_n: return
    
    max_sum = -math.inf
    max_low = 0
    max_high = K-1
    current_low = 0
    
    current_sum = sum(nums[:K])
    for i in range(K, len_n):
        temp_sum = sum(nums[i-K+1:i+1]) # to tell the truth, it is not O(N) because of here
        if current_sum + nums[i] > temp_sum: # extends it
            current_sum += nums[i]
        else: # drop previous
            current_sum = temp_sum
            current_low = i-K+1
        
        if current_sum > max_sum:
            max_sum = current_sum
            max_low = current_low
            max_high = i
    
    return max_sum, nums[max_low:max_high+1]

# a kind of DP solution to compute the current_sum: it is now O(N)
def maxsum_subarray_k_dp(nums, K):
    if not nums: return
    len_n = len(nums)
    if K <= 0 or K > len_n: return
    
    max_sum = -math.inf
    max_low = 0
    max_high = K-1
    current_low = 0
    
    current_sum = sum(nums[:K])
    for i in range(K, len_n):
        temp_sum = current_sum - nums[i-K] + nums[i] # it is now O(1)
        if current_sum + nums[i] > temp_sum: # extends it
            current_sum += nums[i]
        else: # drop previous
            current_sum = temp_sum
            current_low = i-K+1
        
        if current_sum > max_sum:
            max_sum = current_sum
            max_low = current_low
            max_high = i
    
    return max_sum, nums[max_low:max_high+1]
    
            


if __name__ == '__main__':
    nums1 = [-4, -2, 1, -3]
    nums2 = [1, 1, 1, 1, 1, 1]
    
    print(maxsum_subarray_k(nums1, 2))
    print(maxsum_subarray_k(nums2, 3))
    print(maxsum_subarray_k_dp(nums1, 2))
    print(maxsum_subarray_k_dp(nums2, 3))
