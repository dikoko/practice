class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def append_val(head,val):
    if not head: return
    node = head
    while node.next:
        node = node.next
    node.next = Node(val)

def print_list(head):
    if not head: return
    node = head
    while node:
        print(node.val, end=" ")
        node = node.next
    print("")
    
def reverse_iter(head):
    if not head: return
    
    node = head
    prev = None
    while node:
        temp_next = node.next
        node.next = prev
        prev = node
        node = temp_next
        
    return prev
    
    
def reverse_recur(head):
    if not head: return 
    
    def _reverse(node):
        if not node.next: return node ######
        
        temp_next = node.next
        node.next = None
        r_head = _reverse(temp_next)
        temp_next.next = node
        return r_head
        
    return _reverse(head)
        
    


if __name__ == '__main__':
    head1 = Node(1)
    append_val(head1, 2)
    append_val(head1, 3)
    append_val(head1, 4)
    append_val(head1, 5)
    head2 = Node(1)
    append_val(head2, 2)
    append_val(head2, 3)
    append_val(head2, 4)
    append_val(head2, 5)
    
    head_r1 = reverse_iter(head1)
    print_list(head_r1)
    head_r2 = reverse_recur(head2)
    print_list(head_r2)
    
    
    