# Given an array, Find a subset array with Fibonacci numbers.
# e.g. [4,2,8,5,20,1,40,13,23] → [2,5,1,8,13]

def get_fib_numbers(nums):
    
    nums.sort()
    len_n = len(nums)
    
    prev_prev = 0
    prev = 1
    out_list = []
    fibo = 0
    i = 0
    while i < len_n and fibo <= nums[len_n-1]:
        fibo = prev_prev + prev
        
        while i < len_n and nums[i] < fibo:
            i += 1
        if i < len_n and nums[i] == fibo:
            out_list.append(nums[i])
        
        prev_prev = prev
        prev = fibo
    
    return out_list


if __name__ == '__main__':
    nums = [4,2,8,5,20,1,40,13,23]
    print(get_fib_numbers(nums))