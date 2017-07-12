class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        
def append_val(head, val):
    if not head: return None
    node = head
    while node.next:
        node = node.next
    node.next = Node(val)
    
def print_list(head):
    node = head
    while node:
        print(node.val, end=" ")
        node = node.next
    print("")
    
def partition_list(head, X):
    if not head: return
    
    front_head = head
    back_head = None
    
    def add_back(new_node):
        nonlocal back_head
        if not back_head:
            back_head = new_node
        else:
            node = back_head
            while node.next:
                node = node.next
            node.next = new_node
            
    node = front_head
    prev = None
    while node:
        if node.val >= X: # move node to back_head
            if not prev: # node is at the head
                front_head = node.next
                node.next = None
                add_back(node)
                node = front_head
            else:
                temp_next = node.next
                node.next = None
                add_back(node)
                node = temp_next
                prev.next = node #########
        else:
            prev = node
            node = node.next
    
    if prev:    
        prev.next = back_head
    else:
        front_head = back_head
    
    return front_head
                
# 1 4 3 2 4 2
# f_h = 1
# b_h = 4 3 4
# --
# n = 1
#
# prev = 1
# n = 4
#  tn=3
# prev = 1
# n = 3
#  tn=2
# prev = 1
# n = 2
#
# prev = 2
# node = 4
#  tn = 2
# prev = 2
# n = 2
# prev = 2'
# n = none                 

if __name__ == '__main__':
    head = Node(1)
    append_val(head, 4)
    append_val(head, 3)
    append_val(head, 2)
    append_val(head, 5)
    append_val(head, 2)
    
    head = partition_list(head, 1)
    print_list(head)