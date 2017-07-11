def find_rsa(nums, X):
    
    len_n = len(nums)
    
    def _find(low, high):
        if low > high:
            return -1
            
        mid = low + (high-low)//2
        
        if nums[mid] == X:
            return mid
        
        if nums[low] <= nums[mid]: # left is sorted
            if nums[low] <= X and X < nums[mid]:
                return _find(low, mid-1)
            else:
                return _find(mid+1, high)
        else: # right is sorted
            if nums[mid] < X and X <= nums[high]:
                return _find(mid+1, high)
            else:
                return _find(low, mid-1)

    return _find(0, len_n-1)
    


if __name__ == '__main__':
    nums1 = [5, 6, 7, 8, 9, 10, 1, 2, 3] # 3 → 8
    nums2 = [5, 6, 7, 8, 9, 10, 1, 2, 3] # 30 → -1
    nums3 = [30, 40, 50, 10, 20] # 10 → 3
    
    print(find_rsa(nums1, 3))
    print(find_rsa(nums2, 30))
    print(find_rsa(nums3, 10))
    