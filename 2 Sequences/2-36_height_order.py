# You are given the following : A positive number N
# Heights : A list of heights of N persons standing in a queue.
# Infronts : A list of numbers corresponding to each person (P)
#   that gives the number of persons who are taller than P and standing in front of P
# You need to return list of actual order of person’s height. Consider that heights will be unique.

def height_order(heights, infronts):
    
    _fmap = {}
    len_h = len(heights)
    
    for i in range(len_h):
        _fmap[heights[i]] = infronts[i]
        
    print(_fmap)
    
    orders = [-1]*len_h
    
    heights.sort()
    
    for h in heights: # this can be better with Fenwick Tree
        count = -1  #########
        for i in range(len_h):
            if orders[i] == -1:
                count += 1
            if count == _fmap[h]:
                orders[i] = h
                break
    
    return orders


if __name__ == '__main__':
    heights = [5, 3, 2, 6, 1, 4]
    infronts = [0, 1, 2, 0, 3, 2]
    
    print(height_order(heights, infronts))
