#   *       s:1 ,   sp = 2   d=0  N//2-d
#  ***      s:3,    sp = 1   d=1
# *****     s:5,    sp = 0   d=2
#  ***
#   *

def print_diamond(N):
    if N <= 0:
        return
        
    def _printd(depth):
            
        for i in range(N//2-depth):
            print(" ", end="")
        for i in range(2*depth+1):
            print("*", end="")
        print("")

        if depth > N//2 -1:
            return
        
        _printd(depth+1)
        
        for i in range(N//2-depth):
            print(" ", end="")
        for i in range(2*depth+1):
            print("*", end="")
        print("")
    
    _printd(0)
        

if __name__ == '__main__':
    N = 7
    print_diamond(N)