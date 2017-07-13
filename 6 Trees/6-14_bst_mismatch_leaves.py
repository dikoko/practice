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
    
def print_levelorder(root):
    wqueue = [root, None]
    while wqueue:
        node = wqueue.pop(0)
        if node:
            print(node.val, end=" ")
            if node.left: wqueue.append(node.left)
            if node.right: wqueue.append(node.right)
        else:
            if wqueue:
                wqueue.append(None)
            print("")
    print("")
        
def bst_mismatch(pl1, pl2):
    if not pl1 or not pl2: return 
    
    len_p1 = len(pl1)
    len_p2 = len(pl2)
    
    def _build(pre_list, low, high):
        if low > high:
            return None
            
        sub_root = BTNode(pre_list[low])
        for i in range(low+1, high+1):
            if pre_list[i] >= sub_root.val: ########
                break
        else:
            i = high + 1
        
        sub_root.left = _build(pre_list, low+1, i-1)
        sub_root.right = _build(pre_list, i, high)
        
        return sub_root
    
    root1 = _build(pl1, 0, len_p1-1)
    root2 = _build(pl2, 0, len_p2-1)
    
    node1 = root1
    node2 = root2
    wstack1 = []
    wstack2 = []

    while (node1 and node2) or (wstack1 and wstack2):
        # print(node1.val if node1 else None, node2.val if node2 else None)
        # print([item.val for item in wstack1], [item.val for item in wstack2])
        if node1 and node2:
            wstack1.append(node1)
            wstack2.append(node2)
            node1 = node1.left
            node2 = node2.left
        elif not node1 and not node2:
                node1 = wstack1.pop()
                node2 = wstack2.pop()
                if node1.val != node2.val:
                    return node1.val, node2.val
                node1 = node1.right
                node2 = node2.right
    else:
        if node1:
            return node1.val, None
        elif node2:
            return None, node2.val
        else:
            return None, None
                
    return None
            


if __name__ == '__main__':
    pre_list1 = [5, 4, 2, 4, 8, 6, 9]
    pre_list2 = [5, 3, 2, 4, 8, 7, 9]
    print(bst_mismatch(pre_list1, pre_list2))
    