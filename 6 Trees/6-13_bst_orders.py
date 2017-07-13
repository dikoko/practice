class BTNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
def print_preorder(root):
    if not root: return
    
    wstack = [root]
    while wstack:
        node = wstack.pop()
        print(node.val, end=" ")
        if node.right:
            wstack.append(node.right)
        if node.left:
            wstack.append(node.left)
    print("")
    
def print_inorder(root):
    if not root: return
    
    wstack = []
    node = root
    while node or wstack:
        if node:
            wstack.append(node)
            node = node.left
        else:
            node = wstack.pop()
            print(node.val, end=" ")
            node = node.right
    print("")
    

def bst_pre_to_inorder(pre_list):
    if not pre_list: return 
    
    len_pre = len(pre_list)
    
    def _build(low, high):
        if low > high:
            return None
            
        sub_root = BTNode(pre_list[low])
        for i in range(low+1, high+1):
            if pre_list[i] >= sub_root.val:  ########
                break
        else:
            i = high + 1
        
        sub_root.left = _build(low+1, i-1)
        sub_root.right = _build(i, high)
        
        return sub_root
    
    root = _build(0, len_pre-1)

    out_list = []
    node = root
    wstack = []
    while node or wstack:
        if node:
            wstack.append(node)
            node = node.left
        else:
            node = wstack.pop()
            out_list.append(node.val)
            node = node.right
    return out_list
            


if __name__ == '__main__':
    pre_list = [10, 5, 1, 7, 40, 50]
    print(bst_pre_to_inorder(pre_list))
    