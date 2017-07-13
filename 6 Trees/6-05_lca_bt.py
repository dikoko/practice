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
        node_val = inlist.pop(0)
        if node_val:
            node.left = BTNode(node_val)
            wqueue.append(node.left)
        if inlist:
            node_val = inlist.pop(0)
            if node_val: 
                node.right = BTNode(node_val)
                wqueue.append(node.right)
    
    return root
    
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
    
def find_lca(root, val1, val2):
    if not root: return
    
    def _findlca(node):
        if not node:
            return False, False, None

        if node.val == val1:
            return True, False, None
        if node.val == val2:
            return False, True, None
        
        left_v1, left_v2, left_lca = _findlca(node.left)
        right_v1, right_v2, right_lca = _findlca(node.right)
        
        if left_v1 and left_v2: # already found on left
            return True, True, left_lca
        if right_v1 and right_v2:
            return True, True, right_lca
            
        my_v1 = left_v1 or right_v1
        my_v2 = left_v2 or right_v2
        if my_v1 and my_v2: # i'm the lca
            return True, True, node
        else:
            return my_v1, my_v2, None
    
    _, _, lca = _findlca(root) 
    if lca:
        return lca.val
    else:
        print('no lca')
            
        
        
    
    
    

if __name__ == '__main__':
    inlist = [8, 3, 13, 1, 5, 10, 17, None, None, 4, 7, None, 12, 15]
    root = build_from_list(inlist)
    print_inorder(root)
    print(find_lca(root, 1, 7))
    
    