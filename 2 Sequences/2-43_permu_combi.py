def permutation(instr):
	if not instr: return

	inlist = list(instr)

	def _permute(sublist):
		if len(sublist)==0: return [[]]

		out_list = []
		for i in range(len(sublist)):
			picked = sublist[i]
			sub_results = _permute(sublist[:i]+sublist[i+1:])
			for item in sub_results:
				item.append(picked)
			out_list += sub_results
		
		return out_list

	results = _permute(inlist)
	return ["".join(reversed(item)) for item in results]


def permutation_k(instr, K):
	if not instr: return
	if K > len(instr):
		print("invalid permutation K")
		return

	inlist = list(instr)

	def _permute(sublist, k):
		if k==0:
			return [[]]

		out_list = []
		for i in range(len(sublist)):
			picked = sublist[i]
			sub_results = _permute(sublist[:i]+sublist[i+1:],k-1)
			for item in sub_results:
				item.append(picked)
			out_list += sub_results
		return out_list

	results = _permute(inlist, K)
	return ["".join(reversed(item)) for item in results]


def repetive_permutation_k(instr, K):
	if not instr: return
	# note: K can be greater than len(instr)

	inlist = list(instr)
	
	def _rpermute(sublist, k):
		if k==0:
			return [[]]
		
		out_list = []
		for i in range(len(sublist)):
			picked = sublist[i]
			sub_results = _rpermute(sublist, k-1)
			for item in sub_results:
				item.append(picked)
			out_list += sub_results

		return out_list

	results = _rpermute(inlist, K)
	return ["".join(reversed(item)) for item in results]
		

def combination_k(instr, K):
	if not instr: return
	if K > len(instr):
		print('invalid combination K value')
		return
	if K == len(instr):
		return instr

	inlist = list(instr)
	
	def _combi(sublist, k):
		if k == 0:
			return [[]]
		if len(sublist)==0: # and it means k is not 0, it is impossible
			return [] # not [[]]

		picked = sublist[0]
		picked_results = _combi(sublist[1:], k-1)
		unpicked_results = _combi(sublist[1:], k)
		for item in picked_results:
			item.append(picked)
		
		return picked_results + unpicked_results
	
	results = _combi(inlist, K)
	return ["".join(reversed(item)) for item in results]


def repetive_combination_k(instr, K):
	if not instr: return
	if K < 0: return

	inlist = list(instr)

	def _rcombi(sublist, k):
		if k == 0:
			return [[]]
		if len(sublist)==0:
			return []
		
		picked = sublist[0]
		picked_results = _rcombi(sublist, k-1)
		unpicked_results = _rcombi(sublist[1:], k)
	
		for item in picked_results:
			item.append(picked)

		return picked_results + unpicked_results

	results = _rcombi(inlist,K)
	return ["".join(reversed(item)) for item in results]




if __name__ == '__main__':
	instr = 'abc'

	print(permutation(instr))
	print(permutation_k(instr, 2))
	print(repetive_permutation_k(instr,2))
	print(combination_k(instr, 2))
	print(repetive_combination_k(instr,2))