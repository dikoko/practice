# Given a sorted array of integers (including negatives),
# return a sorted array of squares of those integers.
# e.g. [-6, -4, 1, 2, 3 ,5] → [1, 4, 9, 16, 25, 36]

def sorted_squares(nums):
    
    len_n = len(nums)
    i = 0
    out_list = []
    while nums[i] < 0:
        i += 1
    # now i is the first 0 or positive num index (because it is already sorted)
    if i > 0:
        low = i-1
        high = i
    else: # all are positive
        return [n*n for n in nums]
    
    while low >= 0 and high < len_n:
        if abs(nums[low]) < abs(nums[high]):
            out_list.append(nums[low]**2)
            low -= 1
        else:
            out_list.append(nums[high]**2)
            high += 1
    
    if low < 0:
        while high < len_n:
            out_list.append(nums[high]**2)
            high += 1
    else:
        while low >= 0:
            out_list.append(nums[low]**2)
            low -= 1
    
    return out_list


if __name__ == '__main__':
    nums = [-6, -4, 1, 2, 3 ,5] # [1, 4, 9, 16, 25, 36]

    print(sorted_squares(nums))