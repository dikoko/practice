# Given a sorted array, remove the duplicates in place such that each element can appear at most twice
# and return the new length.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# Note that even though we want you to return the new length, make sure to change the original array as well in place.
# e.g.
# [1,1,1,2] -> 3, [1,1,2]

def remove_duplicates2(nums):
    
    len_nums = len(nums)
    count = 1
    prev = nums[0]
    j = 1
    for i in range(1, len_nums):
        if prev == nums[i]:
            count += 1
        else:
            prev = nums[i]
            count = 1
            
        if count <= 2:
            nums[j] = nums[i]
            j += 1
    
    return j, nums[:j]
    


if __name__ == '__main__':
    nums1 = [1, 1, 1, 1, 2, 2, 2, 3, 3]
    nums2 = [1, 1, 1, 2]
    print(remove_duplicates2(nums1))
    print(remove_duplicates2(nums2))    
    