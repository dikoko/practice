import math
from collections import defaultdict

def biggest_plus(inlist):
    slist = defaultdict(set)
    
    max_i = -math.inf
    max_j = -math.inf
     
    for i, j in inlist:
        slist[i].add(j)
        if i > max_i:
            max_i = i
        if j > max_j:
            max_j = j
    
        
    def _checkone(i, j, direction):
        if i <0 or j <0 or i > max_i or j > max_j:
            return 0
        if j not in slist[i]:
            return 0
        
        if direction == 0:
            return 1 + _checkone(i-1, j, 0)
        elif direction == 1:
            return 1 + _checkone(i, j-1, 1)
        elif direction == 2:
            return 1 + _checkone(i+1, j, 2)
        else:
            return 1 + _checkone(i, j+1, 3)
        
    
    max_size = -math.inf
    max_size_i = -1
    max_size_j = -1
    
    for i, j in inlist:
        size = 1 + _checkone(i-1,j,0) + _checkone(i,j-1,1) + _checkone(i+1,j,2) + _checkone(i,j+1,3)
        if size > max_size:
            max_size = size
            max_size_i = i
            max_size_j = j
    
    return max_size, max_size_i, max_size_j    
         

if __name__ == '__main__':
    inlist = [(0,2), (0,5), 
            (1,0), (1,2), (1,4), (1,6),
            (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6),
            (3,2)]
    print(biggest_plus(inlist))
    