# You have a string of numbers, i.e. 123.
# You can insert a + or - sign in front of every number, or you can leave it empty.
# Find all of the different possibilities, make the calculation and return the sum.
# e.g.
# +1+2+3 = 6
# +12+3 = 15
# +123 = 123
# +1+23 = 24
# ...
# -1-2-3 = 6
# ...
# Return the sum of all the results.

def calculator(N):
    
    nlist = str(N)
    len_n = len(nlist)
    
    # 1,2,3 / 1,23 / 12,3 / 123
    def _terms(i):
        if i == len_n:
            return [[]]
        
        out_list = []
        for k in range(i, len_n):
            picked = nlist[i:k+1]
            picked_results = _terms(k+1)
            
            plus_results = []
            for item in picked_results:
                new_item = item[:] # bacause of side effects!
                new_item.append('+'+picked)
                plus_results.append(new_item)
            minus_results = []
            for item in picked_results:
                new_item = item[:]
                new_item.append('-'+picked)
                minus_results.append(new_item)
            
            out_list += plus_results
            out_list += minus_results
        return out_list
    
    results = _terms(0)
    results = [list(reversed(item)) for item in results]
    results = [sum(map(int, item)) for item in results]
    return results

if __name__ == '__main__':
    N = 123
    print(calculator(N))
    