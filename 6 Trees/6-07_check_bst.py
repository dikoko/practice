import math

class BTNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def build_from_list(inlist):
    if not inlist: return
    
    root = BTNode(inlist.pop(0))
    wqueue = [root]
    
    while inlist:
        node = wqueue.pop(0)
        val = inlist.pop(0)
        if val:
            node.left = BTNode(val)
            wqueue.append(node.left)
        if inlist:
            val = inlist.pop(0)
            if val:
                node.right = BTNode(val)
                wqueue.append(node.right)
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
    

def check_bst(root):
    if not root: return False
    
    def _check(node):
        if not node: 
            return True, math.inf, -math.inf # is / min / max
        
        is_left, l_min, l_max = _check(node.left)
        is_right, r_min, r_max = _check(node.right)
        
        if not is_left or not is_right:
            return False, 0, 0
        
        if l_max < node.val and node.val < r_min:
            return True, min(node.val, l_min), max(node.val, r_max)
        else:
            return False, 0, 0
    
    return _check(root)
        

if __name__ == '__main__':
    inlist1 = [8, 3, 13, 1, 5, 10, 17, None, None, 4, 7, None, 12, 15]
    root1 = build_from_list(inlist1)
    # print_inorder(root)

    inlist2 = [8, 3, 13, 1, 2, 10, 17, None, None, 4, 7, None, 12, 15]
    root2 = build_from_list(inlist2)
    
    print(check_bst(root1))
    print(check_bst(root2))
    