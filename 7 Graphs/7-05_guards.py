from collections import defaultdict
import math

class Museum(object):
    def __init__(self, mlist, M, N):
        self.mlist = mlist
        self.M = M
        self.N = N
        
    def read(self, i, j):
        if i < 0 or j < 0 or i >= self.M or j >= self.N:
            return 'W'
        return self.mlist[i*self.N + j]
    
    def guards(self):
        out_list = []
        for i in range(len(self.mlist)):
            if self.mlist[i] == 'G':
                out_list.append((i//self.N, i%self.N))
        return out_list


def get_distances(m):
    
    guards = m.guards()
    M = m.M
    N = m.N
    _dists = [math.inf]*(M * N)
    
    for i, j in guards:
        _visited = defaultdict(bool)
        _dists[i*N+j] = 0
        _visited[(i,j)] = True
        wqueue = []
        if m.read(i-1,j) != 'W':
            wqueue.append((i-1,j,1))
        if m.read(i,j-1) != 'W':
            wqueue.append((i,j-1,1))
        if m.read(i+1,j) != 'W':
            wqueue.append((i+1,j,1))
        if m.read(i,j+1) != 'W':
            wqueue.append((i,j+1,1))
        
        while wqueue:
            vi, vj, d = wqueue.pop(0)
            if not _visited[(vi, vj)]:
                # visit
                _visited[(vi, vj)] = True
                if d < _dists[vi*N + vj]:
                    _dists[vi*N + vj] = d
                    
                if not _visited[(vi-1, vj)] and m.read(vi-1,vj) != 'W':
                    wqueue.append((vi-1,vj,d+1))
                if not _visited[(vi, vj-1)] and m.read(vi,vj-1) != 'W':
                    wqueue.append((vi,vj-1,d+1))
                if not _visited[(vi+1, vj)] and m.read(vi+1,vj) != 'W':
                    wqueue.append((vi+1,vj,d+1))
                if not _visited[(vi, vj+1)] and m.read(vi,vj+1) != 'W':
                    wqueue.append((vi,vj+1,d+1))
                    
    # now _dists all set up
    for i in range(M*N):
        if m.mlist[i] == 'W':
            _dists[i] = 'W'
    
    return _dists            
                


if __name__ == '__main__':
    mlist = [
        'W','W','W','W','W','O','W',
        'W','O','O','G','O','O','W',
        'O','G','O','O','O','O','O',
        'W','W','O','O','O','W','W',
        'W','O','O','W','G','W','W'
        ]
    m = Museum(mlist, 5, 7)
    out_list = get_distances(m)
    
    for i in range(m.M):
        for j in range(m.N):
            print(out_list[i*m.N + j], end=" ")
        print("")