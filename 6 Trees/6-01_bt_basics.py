class BTNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
            
def print_postorder(root):
    if not root: return
    
    wstack = []
    node = root
    prev = 'dummy'
    while node or wstack:
        if node:
            if node.right == prev:
                print(node.val, end=" ")
                prev = node
                node = wstack.pop() if wstack else None
            elif node.left == prev:
                # going right
                prev = node
                wstack.append(node)
                node = node.right
            else:
                # going left
                prev = node
                wstack.append(node)
                node = node.left
        else:
            prev = None
            node = wstack.pop()
    print("")
    
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
    
def print_levelorder(root):
    if not root: return
    node = root
    wqueue = [root, None]
    while node or wqueue:
        node = wqueue.pop(0)
        if node:
            print(node.val, end=" ")
            if node.left: wqueue.append(node.left)
            if node.right: wqueue.append(node.right)
        elif wqueue: # new level if the queue is not empty
            print("")
            wqueue.append(None)
    print("")


                

if __name__ == '__main__':
    inlist = [3, 9, 20, None, None, 15, 7]
    root = build_from_list(inlist)
    print_preorder(root)
    print_inorder(root)
    print_postorder(root)
    print_levelorder(root)















    