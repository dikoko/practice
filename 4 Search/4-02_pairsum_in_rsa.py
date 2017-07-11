def pair_sum(nums, T):
    
    len_n = len(nums)
    
    def find_pivot(low, high):
        if low > high:
            return 0
        mid = low + (high-low)//2
        
        if low < mid and nums[mid-1] > nums[mid]:
            return mid
        if mid < high and nums[mid] > nums[mid+1]:
            return mid+1
        
        if nums[low] <= nums[mid]:
            return find_pivot(mid+1, high)
        else:
            return find_pivot(low, mid-1)
    
    pivot = find_pivot(0, len_n-1)

    def get_val(index):
        return nums[(pivot + index)%len_n]
    
    low = 0
    high = len_n-1
    out_list = []
    while low < high:
        temp_sum = get_val(low) + get_val(high)
        if temp_sum == T:
            out_list.append((get_val(low), get_val(high)))
            low += 1  
            high -= 1
        elif temp_sum > T:
            high -= 1
        else:
            low += 1
    
    return out_list
    

if __name__ == '__main__':
    nums1 = [11, 15, 6, 8, 9, 10] #, x = 16 → True, (6, 10)
    nums2 = [11, 15, 26, 38, 9, 10] #, x = 35 → True (26, 9)
    nums3 = [11, 15, 26, 38, 9, 10] #, x = 45 → False 
    
    print(pair_sum(nums1, 16))
    print(pair_sum(nums2, 35))
    print(pair_sum(nums3, 45))