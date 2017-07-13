
def check_leaf(pre_list):
    
    def _check(low, high):
        if low > high:
            return []
        if low == high:
            return [pre_list[low]]
        
        root_val = pre_list[low]
        for i in range(low+1, high+1): ####### low + 1
            if pre_list[i] >= root_val:
                break
        else:
            i = high+1
        
        left_leaves = _check(low+1, i-1)
        right_leaves = _check(i, high)
        
        return left_leaves + right_leaves
    
    return _check(0, len(pre_list)-1)
    


if __name__ == '__main__':
    pre_list = [5, 3, 2, 4, 8, 7, 9]
    
    print(check_leaf(pre_list))
    