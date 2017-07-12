# Given Nodes such as
# M → N → T → D → E
# |   |   |   |
# C   X   Y   L
# |   |
# A   Z
#
# -> right pointer
# | down pointer
# Output should be
# M->C->A->N->X->Z->T->Y->D-L>E
#
# Write this to flatten
# def flatten(head):
#
# class Node(object):
# right;
# down;
# char a;

class Node(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.down = None
        
def append_down_val(head, val):
    if not head: return 
    
    node = head
    while node.down:
        node = node.down
    node.down = Node(val)

def append_right_node(head, new_node):
    if not head: return
    
    node = head
    while node.right:
        node = node.right
    node.right = new_node
    
def print_right(head):
    if not head: return
    node = head
    while node:
        print(node.val, end=" ")
        node = node.right
    print("")
    
def flatten(head):
    if not head: return
    
    def _flatten_down(node):
        while node.down:
            node.right = node.down
            node.down = None
            node = node.right
        return node # the last node of flatten
    
    node = head    
    while node:
        temp_right = node.right
        flatten_last = _flatten_down(node)
        flatten_last.right = temp_right
        node = temp_right

    return head
    
    
if __name__ == '__main__':
    head = Node('M')
    append_down_val(head, 'C')
    append_down_val(head, 'A')
    head2 = Node('N')
    append_down_val(head2, 'X')
    append_down_val(head2, 'Z')
    head3 = Node('T')
    append_down_val(head3, 'Y')
    head4 = Node('D')
    append_down_val(head4, 'L')    
    head5 = Node('E')
    append_right_node(head, head2)
    append_right_node(head, head3)
    append_right_node(head, head4)
    append_right_node(head, head5)

    flatten(head)
    print_right(head)
    
    
