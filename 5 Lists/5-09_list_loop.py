# Given a linked list, return the node where the cycle begins.
# If there is no cycle, return null.
# Try solving it using constant additional space.
#
# Example :
# Input :
#                   ______
#                  |     |
#                  \/    |
#         1 -> 2 -> 3 -> 4
#
# Return the node corresponding to node 3.


class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
            
def print_list(head):
    node = head
    while node:
        print(node.val, end=" ")
        node = node.next
    print("")

    
def detect_cycle2(head): #######
    if not head: return
    
    # first, detect the cycle
    fast = head.next
    slow = head
    
    while fast and fast.next:
        if slow == fast:
            break
        slow = slow.next
        fast = fast.next.next
        
    if slow and fast and slow == fast: # loop detected!
        slow = head
        while slow != fast.next:
            slow = slow.next
            fast = fast.next
        return slow.val

    return None
    

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node3
    
    print(detect_cycle2(node1))
    