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

def print_reverse_recur(head):
    if not head: return
    
    def _rprint(node):
        if not node: return
        _rprint(node.next)
        print(node.val, end=" ")
    _rprint(head)
    print("")

def print_reverse_iter_nm(head):
    if not head: return
    
    node = head
    wstack = []
    while node:
        wstack.append(node.val)
        node = node.next
    
    for _ in range(len(wstack)):
        print(wstack.pop(), end=" ")
    print("")
        
    
    
def print_reverse_n2t_cm(head):
    last = None
    while last != head:
        node = head
        while node.next != last:
            node = node.next
        print(node.val, end=" ")
        last = node
    print("")

def print_reverse_nt_cm(head):  
    prev = None
    node = head
    while node:
        temp_next = node.next
        node.next = prev
        prev = node
        node = temp_next
    node = prev
    while node:
        print(node.val, end=" ")
        node = node.next
    print("")
    
    
if __name__ == '__main__':
    head = Node('A')
    append_val(head, 'B')
    append_val(head, 'C')
    
    print_list(head)
    print_reverse_recur(head)
    print_reverse_iter_nm(head)
    print_reverse_n2t_cm(head)
    print_reverse_nt_cm(head)