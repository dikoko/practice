# Find length of longest substring of a given string of digits,
# such that sum of digits in the first half and second half of the substring is same.
# e.g. “142124” -> 6, “9430723” -> 4

def longest_same_half_sum(instr):
    len_s = len(instr)
    max_k = len_s//2
    
    inlist = list(map(int, list(instr)))
    max_len = 0
    max_list = []
    for k in range(1, max_k+1):
        for i in range(len_s - 2*max_k +1):
            sum1 = sum(inlist[i:i+k])
            sum2 = sum(inlist[i+k: i+2*k])
            if sum1 == sum2:
                if 2*k > max_len:
                    max_len = 2*k
                    max_list = [(i, i+2*k-1)]
                elif 2*k == max_len:
                    max_list.append((i, i+2*k-1))
                    
    return max_len, max_list
                    
                
def longest_same_half_sum_dp(instr):
    inlist = list(map(int,list(instr)))
    len_s = len(inlist)
    
    max_k = len_s//2
    max_len = 0
    max_list = []
    
    for k in range(1, max_k+1):
        sum1 = sum(inlist[0:k])
        sum2 = sum(inlist[k:2*k])
        for i in range(len_s - 2*max_k + 1):
            if i != 0:
                sum1 = sum1 - inlist[i-1] + inlist[i+k-1] #######
                sum2 = sum2 - inlist[i+k-1] + inlist[i+2*k-1] #######
            if sum1 == sum2:
                if 2*k > max_len:
                    max_len = 2*k
                    max_list = [(i, i+2*k-1)]
                elif 2*k == max_len:
                    max_list.append((i, i+2*k-1))
    
    return max_len, max_list
    


if __name__ == '__main__':
    instr1 = "142124"
    instr2 = "9430723" 
    
    print(longest_same_half_sum(instr1))
    print(longest_same_half_sum(instr2))
    print(longest_same_half_sum_dp(instr1))
    print(longest_same_half_sum_dp(instr2))