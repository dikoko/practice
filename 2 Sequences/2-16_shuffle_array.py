# Given an array of 2n integers in the following format a1 a2 a3 … an b1 b2 b3... bn.
# Shuffle the array to a1 b1 a2 b2 a3 b3 … an bn without any extra memory.
# a1 a2 a3 b1 b2 b3     4 -> 1, 6 ->2  8 -> 3  (N-2)//2 / i = 0,1,2,3..
# a1 a2 (b1 a3) b2 b3    start from len//2, len//2+1  j = 0
# a1 (b1 a2)(b2 a3) b3   

def shuffle_array(nums):
    
    len_n = len(nums)
    for i in range((len_n-2)//2):
        for j in range(i+1):
            left = (len_n-1)//2 -i + 2*j
            nums[left], nums[left+1] = nums[left+1], nums[left]
    
    return nums

#  0  1  2  3  4  5  6  7
# [1, 2, 3, 4, 5, 6, 7, 8]
# i = 0, 1, 2
# --
# i = 0
# j = 0
# left = 3-0+0 = 3

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    print(shuffle_array(nums))