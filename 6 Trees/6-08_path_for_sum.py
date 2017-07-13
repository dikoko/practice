class BTNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def build_from_list(inlist):
    if not inlist: return
    
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
    
    node = root
    wstack = []
    
    while node or wstack:
        if node:
            wstack.append(node)
            node = node.left
        else:
            node = wstack.pop()
            print(node.val, end=" ")
            node = node.right
    print("")
    
    
def find_all_ksum_path(root, K):
    
    # make a function that check all root to node sum
    # visit all node as roots
    
    def _find_all_root_paths(sub_root):
        # termination condition?
        node = sub_root
        wstack = []
        prev = "dummy"
        out_list = []
        
        while node or wstack:
            if node:
                if node.right == prev:
                    ## visit here
                    root_to_here = [n.val for n in wstack]
                    root_to_here.append(node.val)
                    out_list.append(root_to_here)
                    
                    prev = node
                    node = wstack.pop() if wstack else None
                elif node.left == prev:
                    wstack.append(node)
                    prev = node
                    node = node.right
                else:
                    wstack.append(node)
                    prev = node
                    node = node.left
            else:
                prev = None
                node = wstack.pop() if wstack else None
        
        return out_list
                
        
    def _find_path_sum(sub_root, k):
        node = sub_root
        wstack = []
        prev = "dummy"
        
        out_list = []
        while node or wstack:
            if node:
                if node.right == prev:
                    # visit here
                    root_to_here = [n.val for n in wstack]
                    root_to_here.append(node.val)
                    path_sum = sum(root_to_here)
                    if path_sum == k:
                        out_list.append(root_to_here)
                        
                    prev = node
                    node = wstack.pop() if wstack else None
                elif node.left == prev:
                    prev = node
                    wstack.append(node)
                    node = node.right
                else:
                    pre = node
                    wstack.append(node)
                    node = node.left
            else:
                prev = None
                node = wstack.pop() if wstack else None
        return out_list
        
    # 1st, we have to check each left, right has the path sum K
    
    out_list = []
    
    def _check_root_to_node_paths(sub_root, k):
        nonlocal out_list
        
        node = sub_root
        if not node: 
            return 
                
        _check_root_to_node_paths(node.left, k)
        out_list += _find_path_sum(node, k)
        _check_root_to_node_paths(node.right, k)
    
    def _check_root_over_node_paths(sub_root, k):
        nonlocal out_list
        node = sub_root
        if not node:
            return
        
        _check_root_over_node_paths(node.left, k)
        
        sub_paths = _find_all_root_paths(node.left)
        # print(sub_paths)
        for path in sub_paths:
            path.append(node.val)
            path_sum = sum(path)
            # print(path)
            right_sum_paths = _find_path_sum(node.right, k - path_sum)
            if right_sum_paths:
                for right_path in right_sum_paths:
                    right_path = path + right_path
                    out_list.append(right_path)
            
        _check_root_over_node_paths(node.right, k)
        
    
    _check_root_to_node_paths(root, K)
    
    _check_root_over_node_paths(root, K)
    
    return out_list            
        

if __name__ == '__main__':
    inlist = [8, 3, 13, 1, 5, 10, 17, None, None, 4, 7, None, 12, 15]
    root = build_from_list(inlist)
    print_inorder(root)
    
    print(find_all_ksum_path(root, 9))
    