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

def print_levelorder(root):
    if not root: return
    
    wqueue = [root, None]    
    while wqueue:
        node = wqueue.pop(0)
        if node:
            print(node.val, end=" ")
            if node.left:
                wqueue.append(node.left)
            if node.right:
                wqueue.append(node.right)
        else:
            print("")
            if wqueue:
                wqueue.append(None)

    
def mirroring(root):
    if not root: return
    
    def _mirror(original):
        if not original: return
        
        node = BTNode(original.val)    
        node.right = _mirror(original.left)
        node.left = _mirror(original.right)
        
        return node
    
    mroot = _mirror(root)
    return mroot        
        
        


if __name__ == '__main__':
    inlist1 = [8, 3, 13, 1, 5, 10, 17, None, None, 4, 7, None, 12, 15]
    root1 = build_from_list(inlist1)
    mroot = mirroring(root1)
    print_levelorder(root1)
    print("--")
    print_levelorder(mroot)    