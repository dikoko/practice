# Given an array of positive integers, all numbers occur an even number of times
# except one number which occurs an odd number of times. Find the number O(n) time & constant space.
# e.g. [1, 2, 3, 2, 3, 1, 3] -> 3

def find_odd_occurs(nums):
    if not nums: return
    len_n = len(nums)
    n = nums[0]
    for i in range(1,len_n):
        n ^= nums[i]
    
    return n 


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 3, 1, 3]
    print(find_odd_occurs(nums))