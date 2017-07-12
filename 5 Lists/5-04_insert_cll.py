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
        if node == head:
            break
    print("")

def insert_circular_list(head, val):
    if not head: 
        new_head = Node(val)
        new_head.next = new_head
        return new_head
    
    if head and head.val > val: # new head
        node = head
        while node.next != head: ####
            node = node.next
        new_head = Node(val)
        node.next = new_head
        new_head.next = head
        return new_head
        
    node = head
    while node.next != head and node.next.val < val:
        node = node.next
        
    if node.next != head: # usual insert
        temp_next = node.next
        node.next = Node(val)
        node.next.next = temp_next
    else: # node.next == head, the last one
        node.next = Node(val)
        node.next.next = head
        
    return head
        
        
    
        

if __name__ == '__main__':
    head = insert_circular_list(None, 2)
    head = insert_circular_list(head, 1)
    print_list(head)
    head = insert_circular_list(head, 4)
    head = insert_circular_list(head, 6)
    head = insert_circular_list(head, 8)
    print_list(head)
    head = insert_circular_list(head, 3)
    print_list(head)
    head = insert_circular_list(head, 9)
    print_list(head)
    

