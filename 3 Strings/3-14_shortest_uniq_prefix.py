# Find shortest unique prefix to represent each word in the list.
#
# e.g.
# Input: ['zebra', 'dog', 'duck', 'dove']
# Output: {z, dog, du, dov}
# where we can see that
# zebra = z
# dog = dog
# duck = du
# dove = dov

def build_trie(inlist):
    
    root = [0, {}]

    for term in inlist:
        node = root
        node[0] += 1
        for c in term:
            if c not in node[1]:
                node[1][c] = [0,{}]
            node = node[1][c]
            node[0] += 1
    return root
    
def shortest_prefix(inlist):
    
    root = build_trie(inlist)
    out_list = []
    
    for term in inlist:
        node = root
        prefix = ''
        for c in term:
            node = node[1][c]
            prefix += c
            if node[0] == 1:
                out_list.append(prefix)
                break
        else:
            out_list.append(prefix)
    return out_list
        

if __name__ == '__main__':
    inlist = ['zebra', 'dog', 'duck', 'dove']
    
    print(shortest_prefix(inlist))