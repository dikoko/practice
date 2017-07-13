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


def check_mirror(root):
    if not root: return False
    
    def _is_mirror(node1, node2):
        if not node1 and not node2: return True
        if not node1 or not node2: return False
        
        if node1.val != node2.val:
            return False
        else:
            is_left = _is_mirror(node1.left, node2.right)
            is_right = _is_mirror(node1.right, node2.left)
            return is_left and is_right
    
    return _is_mirror(root.left, root.right)

if __name__ == '__main__':
    inlist1 = [1, 2, 2, 3, 4, 4, 3]
    inlist2 = [1, 2, 2, None, 3, None, 3]
    
    root1 = build_from_list(inlist1)
    root2 = build_from_list(inlist2)
    
    print(check_mirror(root1))
    print(check_mirror(root2))
    
    