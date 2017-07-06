# Given an unsorted array, Find the k-th largest number from the array.
# e.g. [4, 2, 5, 3, 9, 1] / 0 → 9

# the best (amortized O(N)) solution with the quick-sort like algorithm 
def find_kth_largest(nums, K):
    if not nums: return
    len_nums = len(nums)
    if K < 0 or K >len_nums: return
    
    def _findkth(subnums,k):
        if not subnums: return
        len_subnums = len(subnums)
        if k < 0 or k > len_subnums: return
        
        pivot = subnums[0]
        left = []
        right = []
        
        for i in range(1, len_subnums):
            if subnums[i] > pivot:
                right.append(subnums[i])
            else:
                left.append(subnums[i])
        
        if len(left) == k:
            return pivot
        elif len(left) > k:
            return _findkth(left, k)
        else:
            return _findkth(right, k - len(left)-1)
        
    return _findkth(nums, len_nums-K-1)

if __name__ == '__main__':
    nums1 = [4, 2, 5, 3, 9, 1]
    
    print(find_kth_largest(nums1, 0))
