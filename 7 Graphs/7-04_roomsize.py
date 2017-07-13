from collections import defaultdict

class Room(object):
    def __init__(self, floors, M, N, x,y):
        self.floors = floors
        self.M = M
        self.N = N
        self.x = x
        self.y = y

    def read(self, i, j):
        if i < 0 or j < 0 or i >= self.M or j >= self.N:
            return 'W'
        return self.floors[i*self.N + j]
    
    def move(self, direction):
        if direction == 0:
            space = self.read(self.x - 1, self.y)
            if space == 'X':
                self.x = self.x - 1
                return True
            else:
                return False
        elif direction == 1:
            space = self.read(self.x, self.y-1)
            if space == 'X':
                self.y = self.y - 1
                return True
            else:
                return False
        elif direction == 2:
            space = self.read(self.x +1, self.y)
            if space == 'X':
                self.x = self.x +1
                return True
            else:
                return False
        else:
            space = self.read(self.x, self.y+1)
            if space == 'X':
                self.y = self.y + 1
                return True
            else:
                return False
                
def room_size(room):
    
    ci, cj = 0, 0 # current i, current j
    wstack = [(0,0)]
    from_stack = [(0,0)]
    _visited = defaultdict(bool)
    room_size = 0
    
    reverse_move = []
    while wstack:
        i, j = wstack.pop() # where to go
        from_i, from_j = from_stack.pop()
        print(i, j, from_i, from_j, ci, cj)
        
        # back tracking
        while from_i != ci or from_j != cj:
            rmove = reverse_move.pop()
            if rmove == 0:
                ci -= 1
                room.move(0)
            elif rmove == 1:
                cj -= 1
                room.move(1)
            elif rmove == 2:
                ci += 1
                room.move(2)
            else:
                cj += 1
                room.move(3)
        
        # actual moves        
        if i - from_i == -1:
            room.move(0)
            reverse_move.append(2)
            ci -= 1
        elif j - from_j == -1:
            room.move(1)
            reverse_move.append(3)
            cj -= 1
        elif i - from_i == 1:
            room.move(2)
            reverse_move.append(0)
            ci += 1
        elif j - from_j == 1:
            room.move(3)
            reverse_move.append(1)
            cj += 1
                
        if not _visited[(i, j)]:            
            _visited[(i, j)] = True
            room_size += 1
            
            # check next visitable nodes
            if not _visited[(i-1,j)] and room.move(0): # up
                room.move(2) # back to here
                wstack.append((i-1,j))
                from_stack.append((i,j))
            if not _visited[(i, j-1)] and room.move(1): # left
                room.move(3)
                wstack.append((i, j-1))
                from_stack.append((i,j))
            if not _visited[(i+1, j)] and room.move(2): # down
                room.move(0)
                wstack.append((i+1, j))
                from_stack.append((i,j))
            if not _visited[(i, j+1)] and room.move(3): # right
                room.move(1)
                wstack.append((i, j+1))
                from_stack.append((i,j))

    return room_size
                    
if __name__ == '__main__':
    floors = [
                'X','W','W','W','W',
                'X','X','X','W','X',
                'X','X','X','X','X'
            ]
    
    room = Room(floors, 3, 5, 0, 0)
    print(room_size(room))
