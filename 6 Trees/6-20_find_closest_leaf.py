#               A
#             /    \
#            B       C
#                  /   \
#                 E     F
#                /       \
#               G         H
#              / \       /
#             I   J     K
#
# Closest leaf to 'H' is 'K', so distance is 1 for 'H'
# Closest leaf to 'C' is 'B', so distance is 2 for 'C'
# Closest leaf to 'E' is either 'I' or 'J', so distance is 2 for 'E'
# Closest leaf to 'B' is 'B' itself, so distance is 0 for 'B'

# 1. find c -> get root to c path also
# 2. root as c, find the shortest distance leaf
#    # return the leaf node and distance
# 3. reverse the root to c path, -= 1 distances,
#    # find the min distance leaft as for each ancestors

import math

class BTNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def build_from_list(inlist):
    if not inlist: return
    
    len_in = len(inlist)
    
    root = BTNode(inlist.pop(0))
    wqueue = [root]
    
    while inlist:
        node = wqueue.pop(0)
        node_val = inlist.pop(0)
        if node_val:
            node.left = BTNode(node_val)
            wqueue.append(node.left)
        if inlist:
            node_val = inlist.pop(0)
            if node_val:
                node.right = BTNode(node_val)
                wqueue.append(node.right)
    return root
    

def print_inorder(root):
    if not root: return
    
    def _printi(node):
        if not node: return
        _printi(node.left)
        print(node.val, end=" ")
        _printi(node.right)
    _printi(root)
    print("")
    
def find_closest_leaf_under(root):
    if not root: return
    
    def _find_cl(node):
        if not node.left and not node.right: # a leaf
            return 0, node.val
        
        left_dist = math.inf
        right_dist = math.inf
        
        if node.left:
            left_dist, left_leaf = _find_cl(node.left)
        if node.right:
            right_dist, right_leaf = _find_cl(node.right)
        
        if left_dist < right_dist:
            return left_dist+1, left_leaf
        else:
            return right_dist+1, right_leaf
            
    return _find_cl(root)
    
def find_closest_leaf(root, node_key):
    if not root: return
    
    node = root
    wstack = [root]
    prev = 'dummy'
    min_dist = math.inf
    min_leaf = None
    while node or wstack:
        if node:
            if node.right == prev:
                # visit here..
                if node.val == node_key:
                    # 1. first, find the min-dist leaf of under this node
                    min_dist, min_leaf = find_closest_leaf_under(node)
                    # 2. get ancestors path
                    ancestors = wstack[:]
                    i = 1 # distance to the ancestor
                    for item in reversed(ancestors):
                        temp_min_dist, temp_min_leaf = find_closest_leaf_under(item)
                        if temp_min_dist + i < min_dist: # new min dist
                            min_dist = temp_min_dist+i
                            min_leaf = temp_min_leaf
                        i += 1
                    break
                prev = node
                node = wstack.pop() if wstack else None
            elif node.left == prev:
                prev = node
                wstack.append(node)
                node = node.right
            else:
                prev = node
                wstack.append(node)
                node = node.left
        else:
            prev = None
            node = wstack.pop() if wstack else None
    
    return min_dist, min_leaf

if __name__ == '__main__':
    inlist = ['A', 'B', 'C', None, None, 'E', 'F', 'G', None, None, 'H', 'I', 'J', 'K']
    root = build_from_list(inlist)
    print_inorder(root)
    print(find_closest_leaf(root, 'H'))    
    print(find_closest_leaf(root, 'C'))
    print(find_closest_leaf(root, 'E'))
    print(find_closest_leaf(root, 'B'))    