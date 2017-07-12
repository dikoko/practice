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
    
def remove_dupl_list(head):
    
    prev = head
    node = head.next
    
    while node:
        if node.val == prev.val: # remove the node
            prev.next = node.next
            node.next = None
            node = prev.next
        else:
            prev = node
            node = node.next
    
    return head
    
# 1 1' 2
# p = 1
# n = 1'
#
# n = 2
# p = 2
# n = None
#


if __name__ == '__main__':
    head1 = Node(1)
    append_val(head1, 1)
    append_val(head1, 2)

    head2 = Node(1)
    append_val(head2, 1)
    append_val(head2, 2)
    append_val(head2, 3)
    append_val(head2, 3)

    
    head1 = remove_dupl_list(head1)
    head2 = remove_dupl_list(head2)
    print_list(head1)
    print_list(head2)