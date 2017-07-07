# Given an array A of sorted integers and another non negative integer k,
# find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
# e.g.
# A : [1 3 5] / k : 4 --> True
# Try doing this in less than linear space complexity.


def diff_k(nums, k):
    len_n = len(nums)
    
    low = 0
    high = 1
    
    while high < len_n:
        temp_diff = nums[high] - nums[low]
        if temp_diff == k:
            return True, low, high
        elif temp_diff > k:
            if high == low +1:
                high += 1
            low += 1
        else:
            high += 1
    
    return False, -1, -1
    

if __name__ == '__main__':
    nums1 = [1, 3, 5] # k = 4
    nums2 = [1, 2, 4, 5, 8, 11, 15] # k = 5
    
    print(diff_k(nums1, 4))
    print(diff_k(nums2, 6))