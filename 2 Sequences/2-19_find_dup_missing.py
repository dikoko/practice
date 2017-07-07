# You are given a read only array of n integers from 1 to n.
# Each integer appears exactly once except A which appears twice and B which is missing. Return A and B.
# Note: Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?
# Note that in your output A should precede B.
# e.g.:
# [3 1 2 5 3] -> [3, 4]
# A = 3, B = 4
# Your algorithm should run in O(n) time and use constant space.

def missing_duplicate(nums):
    
    len_n = len(nums)
    
    # negation
    duplicate = -1
    missing = -1
    for i in range(len_n):
        index = nums[i]
        if index < 0:
            index *= -1
        
        index -= 1 # make it zero-based index
        
        if nums[index] < 0: # already visit. the duplicate
            duplicate = index + 1
        else:
            nums[index] *= -1
    
    for i in range(len_n):
        if nums[i] > 0: # not visited one
            missing = i + 1
    
    return duplicate, missing
        
    

if __name__ == '__main__':
    nums1 = [3, 1, 2, 5, 3] # 3, 4
    
    print(missing_duplicate(nums1))