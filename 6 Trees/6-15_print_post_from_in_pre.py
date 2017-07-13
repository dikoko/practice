class BTNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_from_list(in_list, pre_list):
    
    len_in = len(in_list)
    
    def _build(low, high, pindex):
        if low > high:
            return 
            
        sub_root = BTNode(pre_list[pindex])
        for i in range(low, high+1):
            if in_list[i] == sub_root.val:
                break
        else:
            i = high+1
        
        sub_root.left = _build(low, i-1, pindex+1)
        sub_root.right = _build(i+1, high, pindex+(i-low)+1)
        
        return sub_root
    
    root = _build(0, len_in-1, 0)
    
    node = root
    wstack = []
    prev = 'dummy'
    out_list = []
    while node or wstack:
        if node:
            if node.right == prev:
                out_list.append(node.val)
                prev = node
                node = wstack.pop() if wstack else None
            elif node.left == prev:
                prev = node
                wstack.append(node)
                node = node.right
            else:
                prev = node
                wstack.append(node)
                node = node.left
        else:
            prev = None
            node = wstack.pop() if wstack else None
    
    return out_list
        


if __name__ == '__main__':
    in_list = [4, 2, 5, 1, 3, 6]
    pre_list = [1, 2, 4, 5, 3, 6]
    
    print(build_from_list(in_list, pre_list))