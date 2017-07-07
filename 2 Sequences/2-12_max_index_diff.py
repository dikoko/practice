# Given an array A[ ], find the maximum j - i such that A[j] > A[i].
# e.g. [34, 8, 10, 3, 2, 80, 30, 33, 1] -> 6 (j = 7, i = 1)

# left_mins [34, 8, 8, 3, 2, 2, 2, 2, 1]
# right_maxs [80, 80, 80, 80, 80, 80, 33, 33, 1]

def max_index_diff(nums):
    if not nums: return
    len_n = len(nums)
    low = 0
    high = 0
    max_diff = -1
    max_low = 0
    max_high = 0
    
    left_mins = [nums[0]]*len_n
    right_maxs = [nums[len_n-1]]*len_n
    
    for i in range(1, len_n):
        left_mins[i] = min(left_mins[i-1], nums[i])
    for i in reversed(range(len_n-1)):
        right_maxs[i] = max(right_maxs[i+1], nums[i])
        
    while low < len_n and high < len_n:
        while high < len_n and left_mins[low] < right_maxs[high]:
            high += 1
        index_diff = (high-1) - low
        if index_diff > max_diff:
            max_diff = index_diff
            max_low = low
            max_high = high - 1
        low += 1
    
    return max_diff, max_low, max_high
    
if __name__ == '__main__':
    nums = [34, 8, 10, 3, 2, 80, 30, 33, 1]
    print(max_index_diff(nums))