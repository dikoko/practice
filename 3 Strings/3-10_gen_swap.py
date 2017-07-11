# GIven a string "str" and pair of "N" swapping indices, generate a lexicographically largest string.
# Swapping indices can be reused any number times.
# e.g. 1)
# String = "abdc"
# Indices:
# (1,4)
# (3,4)
# Answer:
# cdba, cbad, dbac,dbca
# ​you should print only "dbca" which is lexicographically largest.

from collections import defaultdict
def gen_by_swapping(instr, indices):
    
    len_s = len(instr)
    len_i = len(indices)
    
    _edges = defaultdict(set)
    for u, v in indices:
        _edges[u].add(v)
        _edges[v].add(u)
    
    nodes = [i+1 for i in range(len_s)] # the index is 1 based
    # find connected sets
    connected_sets = [] # results will be [[]]
    while nodes:
        picked = nodes[0]
        wstack = [picked]
        group = []
        _visited = defaultdict(bool)
        while wstack:
            node = wstack.pop()
            if not _visited[node]:
                _visited[node] = True
                group.append(node)
                nodes.remove(node)
                for nbr in _edges[node]:
                    if not _visited[nbr]:
                        wstack.append(nbr)
        connected_sets.append(group)
    
    connected_sets = list(map(sorted, connected_sets)) ######

    out_list = ['0']*len_s
    for connects in connected_sets:
        # get the characters of the index
        chars = [instr[i-1] for i in connects]
        chars.sort(reverse=True)
        for i in range(len(chars)):
            out_list[connects[i]-1] = chars[i]
            
    return "".join(out_list)
    
            
if __name__ == '__main__':
    instr = 'abdc'
    indices = [(1,4), (3,4)] # "dbca"
    
    print(gen_by_swapping(instr, indices))