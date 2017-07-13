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
    
def print_preorder(root):
    if not root: return
    
    node = root
    wstack = []
    
    while node or wstack:
        if node:
            print(node.val, end=" ")
            wstack.append(node.right)
            node = node.left
        else:
            node = wstack.pop()
    print("")
    
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
    

def lcs_bst(root, val1, val2):
    if not root: return
    
    def _find_lcs(node, val1, val2):
        if not node: 
            print('hit?')
            return 
        
        if val1 <= node.val and node.val <= val2:
            return node.val
            
        if node.val < val1:
            return _find_lcs(node.right, val1, val2)
        else: # val2 < node.val
            return _find_lcs(node.left, val1, val2)
    
    return _find_lcs(root, min(val1,val2), max(val1, val2))          

    
if __name__ == '__main__':
    inlist = [8, 3, 13, 1, 5, 10, 17, None, None, 4, 7, None, 12, 15]
    root = build_from_list(inlist)
    print_preorder(root)
    print_inorder(root)
    
    print(lcs_bst(root, 1, 7))
    print(lcs_bst(root, 1, 12))
    print(lcs_bst(root, 5, 7))
    print(lcs_bst(root, 10, 15))
    