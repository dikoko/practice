# Given an array A[ ] consisting of 0’s, 1’s and 2’s, give a algorithm for sorting A[ ].
# The algorithm should put all 0’s first, then all 1’s second and finally all 2’s at the end.
# e.g. [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1] -> [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]

def segregate_012(nums):
    if not nums: return
    len_n = len(nums)
    
    def _seg(low, high, x):
        if low == high:
            if nums[low] == x:
                return high+1
            else:
                return low
        while low < high:
            while low <= high and nums[low] == x:
                low += 1
            while low < high and nums[high] != x:
                high -= 1
            if low < high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1
        return low
    
    low = _seg(0, len_n-1, 0)
    low = _seg(low, len_n-1, 1)
    return low, nums

if __name__ == '__main__':
    nums = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    print(segregate_012(nums))