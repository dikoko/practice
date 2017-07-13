class BTNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
        
def build_from_orders(in_list, pre_list):
    len_i = len(in_list)
    len_p = len(pre_list)
    
    def _build(low, high, pindex):
        if low > high: 
            return None
            
        sub_root = BTNode(pre_list[pindex])
        for i in range(low, high+1):
            if in_list[i] == sub_root.val:
                break
        
        sub_root.left = _build(low, i-1, pindex+1)
        sub_root.right = _build(i+1, high, pindex+(i-low+1))
        
        return sub_root
    
    return _build(0, len_i-1, 0)
        
#     0   1   2   3   4   5
# i:['D','B','E','A','F','C']
# p:['A','B','D','E','C','F']
#
# _b(0, 5, 0)
# sr = 'A'
# i = 3
# sr.left = _b(0, 2, 1) 'B'->
# sr.r = _b(4, 5, 4)
# --
# _b(0,2,1)
# sr = 'B'
# i = 1
# sr.l = _b(0, 0, 2) 'D'
# sr.r = _b(2, 2, 3) 'E'
# --
# _b(0,0,2)
# sr = 'D'
# i = 0
# sr.l = _b(0,-1 --> None
# sr.r = _b(1,0 --> None
# --
# _b(2,2,3)
# sr = 'E'
# i = 2
# sr.l = _b(2,1 -->
# --
# _b(4,5,4)
# sr = 'C'
# i = 5
# sr.l = _b(4,4, 5) 'F'
# sr.r = _b(6,5,4+1+1) N

def print_levelorder(root):
    if not root: 
        return
        
    wqueue = [root, None]
    while wqueue:
        node = wqueue.pop(0)
        if node:
            print(node.val, end=" ")
            if node.left: 
                wqueue.append(node.left)
            if node.right: 
                wqueue.append(node.right)
        else: # new level
            if wqueue: # more to go
                wqueue.append(None)
            print("")
    print("")
    
def print_preorder(root):
    if not root:
        return
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

def print_postorder(root):
    if not root: return
    node = root
    wstack = []
    prev = 'dummy'
    while node or wstack:
        if node:
            if node.right == prev:
                print(node.val, end=" ")
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
    print("")
                


if __name__ == '__main__':
    in_list = ['D','B','E','A','F','C']
    pre_list = ['A','B','D','E','C','F']
    
    root = build_from_orders(in_list, pre_list)
    
    print_levelorder(root)
    print_preorder(root)
    print_inorder(root)
    print_postorder(root)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    