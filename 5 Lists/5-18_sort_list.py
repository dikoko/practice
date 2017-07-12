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

def sort_list(head):
    
    def _sortl(head):
        if not head: return None, None
        if not head.next: return head, head
        
        left_head = None
        left_tail = None
        right_head = None
        right_tail = None
        
        pivot = head
        node = head.next
        while node:
            if node.val >= pivot.val:
                if not right_head:
                    right_head = node
                    right_tail = node
                else:
                    right_tail.next = node
                    right_tail = node
            else:
                if not left_head:
                    left_head = node
                    left_tail = node
                else:
                    left_tail.next = node
                    left_tail = node
            temp_next = node.next
            node.next = None
            node = temp_next
        
        ls_head, ls_tail = _sortl(left_head)
        rs_head, rs_tail = _sortl(right_head)
        
        if ls_tail:
            ls_tail.next = pivot
        else: # pivot should be the head
            ls_head = pivot
        pivot.next = rs_head
        
        if not rs_tail: # pivot should be the tail
            rs_tail = pivot
        
        return ls_head, rs_tail

    shead, _ = _sortl(head)
    return shead

if __name__ == '__main__':
    head1 = Node(1)
    append_val(head1, 5)
    append_val(head1, 4)
    append_val(head1, 3)
    append_val(head1, 2)

    head1 = sort_list(head1)
    print_list(head1)

