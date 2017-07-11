# Given an input string and a dictionary of words,
# find out if the input string can be segmented into a space-separated sequence of dictionary words.
# Ex: "bedbathandbeyond" would be "bed bath and beyond" which are all dictionary words.

def word_break(words, instr):
    len_in = len(instr)
    
    def _wordb(i):
        if i == len_in: return [[]]
        
        picked = None
        out_list = []
        for k in range(i+1, len_in+1):
            if instr[i:k] in words:
                picked = instr[i:k]
                picked_results = _wordb(k)
                for item in picked_results:
                    item.append(picked)
                out_list += picked_results

        if not picked:
            return []
        
        return out_list
    
    results = _wordb(0)
    
    return [list(reversed(item)) for item in results]
        


if __name__ == '__main__':
    words = {'i', 'like', 'a', 'apple', 'an', 
            'mobile', 'ice', 'cream', 'icecream',
            'man', 'go', 'mango'}
            
    str1 = 'ilike'
    str2 = 'ilikeapple'
    str3 = 'ilikeaapplemobile'
    str4 = 'ilikeamangoicecream'
    str5 = 'ihatei'
    
    print(word_break(words, str1))
    print(word_break(words, str2))
    print(word_break(words, str3))
    print(word_break(words, str4))
    print(word_break(words, str5))    