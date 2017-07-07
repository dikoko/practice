# Determine if any 3 integers in an array sum to 0.
# Note: The following situation assumes that repetitions
# (i.e. can choose the same array element more than once.
# so the array [-5,1,10] contains a zero sum (-5-5+10) and so does [0] (0+0+0) )

def multi_subset_sum(nums):
    if not nums: return
    len_n = len(nums)
    
    def _msubset_sum(i, k): # find all multi-3choice combinations
        if k == 0: # success case
            return [[]] 
        if i == len_n: # failure case
            return [] 
            
        picked = nums[i]
        picked_results = _msubset_sum(i, k-1) # do not proceed i, consumes k
        unpicked_results = _msubset_sum(i+1, k) # do not use, so skip i
        for item in picked_results:
            item.append(picked)
        
        return picked_results + unpicked_results
    
    combis = _msubset_sum(0, 3)
    return [item for item in combis if sum(item) == 0]
        

if __name__ == '__main__':
    nums1 = [-5, 1, 10]
    nums2 = [0]
    print(multi_subset_sum(nums1))
    print(multi_subset_sum(nums2))    