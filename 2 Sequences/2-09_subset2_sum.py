# Given an array of n elements. Find two elements in the array such that their sum is equal to given T
# [3, 2, 7, 1, 4], 7

# There is a O(nlogn) solution: O(nlogn)+O(n) - sort and n
def subset2_sum(nums, T):
    if not nums: return
    len_n = len(nums)
    nums.sort()
    
    low = 0
    high = len_n -1
    out_list = []
    while low < high:
        temp_sum = nums[low] + nums[high]
        if temp_sum == T:
            out_list.append([nums[low], nums[high]])
            low += 1
            high -= 1
        elif temp_sum > T:
            high -= 1
        else:
            low += 1
    
    return out_list
    

if __name__ == '__main__':
    nums = [3, 2, 7, 1, 4]
    print(subset2_sum(nums, 7))
    