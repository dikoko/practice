# Given an array of n elements which contains elements from 0 to n-1,
# with any of these numbers appearing any number of times.
# Find these repeating numbers in O(n) and using only constant memory space. Try to do it in one pass.
# e.g
# [4, 2, 0, 5, 2, 0, 1] -> [0, 2]
# [1, 2, 3, 0, 0, 1, 3, 6, 6,6] -> [0, 1, 3, 6]

def find_duplicate(nums):
    
    len_n = len(nums)
    
    out_list = []
    for i in range(len_n):
        index = nums[i]
        if index < 0: # we have to get original val and index
            index = (-1*index)-1
        
        if nums[index] < 0: # already visited:
            out_list.append(index)
        else: # make negation, the first visit
            nums[index] = (nums[index]+1)*-1
    
    return out_list

# ol = [2, 0]
#  0  1  2  3   4  5  6
# [-5,-3, -1,5, -3,-1, 1]
# i = 0
# index = 4
# i = 1
# index = 2
# i = 2
# index = -1 -> 0
# i = 3
# index = 5
# i = 4
# index = -3 ->2
# i = 5
# index = -1 -> 0
# i = 6
# index = 1

if __name__ == '__main__':
    nums1 = [4, 2, 0, 5, 2, 0, 1] # return: 0, 2 
    nums2 = [1, 2, 3, 0, 0, 1, 3, 6, 6, 6] # return 0, 1, 3, 6 

    print(find_duplicate(nums1))
    print(find_duplicate(nums2))    