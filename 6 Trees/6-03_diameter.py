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
    

def diameter(root):
    if not root: return
     
    def _find_height(node):
        if not node: return 0
        if not node.left and not node.right:
            return 1
        
        left_height = _find_height(node.left)
        right_height = _find_height(node.right)
        
        return max(left_height, right_height) + 1
    
    return _find_height(root.left) + _find_height(root.right)
        
            
    
if __name__ == '__main__':
    inlist = [8, 3, 13, 1, 5, 10, 17, None, None, 4, 7, None, 12, 15]
    root = build_from_list(inlist)
    print_preorder(root)
    print_inorder(root)
    
    print(diameter(root))
    
    