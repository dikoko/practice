# Given n non-negative integers a1, a2, ..., an,
# where each represents a point at coordinate (i, ai).
# 'n' vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
#
# Find two lines, which together with x-axis forms a container,
# such that the container contains the most water.
#
# Your program should return an integer which corresponds to the maximum area of water that can be contained
# ( Yes, we know maximum area instead of maximum volume sounds weird.
# But this is 2D plane we are working with for simplicity ).
# Note: You may not slant the container.


def max_capacity(containers):
    
    len_c = len(containers)
    max_cap = 0
    max_high = -1
    max_low = -1
    
    low = 0
    high = len_c-1
    while low < high:
        cap = (high-low) * min(containers[low], containers[high])
        if cap > max_cap:
            max_cap = cap
            max_high = high
            max_low = low
        if containers[low] > containers[high]:
            high -= 1
        else:
            low += 1
    
    return max_cap, max_low, max_high

if __name__ == '__main__':
    containers = [1, 5, 4, 3] # 6
    
    print(max_capacity(containers))