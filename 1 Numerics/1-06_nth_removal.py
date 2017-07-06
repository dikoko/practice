def new_nums_bf(N):
    num = 0        
    while N != 0:
        num += 1
        if '9' in str(num):
            continue
        N -= 1
    
    return num

def num_9num(N):
    if N < 9: return 0

    _dtable = {} # cache for the memoization
    def _D(d):
        if d in _dtable:
            return _dtable[d]   
        if d < 1: 
            _dtable[d] = 0
            return 0
        if d == 1: # 0~9 , 1digit
            _dtable[d] = 1
            return 1 
        _dtable[d] = _D(d-1)*9 + 10**(d-1) 
        return _dtable[d]   
    
    def _num9(n):
        if n < 9:
            return 0
        if n == 9:
            return 1
            
        d = len(str(n)) # digit length of n
        MSD = int(str(n)[0])
        
        if MSD < 9: # 0, 1, 2, 3..
            return MSD*_D(d-1) + _num9(n % 10**(d-1))
        elif MSD == 9:
            return MSD*_D(d-1) + 1 + (n % 10**(d-1))
    
    return _num9(N)

def new_nums(N):
    num = num_9num(N) # num is how many having 9digit numbers till N
    prev_num = 0
    while num - prev_num > 0:
        N += (num - prev_num)
        prev_num = num
        num = num_9num(N)
    
    return N
        

if __name__ == '__main__':
    print(new_nums_bf(9))
    print(new_nums(9))
    print(new_nums_bf(112))
    print(new_nums(112)) # 134
