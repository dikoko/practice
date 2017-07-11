# Given a string, find all possible combinations of the upper and lower case of each Alphabet char,
# keep the none Alphabet char as it is.
# example1 s = "ab", return: "Ab", "ab", "aB", "AB"
# example2 s = "a1b", return: "A1b", "a1b", "a1B", "A1B"

def permu_tweak(instr):
    len_s = len(instr)
    
    def _permute(i):
        if i == len_s:
            return [[]]
        
        picked = instr[i]
        if picked.isalpha():
            lower_results = _permute(i+1) # we need two instances for each(lower, upper)
            upper_results = _permute(i+1)
            for item in lower_results:
                item.append(picked.lower())
            for item in upper_results:
                item.append(picked.upper())
            return lower_results + upper_results
        else:
            picked_results = _permute(i+1)
            for item in picked_results:
                item.append(picked)
            return picked_results
    
    results = _permute(0)
    
    return ["".join(reversed(item)) for item in results]
        
        
if __name__ == '__main__':
    s1 = 'ab'
    s2 = 'a1b'
    
    print(permu_tweak(s1))
    print(permu_tweak(s2))    