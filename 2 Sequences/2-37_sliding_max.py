# A long array A[] is given to you.
# There is a sliding window of size w which is moving from the very left of the array to the very right.
# You can only see the w numbers in the window. Each time the sliding window moves rightwards by one position.
#
# e.g:
# The array is [1 3 -1 -3 5 3 6 7], and w is 3.
# Window position    Max
# [1 3 -1] -3 5 3 6 7    3
# 1 [3 -1 -3] 5 3 6 7    3
# 1 3 [-1 -3 5] 3 6 7    5
# 1 3 -1 [-3 5 3] 6 7    5
# 1 3 -1 -3 [5 3 6] 7    6
# 1 3 -1 -3 5 [3 6 7]    7
# Input: A long array A[], and a window width w
# Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
# Requirement: Find a good optimal way to get B[i]
# Note: If w > length of the array, return 1 element with the max of the array.

def sliding_max_bf(nums, w):
    
    len_n = len(nums)
    out_list = []
    for i in range(len_n - w + 1):
        max_num = max(nums[i:i+w])
        out_list.append(max_num)
    
    return out_list
    
def sliding_max_better(nums, w):
    len_n = len(nums)
    
    mqueue = [0]
    for i in range(1,w+1):
        while mqueue and nums[i] > nums[mqueue[-1]]:
            mqueue.pop()
        mqueue.append(i)
    
    out_list = [nums[mqueue[0]]]
    for i in range(w, len_n):
        if i-w >= mqueue[0]:
            mqueue.pop(0)
        while mqueue and nums[i] > nums[mqueue[-1]]:
            mqueue.pop()
        mqueue.append(i)
        out_list.append(nums[mqueue[0]])
    
    return out_list
        

if __name__ == '__main__':
    A1 = [1, 3, -1, -3, 5, 3, 6, 7] # [3, 3, 5, 5, 6, 7]
    A2 = [1, 1] # [1, 1]
    print(sliding_max_bf(A1, 3))
    print(sliding_max_bf(A2, 1))
    print(sliding_max_better(A1, 3))
    print(sliding_max_better(A2, 1))
