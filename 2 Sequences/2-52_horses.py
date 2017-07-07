# You are given a sequence of black and white horses,
# and a set of K stables numbered 1 to K.
# You have to accommodate the horses into the stables in such a way that the following conditions are satisfied:
#
# You fill the horses into the stables preserving the relative order of horses.
# For instance, you cannot put horse 1 into stable 2 and horse 2 into stable 1. 
# You have to preserve the ordering of the horses.
# No stable should be empty and no horse should be left unaccommodated.
# Take the product (number of white horses * number of black horses)
# for each stable and take the sum of all these products.
# This value should be the minimum among all possible accommodation arrangements
#
# e.g.
# Input: {WWWB} , K = 2
# Output: 0
#
# We have 3 choices {W, WWB}, {WW, WB}, {WWW, B}
# for first choice we will get 1*0 + 2*1 = 2.
# for second choice we will get 2*0 + 1*1 = 1.
# for third choice we will get 3*0 + 0*1 = 0.
# Of the 3 choices, the third choice is the best option.

from operator import itemgetter

def horse_product(wb_list):
    out_list = []
    for wbs in wb_list:
        w_count = 0
        b_count = 0
        for h in wbs:
            if h == 'W':
                w_count += 1
            elif h == 'B':
                b_count += 1
        out_list.append(w_count*b_count)
    
    return sum(out_list)

def horses_stables(horses, K):
    
    len_h = len(horses)
    
    def _accommodate(i, k):
        if i == len_h and k == 0:
            return [[]]
        if i == len_h or k == 0:
            return []
        
        out_list = []
        for j in range(i, len_h):
            picked = horses[i:j+1]
            picked_results = _accommodate(j+1, k-1)
            for item in picked_results:
                item.append(picked)
            out_list += picked_results
        
        return out_list
    
    results = _accommodate(0, K)
    results = [list(reversed(item)) for item in results]
    results = list(map(horse_product, results))
    min_index, _ = min(enumerate(results), key=itemgetter(1))
    return min_index
            
    


if __name__ == '__main__':
    horses = 'WWWB'
    K = 2
    horses2 = 'BWWWWBBWWBWBWWBBBBBWBWWBBBWWWWBBBW' # it will not end...
    K2 = 28 # 0
    print(horses_stables(horses, K))
    print(horses_stables(horses2, K2))
    