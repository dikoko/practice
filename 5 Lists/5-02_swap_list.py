# Before: A->B->C->D
# After: B->A->D->C

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
    if not head: return
    node = head
    while node:
        print(node.val, end=" ")
        node = node.next
    print("")


def swap_pair_recur(head):
    if not head: return
    
    def _swap(node):
        if not node: return ######
        
        temp_next = node.next
        node.next = _swap(temp_next.next)
        temp_next.next = node
        return temp_next
    
    return _swap(head)


if __name__ == '__main__':
    head2 = Node('A')
    append_val(head2, 'B')
    append_val(head2, 'C')
    append_val(head2, 'D')
    
    head_s2 = swap_pair_recur(head2)
    print_list(head_s2)
    