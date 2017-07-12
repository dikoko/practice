class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
        
def append_val(head,val):
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

def scoped_reverse(head, m, n):
    
    scope_before = None
    scope_after = None
        
    node = head
    count = 1
    while node:
        if count == m-1:
            scope_before = node
        if count == n:
            scope_after = node.next
            node.next = None
            break
        node = node.next
        count += 1  ########
        
    if m == 1:
        scope_before = None # before head
    
    if scope_before:
        s_head = scope_before.next
    else:
        s_head = head
    
    node = s_head
    prev = None
    while node:
        temp_next = node.next
        node.next = prev
        prev = node
        node = temp_next
        
    s_head.next = scope_after
    
    s_head = prev
    if scope_before:
        scope_before.next = s_head
    else:
        head = s_head
    
    return head
        
            

if __name__ == '__main__':
    head = Node(1)
    append_val(head,2)
    append_val(head,3)
    append_val(head,4)
    append_val(head,5)
    
    head = scoped_reverse(head, 2, 4)
    
    print_list(head)
    