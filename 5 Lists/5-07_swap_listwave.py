# Given a singly linked list: 1->2->3->4->5
# Change it to 1->5->2->4->3 using O(1) space

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        
def append_val(head, val):
    if not head: return
    
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

def swap_wave(head):
    if not head: return
    if not head.next or not head.next.next: return head
    
    node = head
    
    while node and node.next and node.next.next:
        # find the last
        tail_before = node
        while tail_before.next and tail_before.next.next:
            tail_before = tail_before.next
        
        temp_next = node.next
        node.next = tail_before.next # tail
        tail_before.next = None
        node.next.next = temp_next
        node = temp_next
    
    return head


if __name__ == '__main__':
    head = Node(1)
    append_val(head, 2)
    append_val(head, 3)
    append_val(head, 4)
    append_val(head, 5)
    
    print_list(head)
    head = swap_wave(head)
    print_list(head)
    