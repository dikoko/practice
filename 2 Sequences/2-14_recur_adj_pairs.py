# Given a string “ABCCBCBA”,
# give an algorithm for recursively removing the adjacent characters if they are the same.
# e.g. ABCCBCBA -> ABBCBA -> ACBA

# do not use shift copies, try to do it O(n)
def remove_recur_pairs(instr):
    if not instr: return
    len_s = len(instr)
    inlist = list(instr)
    
    low = 0
    high = 1
    while low < high and high < len_s:
        if inlist[low] == inlist[high]:
            while inlist[high] == inlist[low]:
                high += 1
            low -= 1
        else:
            inlist[low+1] = inlist[high]
            low += 1
            high += 1
    return "".join(inlist[:low+1])
         
    

if __name__ == '__main__':
    instr1 = 'ABCCBCBA'
    instr2 = 'ABCCCCBACA'
    print(remove_recur_pairs(instr1))
    print(remove_recur_pairs(instr2))    