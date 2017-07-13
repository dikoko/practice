
class BTNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def restore(inlist):
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
    
def store(root):
    if not root: return 
    
    wqueue = [root]
    
    out_list = []
    while wqueue:
        node = wqueue.pop(0)
        if node:
            out_list.append(node.val)
        else:
            out_list.append(None)
        
        if node:
            wqueue.append(node.left)
            wqueue.append(node.right)
    
    j = len(out_list)-1
    while out_list[j] == None:
        j -= 1
    
    return out_list[:j+1]
            

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

def print_preorder(root):    
    wstack = []
    node = root
    
    while node or wstack:
        if node:
            print(node.val, end=" ")
            wstack.append(node.right)
            node = node.left
        else:
            node = wstack.pop()
    print("")
    
def print_postorder(root):
    wstack = []
    node = root
    prev = "dummy"
    
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
    inlist2 = [8, 3, 13, 1, 5, 10, 17, None, None, 4, 7, None, 12, 15]
    
    root2 = restore(inlist2)
    print_inorder(root2)
    print_levelorder(root2)
    
    inlist3 = store(root2)
    print(inlist3)
    
    print_preorder(root2)
    print_postorder(root2)
    