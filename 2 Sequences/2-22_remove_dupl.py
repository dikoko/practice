# Remove duplicates from Sorted Array. Given a sorted array,
# remove the duplicates in place such that each element appears only once and return the new length.
# Note that even though we want you to return the new length, make sure to change the original array as well in place.
# Do not allocate extra space for another array, you must do this in place with constant memory.
# e.g:
# [1,1,2] -> 2, [1,2]

def remove_duplicates(nums):
    
    len_nums = len(nums)
    
    prev = nums[0]
    j = 1
    for i in range(1, len_nums):
        if prev != nums[i]:
            nums[j] = nums[i]
            prev = nums[i]
            j += 1
            
    return j, nums[:j]
            

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 2, 2]
    
    print(remove_duplicates(nums))