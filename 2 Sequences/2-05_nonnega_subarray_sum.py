# Given an array of 'nonnegative' integers and an integer T,
# find whether there is a ‘continuous sequence’ of the array that sums up to exactly T.
# e.g.)
# [23, 5, 4, 7, 2, 11], 20 => [7, 2, 11]
# [1, 3, 5, 23, 2], 8 => [3, 5]

# Nonnegative Subarray Sum
# using two pointers
# if we want to reduce the sum: should increase the low
# if we want to increase the sum: should increase the high
def subarray_sum(nums, T):
    if not nums: return
    if T < 0: return
    
    len_n = len(nums)
    low = 0
    high = 0
    current_sum = nums[high]
    while low <= high and high < len_n:
        if current_sum == T:
            return nums[low:high+1]
        elif current_sum > T: # we should reduce
            if low == high: # we also increase the high
                high += 1
                current_sum += nums[high]
            current_sum -= nums[low]
            low += 1
        else: # we should increase the sum
            high += 1
            current_sum += nums[high]
    
    return []
    


if __name__ == '__main__':
    nums1 = [23, 5, 4, 7, 2, 11]
    nums2 = [1, 3, 5, 23, 2]
    
    print(subarray_sum(nums1, 20))
    print(subarray_sum(nums2, 8))    