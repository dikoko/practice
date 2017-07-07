# Given an array of integers greater than zero,
# find if it is possible to split it in two (without reordering the elements),
# such that the sum of the two resulting arrays is the same. Print the resulting arrays.
# [1,2,3,4,5,6,21], → [1,2,3,4,5,6][21]
# [1,90, 50, 30, 5, 3, 2, 1 ], → [1,90][50,30,5,3,2,1]
# [1, 50, 900, 1000 ] → none

def samesum_split(nums):
    if not nums: return
    
    len_nums = len(nums)
    
    out_list = []
    
    for k in range(1, len_nums):
        sum1 = sum(nums[:k])
        sum2 = sum(nums[k:])
        if sum1 == sum2:
            out_list.append([nums[:k], nums[k:]])
    
    return out_list

def samesum_split_dp(nums):
    if not nums: return
    
    len_nums = len(nums)
    
    out_list = []

    sum1 = sum(nums[:1])
    sum2 = sum(nums[1:])
    for k in range(1, len_nums):
        if k != 1:
            sum1 = sum1 + nums[k-1]
            sum2 = sum2 - nums[k-1]
        if sum1 == sum2:
            out_list.append([nums[:k], nums[k:]])
    
    return out_list


if __name__ == '__main__':
    nums1 = [1,2,3,4,5,6,21] # → [1,2,3,4,5,6][21]
    nums2 = [1,90, 50, 30, 5, 3, 2, 1 ] # → [1,90][50,30,5,3,2,1]
    nums3 = [1, 50, 900, 1000 ] # → none
    
    print(samesum_split(nums1))
    print(samesum_split(nums2))
    print(samesum_split(nums3))
    print(samesum_split_dp(nums1))
    print(samesum_split_dp(nums2))
    print(samesum_split_dp(nums3))
    