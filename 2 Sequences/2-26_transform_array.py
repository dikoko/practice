# Given an array of elements, convert it into an array such that A < B > C < D >E < F
# e.g. [1, 3, 2, 5, 4, 6]

def transform_array(nums):
    if not nums: return
    
    nums.sort()
    len_nums = len(nums)
    for i in range(1, len_nums-1, 2):
        nums[i], nums[i+1] = nums[i+1], nums[i]
    
    return nums


if __name__ == '__main__':
    nums = [1, 3, 2, 5, 4, 6]
    
    print(transform_array(nums))