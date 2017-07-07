# Given an unsorted array, sort it in such a way that the first element is the largest value,
# the second element is the smallest, the third element is the second largest element and so on.
# [2, 4, 3, 5, 1] -> [5, 1, 4, 2, 3]
# Can you do it without using extra space?

def alternative_sort(nums):
    if not nums: return
    len_nums = len(nums)
    
    nums.sort()
    for i in range(0, len_nums-1, 2):
        temp_max = nums[len_nums-1]
        nums[i+1:] = nums[i:len_nums-1]
        nums[i] = temp_max
    
    return nums
    
def alternative_sort_wa(nums): # with additional memories
    if not nums: return
    len_nums = len(nums)
    
    nums.sort()
    min_i = 0
    max_i = len_nums-1
    
    out_list = [0]*len_nums
    toggle = False
    for i in range(len_nums):
        if not toggle:
            out_list[i] = nums[max_i]
            max_i -= 1
        else:
            out_list[i] = nums[min_i]
            min_i += 1
        toggle = not toggle
    
    return out_list
        

if __name__ == '__main__':
    nums1 = [2, 4, 3, 5, 1]
    nums2 = [2, 4, 3, 5, 1, 9, 7, 6]
    
    print(alternative_sort(nums1))
    print(alternative_sort(nums2))
    print(alternative_sort_wa(nums1))
    print(alternative_sort_wa(nums2))    