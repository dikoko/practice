from collections import defaultdict

class Maze(object):
    def __init__(self, mlist, M, N):
        self.mlist = mlist
        self.M = M
        self.N = N
        
    def read(self, i, j):
        if i < 0 or j < 0 or i >= self.M or j >= self.N:
            return 'X'
        return self.mlist[i*self.N+j]
    
    def get_start(self):
        for i in range(len(self.mlist)):
            if self.mlist[i] == 'R':
                return i//self.N, i%self.N
        return -1, -1

def find_exit(maze):
    
    _visited = defaultdict(bool)
    
    def _find(i, j):
        _visited[(i,j)] = True
        cell = maze.read(i,j)

        if cell == 'T':
            return True
        
        is_found = False
        if not _visited[(i-1,j)] and maze.read(i-1,j) != 'X':
            is_found |= _find(i-1,j)
        if not _visited[(i,j-1)] and maze.read(i,j-1) != 'X':
            is_found |= _find(i,j-1)
        if not _visited[(i+1,j)] and maze.read(i+1,j) != 'X':
            is_found |= _find(i+1,j)
        if not _visited[(i,j+1)] and maze.read(i,j+1) != 'X':
            is_found |= _find(i,j+1)
            
        return is_found
        
    i, j = maze.get_start()
    return _find(i, j)
            
        

if __name__ == '__main__':
    mlist = [
        'X','_','_','R','_','X', 
        'X','_','X','X','X','_', 
        '_','_','_','_','_','_', 
        '_','X','X','_','X','X', 
        'X','T','_','_','X','_'
        ] 
        
    mlist2 = [
        'X','X','_','_','_','_','_','X',
        'X','X','_','X','X','X','_','X',
        'X','X','_','X','R','X','_','_',
        'X','X','_','X','_','X','_','_',
        '_','_','_','X','_','X','_','X',
        '_','X','X','X','_','_','_','X',
        '_','T','X','_','_','X','X','X'
    ]

    mlist3 = [
        'X','_','_','X','X',
        'X','X','R','_','_',
        '_','_','_','X','X',
        '_','X','_','X','X',
        'X','T','X','X','X'
    ]

    m = Maze(mlist, 5, 6)
    print(find_exit(m))
    
    maze2 = Maze(mlist2,7,8)
    print(find_exit(maze2))

    maze3 = Maze(mlist3,5,5)
    print(find_exit(maze3))
