# Given an array A of integers and another non negative integer k,
# find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
# e.g.
# A : [1 5 3] / k : 2 --> True
    
def diff_k2(nums, k):
    _index = {}
    len_n = len(nums)
    for i in range(len_n):
        _index[nums[i]] = i
    
    nums.sort()
    low = 0
    high = 1
    
    while high < len_n:
        temp_diff = nums[high] - nums[low]
        if temp_diff == k:
            return True, min(_index[nums[high]], _index[nums[low]]), max(_index[nums[high]], _index[nums[low]])
        if temp_diff > k:
            if high == low+1:
                high += 1
            low += 1
        else:
            high += 1
    
    return False, -1, -1


if __name__ == '__main__':
    nums1 = [1, 5, 3] # k = 4
    nums2 = [1, 4, 2, 11, 15, 5, 8] # k = 6
    
    print(diff_k2(nums1, 4))
    print(diff_k2(nums2, 6))

    