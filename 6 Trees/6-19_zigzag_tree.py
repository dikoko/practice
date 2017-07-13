class BTNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def build_from_list(vals):
    if not vals: retrun
    
    root = BTNode(vals.pop(0))
    wqueue = [root]
    while vals:
        node = wqueue.pop(0)
        val = vals.pop(0)
        if val:
            node.left = BTNode(val)
            wqueue.append(node.left)
        if vals:
            val = vals.pop(0)
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


def zigzag_list(root):
    if not root: return
    
    wqueue = [root, None]
    
    out_list = []
    level = []
    is_reverse = False
    while wqueue:
        if not is_reverse:
            node = wqueue.pop(0)
        else:
            node = wqueue.pop()
        
        if node:
            level.append(node.val)
            
            if not is_reverse:
                if node.left:
                    wqueue.append(node.left)
                if node.right:
                    wqueue.append(node.right)
            else:
                if node.right:
                    wqueue.insert(0, node.right)
                if node.left:
                    wqueue.insert(0, node.left)
        else:
            if wqueue:
                if not is_reverse:
                    wqueue.insert(0,None)
                else:
                    wqueue.append(None)
            out_list.append(level)
            level = []
            is_reverse = not is_reverse
        
    return out_list

    

if __name__ == '__main__':
    vals1 = [3, 9, 20, None, None, 15, 7]
    vals2 = [8, 3, 13, 1, 5, 10, 17, None, None, 4, 7, None, 12, 15]
    root1 = build_from_list(vals1)
    print(zigzag_list(root1))
    root2 = build_from_list(vals2)
    print(zigzag_list(root2))