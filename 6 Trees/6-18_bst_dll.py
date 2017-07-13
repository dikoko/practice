
class BTNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Node(object):
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None
        
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

def print_list(head):
    node = head
    while node:
        val = node.val
        if node.prev:
            prev_val = node.prev.val
        else:
            prev_val = 0
        print("%d(%d)-" % (val, prev_val), end=" ")
        node = node.next
    print("")
    
def bst_to_dll(root):
    if not root: return
    
    node = root
    wstack = []
    head = None
    tail = None
    
    while node or wstack:
        if node:
            wstack.append(node)
            node = node.left
        else:
            node = wstack.pop()
            new_node = Node(node.val)
            if not head:
                head = new_node
                tail = head
            else:
                tail.next = new_node
                new_node.prev = tail
                tail = new_node
            node = node.right
    
    return head
    
    


if __name__ == '__main__':
    vals = [8, 3, 13, 1, 5, 10, 17, None, None, 4, 7, None, 12, 15]
    root = build_from_list(vals)
    print_inorder(root)
    head = bst_to_dll(root)
    print_list(head)