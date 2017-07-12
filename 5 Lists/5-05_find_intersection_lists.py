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

def append_node(head, new_node):
    if not head: return
    
    node = head
    while node.next:
        node = node.next
    
    node.next = new_node

def find_intersection(head1, head2):
    if not head1 or not head2: return
    
    stack1 = []
    stack2 = []
    
    node = head1
    while node:
        stack1.append(node.val)
        node = node.next
    node = head2
    while node:
        stack2.append(node.val)
        node = node.next
    
    len1 = len(stack1)
    len2 = len(stack2)
    last_one = None
    while len1 and len2:
        if stack1[len1-1] == stack2[len2-1]:
            last_one = stack1[len1-1]
            len1 -= 1
            len2 -= 1
        else:
            return last_one
    if last_one:
        return last_one
    else:
        return None

# s1 = [1 2 6 7]
# s2 = [3 4 5 6 7]
# len1 = 4
# len2 = 5
# --
# l1:l2 = 4:5
# lo = 7
# 3:4
# lo = 6
# 2:3
#
        

if __name__ == '__main__':
    head1 = Node(1)
    head2 = Node(3)
    head3 = Node(6)
    append_val(head1, 2)
    append_val(head2, 4)
    append_val(head2, 5)
    append_val(head3, 7)
    append_node(head1, head3)
    append_node(head2, head3)

    print(find_intersection(head1, head2))
    
    
    