# Given an array with both positive and negative numbers,
# find the two elements such that their sum is closest to zero.
# i.e. [1, 60, -10, 70, -80, 85] => -80, 85
import math

def subset2_sum_close0(nums):
    if not nums: return
    len_n = len(nums)

    nums.sort()
    
    low = 0
    high = len_n - 1
    min_abs = math.inf
    out_list = []
    while low < high:
        temp_sum = nums[low] + nums[high]
        if abs(temp_sum) < min_abs:
            min_abs = abs(temp_sum)
            out_list = [[nums[low], nums[high]]]
        elif abs(temp_sum) == min_abs:
            out_list.append([nums[low], nums[high]])
        
        if temp_sum > 0:
            high -= 1
        elif temp_sum < 0:
            low += 1
        else:
            high -= 1
            low += 1
    
    return min_abs, out_list
    

if __name__ == '__main__':
    nums = [1, 60, -10, 70, -80, 85]
    print(subset2_sum_close0(nums))