# Given an input string "aabbccba", find the shortest substring from the alphabet "abc".
# In the above example, there are these substrings "aabbc", "aabbcc", "ccba" and "cba".
# However the shortest substring that contains all the characters in the alphabet is "cba", so "cba" must be the output.
# Output doesn’t need to maintain the ordering as in the alphabet.
# e.g.:
# input = "abbcac", alphabet="abc" Output : shortest substring = "bca".

from collections import defaultdict

def shortest_substring(instr, alpha):
    
    len_s = len(instr)
    len_a = len(alpha)
    
    # make a counter with alpha
    _count = defaultdict(int)
    
    def check_count():
        for a in alpha:
            if _count[a] == 0:
                return False
        return True
        
    low = 0
    high = 0
    min_len = len_s+1
    out_list = []
    _count[instr[0]] += 1

    while high < len_s:
        # char pointer is high
        if check_count():
            current_len = high - low +1
            if current_len < min_len:
                min_len = current_len
                out_list = [instr[low:high+1]]
            elif current_len == min_len:
                out_list.append(instr[low:high+1])
            # then, we're going to try reduce the substring size
            if low == high:
                high += 1
                if high < len_s:
                    _count[instr[high]] += 1
            _count[instr[low]] -= 1
            low += 1
        else:
            high += 1
            if high < len_s:
                _count[instr[high]] += 1
    
    return out_list

# ml = 3
# ol = [cba]
# _c{1, 1, 0}
# 01234567
# aabbccba len_s = 8
# l:h = 6:8 

if __name__ == '__main__':
    instr1 = "aabbccba"
    alpha1 = 'abc' # 'cba'
    
    instr2 = "abbcac"
    alpha2 = 'abc' # 'bca'
    
    print(shortest_substring(instr1, alpha1))
    print(shortest_substring(instr2, alpha2))
    
    