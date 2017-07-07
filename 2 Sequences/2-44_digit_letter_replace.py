# Given a mapping from digits to list of letters and a string of digits of arbitrary length
# determine all possible ways to replace the digits with letters.

def digit_letter(mapping, instr):
    
    len_s = len(instr)
    
    def _dletter(i):
        if i == len_s: 
            return [[]]
        
        ith_list = mapping[instr[i]]
        out_list = []
        for ch in ith_list:
            next_results = _dletter(i+1)
            for item in next_results:
                item.append(ch)
            out_list += next_results
        
        return out_list
    
    results = _dletter(0)
    return ["".join(reversed(item)) for item in results]
                
    

if __name__ == '__main__':
    mapping = {'1': ['A', 'B', 'C'], 
                '2': ['D', 'E', 'F']}
                
    instr = '12'
    
    print(digit_letter(mapping, instr))