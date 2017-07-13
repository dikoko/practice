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
    

def root_to_leaf_paths(root):
    if not root: return
    
    node = root
    wstack = []
    prev = "dummy"
    all_paths = []
    while node or wstack:
        if node:
            if node.right == prev:
                ## Visit here
                if not node.left and not node.right:
                    path = [n.val for n in wstack] # in post order, wstack is the path to the node
                    path.append(node.val)
                    all_paths.append(path)
                
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
    
    return all_paths
    
if __name__ == '__main__':
    inlist = [8, 3, 13, 1, 5, 10, 17, None, None, 4, 7, None, 12, 15]
    root = build_from_list(inlist)
    print_preorder(root)
    print_inorder(root)
    
    print(root_to_leaf_paths(root))