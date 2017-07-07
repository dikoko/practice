# Given an array of nonnegative integers and a positive number X,
# determine if there exists a subset of the elements of array with sum equal to X.
# e.g. [3, 2, 7, 1] / 6 → True (3, 2, 1)

# subarray: contiguous sequence
# subset: non-contiguous sequence
# subset sum, nonnegative, no size limit -> a DP solution
def subset_sum_dp(nums, X):
    if not nums: return
    if X < 0: return
    
    len_n = len(nums)
    T = [[False]*(X+1) for _ in range(len_n)] # X+1: 0 to X
    
    # fill the first col - we can make 0 always with 0 uses
    for i in range(len_n):
        T[i][0] = True
        
    # fill the first row with the first number only - nums[0]
    for j in range(1, X+1):
        if nums[0] == j:
            T[0][j] = True
    # and the rest rows - use nums[i] or not
    for i in range(1, len_n):
        for j in range(1, X+1):
            T[i][j] = T[i-1][j] or T[i][j - nums[i]] # T[i][j-nums[i]] means uses nums[i]
    
    for i in range(len_n):
        print(T[i])
    
    return T[len_n-1][X]

# a recursive solution
# can be slow, but relatively intuitive and easy to find the set
def subset_sum(nums, X):
    if not nums: return
    if X < 0: return
    
    len_n = len(nums)
    def _subsetsum(i, x):
        if x == 0: # success case
            return [[]]
        if i == len_n or x < 0: # failure case
            return []
            
        picked = nums[i]
        picked_results = _subsetsum(i+1, x - picked) # using nums[i]
        unpicked_results = _subsetsum(i+1, x) # not using nums[i]
        
        for item in picked_results:
            item.append(picked)
        
        return picked_results + unpicked_results
    
    results = _subsetsum(0, X)
    return [list(reversed(item)) for item in results]
        
    
if __name__ == '__main__':
    nums = [3, 2, 7, 1]
    print(subset_sum_dp(nums, 6))
    print(subset_sum(nums, 6))    