# Given an array and a value, remove all the instances of that value in the array.
# Also return the number of elements left in the array after the operation.
# It does not matter what is left beyond the expected length.
# e.g:
# [4, 1, 1, 2, 1, 3] and value is 1, -> [4, 2, 3]
# Try to do it in less than linear additional space complexity.

def remove_element(nums, elem):
    if not nums: return
    
    len_nums = len(nums)
    j = 0
    for i in range(len_nums):
        if nums[i] != elem:
            nums[j] = nums[i]
            j += 1
    nums = nums[:j]
    
    return j, nums

# [4, 1, 1, 2, 1, 3]
# [4, 2,
# ele = 1
# j = 1
# 4
# --
# i = 3
   

if __name__ == '__main__':
    nums = [4, 1, 1, 2, 1, 3]
    print(remove_element(nums, 1))
    