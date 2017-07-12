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

def remove_dupl2(head):
    new_head = None
    new_tail = None
    prev = head
    node = head.next
    is_repeat = False
    while node:
        if node.val != prev.val: # move prev to the new_head
            if not is_repeat:
                prev.next = None
                if not new_head:
                    new_head = prev
                    new_tail = new_head
                else:
                    new_tail.next = prev
                    new_tail = prev
            else:
                is_repeat = False
        else:
            is_repeat = True

        prev = node
        node = node.next
    
    if not is_repeat: # move the prev to the new_head
        prev.next = None
        if not new_head:
            new_head = prev
        else:
            new_tail.next = prev
    
    return new_head
# [2
#
# 1 1' 1'' 2 3
# prev = 1
# n = 1'
# is_r = T
# p = 1'
# n = 1''
# -
# is_r = F
# p = 2
# n = 3

        


if __name__ == '__main__':
    head1 = Node(1)
    append_val(head1, 2)
    append_val(head1, 3)
    append_val(head1, 3)
    append_val(head1, 4)
    append_val(head1, 4)
    append_val(head1, 5)

    head2 = Node(1)
    append_val(head2, 1)
    append_val(head2, 1)
    append_val(head2, 2)
    append_val(head2, 3)
    
    head1 = remove_dupl2(head1)
    print_list(head1)
    head2 = remove_dupl2(head2)
    print_list(head2)
    