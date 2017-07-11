
def find_pivot(nums):
    len_n = len(nums)
    
    def _findp(low, high):
        if low > high: # no shift - sorted
            return 0
        mid = low + (high-low)//2
        
        if low < mid and nums[mid-1] > nums[mid]:
            return mid
        if mid < high and nums[mid] > nums[mid+1]:
            return mid+1
        
        if nums[low] <= nums[mid]: # left is sorted - pivot is at right
            return _findp(mid+1, high)
        else:
            return _findp(low, mid-1)
        
    return _findp(0, len_n-1)
        
        

if __name__ == '__main__':
    nums1 = [15, 18, 2, 3, 6, 12] # 2
    nums2 = [7, 9, 11, 12, 5]  # 4
    nums3 = [7, 9, 11, 12, 15] # 0
    
    print(find_pivot(nums1))
    print(find_pivot(nums2))
    print(find_pivot(nums3))
    