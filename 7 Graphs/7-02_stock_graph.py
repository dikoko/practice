# given a graph: example -> A company holds 10% of B company’s share,
# B company holds 5% of C company’s share, A company holds 2% of C company’s share,
# what percent of C company’s share does A company hold?

from collections import defaultdict

class Graph(object):
    def __init__(self, vertices, is_directed = True):
        self.vertices = vertices
        self.is_directed = is_directed
        self.edges = defaultdict(set)
        self.weights = defaultdict(int)
    
    def add_edge(self, u, v, w):
        self.edges[u].add(v)
        self.weights[(u,v)] = w
        if not self.is_directed:
            self.edges[v].add(u)
            self.weights[(v,u)] = w

def find_all_paths(graph, src, dst):
    if not graph: return
    
    _visited = defaultdict(bool)
    
    def _find_paths(u, v):
        if u == v: # this is the path
            return [[v]]
        
        _visited[u] = True
        
        neighbors = graph.edges[u]
        out_list = []
        for node in neighbors:
            if not _visited[node]:
                sub_paths = _find_paths(node, v)
                for item in sub_paths:
                    item.append(u)
                out_list += sub_paths
        
        return out_list
    
    return [[node for node in reversed(path)] for path in _find_paths(src, dst)]
    
def calc_share(graph, holder, holdee):
    if not graph: return 
    
    connection_list = find_all_paths(graph, holder, holdee)
    total_share = 0
    for connection in connection_list:
        ratio = 1
        for i in range(len(connection)-1):
            ratio *= (graph.weights[(connection[i], connection[i+1])]/100)
        total_share += ratio
        
    return total_share
            
# 0.02
# 0.1*0.05 = 0.005
        

if __name__ == '__main__':
    g = Graph(['A', 'B', 'C'])
    g.add_edge('A', 'B', 10)
    g.add_edge('B', 'C', 5)
    g.add_edge('A', 'C', 2)
    
    print(calc_share(g, 'A', 'C'))
    
    