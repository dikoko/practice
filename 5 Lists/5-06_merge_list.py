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

def merge_list(list1, list2):
    if not list1 and not list2: return None

    head1 = list1
    head2 = list2
    
    mhead = None
    while head1 and head2:
        picked = None
        if head1.val < head2.val: # pick 1
            picked = head1
            head1 = head1.next
        else:
            picked = head2
            head2 = head2.next
            
        picked.next = None
        if not mhead: # the first node
            mhead = picked
        else:
            node = mhead
            while node.next:
                node = node.next
            node.next = picked
    
    node = mhead
    while node.next:
        node = node.next

    if head1: # append head1
        node.next = head1
    elif head2:
        node.next = head2
        
    return mhead
    
    

if __name__ == '__main__':
    head1 = Node(5)
    append_val(head1, 10)
    append_val(head1, 15)
    append_val(head1, 30)
    
    head2 = Node(2)
    append_val(head2, 3)
    append_val(head2, 20)
    
    print_list(head1)
    print_list(head2)
    
    mhead = merge_list(head1, head2)
    print_list(mhead)
    