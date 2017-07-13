from collections import defaultdict
import math

class Graph(object):
    def __init__(self, nodes, is_directed=True):
        self.is_directed = is_directed
        self.nodes = nodes
        self.edges = defaultdict(set)
        self.weights = defaultdict(int)
    
    def add_edge(self, u, v, w=1):
        self.edges[u].add(v)
        self.weights[(u,v)] = w
        if not self.is_directed:
            self.edges[v].add(u)
            self.weights[(v,u)] = w
        

def dfs_iter(graph, start):
    
    _visited = defaultdict(bool)
    wstack = [start]
    out_list = []
    while wstack:
        node = wstack.pop()
        if not _visited[node]:
            _visited[node] = True
            out_list.append(node)
            for nbr in graph.edges[node]:
                if not _visited[nbr]:
                    wstack.append(nbr)
    return out_list
    

def dfs_recur(graph, start):
    _visited = defaultdict(bool)
    out_list = []
    
    def _dfs_visit(v):
        if not _visited[v]:
            _visited[v] = True
            out_list.append(v)
            for nbr in graph.edges[v]:
                if not _visited[nbr]:
                    _dfs_visit(nbr)
    _dfs_visit(start)
    
    return out_list


def bfs(graph, start):
    _visited = defaultdict(bool)
    out_list = []
    
    wqueue = [start]
    while wqueue:
        node = wqueue.pop(0)
        if not _visited[node]:
            _visited[node] = True
            out_list.append(node)
            for nbr in graph.edges[node]:
                if not _visited[nbr] and nbr not in wqueue:
                    wqueue.append(nbr)
    return out_list
    

def all_paths(graph, src, dest):
    
    out_list = []
    path = []
    _visited = defaultdict(bool)
    def _dfs_visit(u, v):
        
        _visited[u] = True
        path.append(u)
        
        if u == v:
            out_list.append(path[:])
        
        for nbr in graph.edges[u]:
            if not _visited[nbr]:
                _dfs_visit(nbr, v)
        
        path.pop()
        _visited[u] = False
    
    _dfs_visit(src,dest)
    
    return out_list
    

def dijkstra(graph, src, dest):
    
    _costs = defaultdict(lambda: math.inf)
    _processed = set()
    _prevs = defaultdict(lambda: None)
    
    def get_next_node():
        min_cost = math.inf
        min_node = None
        for node in graph.nodes:
            if node not in _processed and _costs[node] < min_cost:
                min_cost = _costs[node]
                min_node = node
        return min_node
    
    _costs[src] = 0
    node = src
    while node:
        for nbr in graph.edges[node]:
            new_cost = _costs[node] + graph.weights[(node,nbr)]
            if new_cost < _costs[nbr]:
                _costs[nbr] = new_cost
                _prevs[nbr] = node
        _processed.add(node)
        node = get_next_node()
    
    path = []
    node = dest
    while node:
        path.append(node)
        node = _prevs[node]
    
    return _costs[dest], list(reversed(path))
                

def connected(graph):
    
    connecteds = []
    
    nodes = graph.nodes[:]
    
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
                for nbr in graph.edges[node]:
                    if not _visited[nbr]:
                        wstack.append(nbr)
        connecteds.append(group)
    
    return connecteds
        



if __name__ == '__main__':
    g = Graph(['A', 'B', 'C', 'D', 'E', 'F'])
    g.add_edge('A', 'B', 5)
    g.add_edge('A', 'C', 2)
    g.add_edge('C', 'B', 8)
    g.add_edge('B', 'D', 4)
    g.add_edge('B', 'E', 2)
    g.add_edge('C', 'E', 7)
    g.add_edge('D', 'E', 6)
    g.add_edge('D', 'F', 3)
    g.add_edge('E', 'F', 1)

    g2 = Graph(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], False)
    g2.add_edge('A', 'B')
    g2.add_edge('B', 'F')
    g2.add_edge('B', 'E')
    g2.add_edge('E', 'F')
    g2.add_edge('C', 'D')
    g2.add_edge('G', 'H')
    
    print(dfs_iter(g, 'A'))
    print(dfs_recur(g, 'A'))
    print(bfs(g, 'A'))
    print(all_paths(g, 'A', 'F'))
    print(dijkstra(g, 'A', 'F'))
    # print(bellman_ford(g, 'A', 'F'))
    print(connected(g2))
    
    
