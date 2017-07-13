class BTNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def build_bst_min_height(inlist):
    
    len_in = len(inlist)
    
    def _build(low, high):
        if low > high:
            return None
        mid = low + (high-low)//2
        
        subroot = BTNode(inlist[mid])
        subroot.left = _build(low, mid-1)
        subroot.right = _build(mid+1, high)
        
        return subroot
    
    root = _build(0, len_in-1)
    return root
    
def print_inorder(root):
    if not root: return
    node = root
    wstack = []
    
    while node or wstack:
        if node:
            wstack.append(node)
            node = node.left
        else:
            node = wstack.pop()
            print(node.val, end=" ")
            node = node.right
    print("")
    


if __name__ == '__main__':
    inlist = [1, 3, 4, 5, 7, 8, 10, 12, 13, 15, 17]
    
    root = build_bst_min_height(inlist)
    print_inorder(root)
    
