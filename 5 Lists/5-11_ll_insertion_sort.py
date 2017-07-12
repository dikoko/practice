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

def insertion_sort(head):
    if not head: return
    
    s_head = head # sorted head
    u_head = head.next # unsorted head
    s_head.next = None
    
    while u_head:
        next_item = u_head
        u_head = u_head.next
        next_item.next = None

        node = s_head
        if node.val > next_item.val: # new head
            next_item.next = s_head
            s_head = next_item
            continue
            
        while node.next and node.next.val < next_item.val:
            node = node.next
        # last or node.next.val >= next_item.val
        temp_next = node.next
        node.next = next_item
        node.next.next = temp_next
    
    return s_head

        

if __name__ == '__main__':
    head = Node(2)
    append_val(head, 3)
    append_val(head, 1)
    append_val(head, 5)
    append_val(head, 4)
    append_val(head, 7)
    
    head = insertion_sort(head)
    print_list(head)
    
    