# A person is a famous person if he doesn't know anyone in the list 
# and everyone else in the list should know this person. 
# The function isKnow(i,j) => true/ false is given to us. No need to worry about it. 
# Goal is to find the famous person in O(n) complexity.

from collections import defaultdict

class Candidates(object):
	def __init__(self, names):
		self.names = names
		self.nums = len(names)
		self.knows = defaultdict(set)
	
	def set_know(self, i, js):
		for j in js:
			self.knows[i].add(j)

	def is_know(self, i, j):
		if j in self.knows[i]:
			return True
		else:
			return False

def find_famous_bf(candidates):

	nums = candidates.nums
	knows = [0]*nums

	for i in range(nums):
		for j in range(nums):
			if i != j:
				if candidates.is_know(i, j):
					knows[j] += 1
					knows[i] -= 1

	for i in range(nums):
		if knows[i] == nums -1:
			return candidates.names[i]

	return "???"

def find_famous_smart(candidates):
	nums = candidates.nums

	if nums == 1:
		return candidates.names[0]

	# nums >= 2
	candidate = 0
	for i in range(1, nums):
		if not candidates.is_know(i, candidate):
			candidate = i

	return candidates.names[candidate]
							


if __name__ == '__main__':
	names = ['Carl', 'Jane', 'Lucy', 'May', 'Peter', 'Diko', 'Jane', 'Blin']
	c = Candidates(names)
	c.set_know(0,[1,2,5])
	c.set_know(1,[5,7])
	c.set_know(2,[3,4,5])
	c.set_know(3,[4,5,6,7])
	c.set_know(4,[2,5])
	c.set_know(5,[])
	c.set_know(6,[5,7])
	c.set_know(7,[3,5])

	print(find_famous_bf(c))
	print(find_famous_smart(c))


	
