# Find all subsets of size K in an array that sum up to target T.
# The array may contains negative number.
# def combination_sum(nums, T, K)
# Returns a list of subset numbers
# e.g. [3, 2, 7, 1] / T=6, K=3 / [1, 2, 3]
# e.g. [-3, 2, -1, 4, 5, 3, 7] / T=3, K=3 / [4, 2, -3], [7,-1,-3]

def combination_sum(nums, T, K):
    if not nums: return
    len_n = len(nums)
    
    def _combs(i, t, k):
        if t == 0 and k == 0: # success case
            return [[]]
        if i == len_n or k <= 0: # failure case
            return []
        
        picked = nums[i]
        picked_results = _combs(i+1, t-picked, k-1)
        unpicked_results = _combs(i+1, t, k)
        
        for item in picked_results:
            item.append(picked)
        
        return picked_results + unpicked_results
    
    results = _combs(0, T, K)
    return [list(reversed(item)) for item in results]


if __name__ == '__main__':
    nums1 = [3, 2, 7, 1]
    nums2 = [-3, 2, -1, 4, 5, 3, 7]
    
    print(combination_sum(nums1, 6, 3))
    print(combination_sum(nums2, 3, 3))
    