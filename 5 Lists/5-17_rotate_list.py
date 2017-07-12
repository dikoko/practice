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

def rotate_list(head, K):
    # find k+1 th element from the last
    # make k th head and circular and k+1th cut
    
    # fist check the list size
    count = 0
    node = head
    
    while node:
        count += 1
        node = node.next
    if K > count:
        K = K % count
    
    if K == 0:
        return head
    
    slow = head
    fast = head
    for _ in range(K):
        if fast:
            fast = fast.next
        else:
            print('something wrong')
    if not fast: # K is the same as the size
        return head

# 1 2 3 4 5 k = 2
# s   f
#     s   f         
    while fast.next:
        fast = fast.next
        slow = slow.next
    
    new_head = slow.next
    fast.next = head
    slow.next = None
    
    return new_head
    
        
    

if __name__ == '__main__':
    head1 = Node(1)
    append_val(head1, 2)
    append_val(head1, 3)
    append_val(head1, 4)
    append_val(head1, 5)

    head2 = Node(68)
    append_val(head2, 86)
    append_val(head2, 36)
    append_val(head2, 16)
    append_val(head2, 5)
    append_val(head2, 75) # 68 -> 86 -> 36 -> 16 -> 5 -> 75
    
    head1 = rotate_list(head1, 6)
    print_list(head1)
    
    head2 = rotate_list(head2, 90)
    print_list(head2)    