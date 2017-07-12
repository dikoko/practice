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
    
def add_in_list(l1, l2):
    
    node1 = l1
    node2 = l2
    
    head = None
    tail = None
    overf = 0
    while node1 or node2:
        val = overf
        if node1:
            val += node1.val
        if node2:
            val += node2.val
            
        overf = val // 10
        digit = val % 10
        new_node = Node(digit)        
        if not head:
            head = new_node
            tail = head
        else:
            tail.next = new_node
            tail = tail.next
        
        if node1:
            node1 = node1.next
        if node2:
            node2 = node2.next

    if overf > 0:
        new_node = Node(overf)
        if not head:
            head = new_node
            tail = head
        else:
            tail.next = new_node
            tail = tail.next
        
    return head
    
# 2 4 3
# 5 6 4
# h = [7 0 8
# n1 =2
# n2 =5
# val = 7 : 0 / 7
# new = 7
# --
# n1 = 4
# n2 = 6
# val = 10 : 1 / 0
# new = 0
# --
# of = 1
# n1 = 3
# n2 = 4
# val = 8 : 0 / 8
     
    
    

if __name__ == '__main__':
    head1 = Node(2)
    append_val(head1, 4)
    append_val(head1, 3)

    head2 = Node(5)
    append_val(head2, 6)
    # append_val(head2, 4)
    
    head = add_in_list(head1, head2)
    print_list(head)