# A "derangement" of a sequence is a permutation where no element appears in its original position.
# For example ECABD is a derangement of ABCDE, given a string, may contain duplicate char,
# please out put all the derangement

def get_derangement(instr):
    if not instr: return
    
    inlist = list(instr)
    len_in = len(inlist)
    
    def _derange(i, sublist):
        if not sublist: return [[]]
        
        out_list = []
        len_sub = len(sublist)
        for j in range(len_sub):
            if sublist[j] != inlist[i]:
                picked = sublist[j]
                picked_results = _derange(i+1, sublist[:j] + sublist[j+1:])
                for item in picked_results:
                    item.append(picked)
                out_list += picked_results
                
        return out_list
        
    results = _derange(0, inlist)
    return ["".join(reversed(item)) for item in results]

if __name__ == '__main__':
    instr = 'ABCDE'
    print(get_derangement(instr))