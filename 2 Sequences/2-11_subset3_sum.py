# Given an array of n elements.
# Find three elements in the array such that their sum is equal to given element T?
# [3, 2, 7, 1, 4] / 10 → [2,7,1]
# [1, 2, 3, 4] / 10 -> False

# a brute force solution will be O(n^3)
# but there is a O(n^2) solution by using 2-9 solution
def subset3_sum(nums, T):
    if not nums: return
    len_n = len(nums)
    
    nums.sort()
    
    def _subset2sum(low, high, t):
        out_list = []
        while low < high:
            temp_sum = nums[low] + nums[high]
            if temp_sum == t:
                out_list.append([nums[low], nums[high]])
                low += 1
                high -= 1
            elif temp_sum > t:
                high -= 1
            else:
                low += 1
        return out_list
    
    results = []
    for i in range(len_n - 2):
        sub_results = _subset2sum(i+1, len_n-1, T-nums[i])
        for item in sub_results:
            item.append(nums[i])
        results += sub_results
    
    return results
        
                

if __name__ == '__main__':
    nums1 = [3, 2, 7, 1, 4]
    nums2 = [1, 2, 3, 4]
    
    print(subset3_sum(nums1, 10))
    print(subset3_sum(nums2, 10))
    