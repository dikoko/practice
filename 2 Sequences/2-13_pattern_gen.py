# Write a program to find pattern.
# 0: 1
# 1: 11
# 2: 21
# 3: 1211
# 4: 111221
# 5: 312211
# Iterate over the previous number, and find count for same number number. Append that count before number.
# e.g.,
# If input = 4, function should return 111221.

def pattern(N):
    if N < 0: return
    
    def _genp(n):
        if n == 0:
            return '1'
        if n == 1:
            return '11'
        
        prev_pattern = _genp(n-1)
        count = 1
        out_list = []
        prev = prev_pattern[0]
        for c in prev_pattern[1:]:
            if c == prev:
                count += 1
            else: # flush before
                out_list.append(str(count)+prev)
                count = 1
                prev = c
        out_list.append(str(count)+prev)
        return "".join(out_list)
    
    return _genp(N)
            

if __name__ == '__main__':
    N = 4
    print(pattern(N))
    