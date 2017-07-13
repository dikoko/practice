# convert a ternary expression into a Binary tree structure.
#
#     a?b:c 
#       a
#      / \
#     b   c
#
#  a?b?c:d:e
#     a
#    / \
#   b   e
#  / \
# c   d
#try to do it in o(n) time complexity, n is the size of the string

class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def print_level(root):
	if not root: return
	
	wqueue = [root, None]
	while len(wqueue) > 0:
		node = wqueue.pop(0)
		if node:
			if node:
				print(node.val, end=" ")
				if node.left: 
					wqueue.append(node.left)
				if node.right:
					wqueue.append(node.right)
		else: # means the new level
			if len(wqueue) > 0:
				wqueue.append(None)
			print("")

def build(strexp):
	if not strexp: return

	node_stack = []
	leaf_stack = []
	is_second = False

	s = list(strexp)
	s.append(':') # to make the process consistent at the end
	
	index = 0
	buffer = ''
	while index < len(s):
		if s[index] == '?':
			new_node = TreeNode(buffer)
			node_stack.append(new_node)
		elif s[index] == ':':
			if is_second: # build a tree
				node = node_stack.pop()
				node.right = TreeNode(buffer)
				node.left = leaf_stack.pop() 
				leaf_stack.append(node)
			else:
				new_node = TreeNode(buffer)
				leaf_stack.append(new_node)
			is_second = not is_second
		else: # it is a character
			buffer = s[index]
		index += 1	

	# clean up the residuals 
	while len(node_stack) > 0:
		node = node_stack.pop()
		node.right = leaf_stack.pop()
		node.left = leaf_stack.pop()
		leaf_stack.append(node)

	return leaf_stack[0]	

if __name__ == '__main__':
	str1 = "a?b:c"
	str2 = "a?b?c:d:e"
	str3 = "a?b?c:d:e?f:g"
	root = build(str1)
	print_level(root)
	print("--")
	root = build(str2)
	print_level(root)
	print("--")
	root = build(str3)
	print_level(root)



