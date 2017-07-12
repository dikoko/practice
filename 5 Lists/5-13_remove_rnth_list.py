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

def remove_nth_last(head, N):
    if not head: return 
    
    fast = head
    slow = head
    
    for _ in range(N):
        if fast:
            fast = fast.next
        else: #N is larger than the list size
            fast = head.next
            head.next = None
            return fast
    else:
        if not fast:  ########## N and list size is same
            fast = head.next
            head.next = None
            return fast
    
    while fast.next:
        fast = fast.next
        slow = slow.next
    # slow.next is target to remove
    temp_next = slow.next.next
    slow.next.next = None
    slow.next = temp_next
    
    return head

if __name__ == '__main__':
    head = Node(1)
    append_val(head, 1)
    append_val(head, 3)
    append_val(head, 4)
    append_val(head, 5)

    head = remove_nth_last(head, 5)
    print_list(head)