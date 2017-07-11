def is_substring_simple(term, tstr):
    return term in tstr
        
def group_substrings(inlist):
    if not inlist: return
    
    len_in = len(inlist)
    
    inlist.sort(key=lambda x: len(x))

    out_list = []
    while inlist:
        picked = inlist.pop(0)
        group = [picked]
        for term in inlist:
            if is_substring_simple(picked, term):
                group.append(term)
                
        for term in group:
            if term in inlist:
                inlist.remove(term)
            
        out_list.append(group)
    
    return out_list
        

if __name__ == '__main__':
    strs1 = ["cow","cold","an","co","can"]
    strs2 = ["can", "cow", "cold"]
    strs3 = ["c", "ca", "can"]
    
    print(group_substrings(strs1))
    print(group_substrings(strs2))
    print(group_substrings(strs3))    