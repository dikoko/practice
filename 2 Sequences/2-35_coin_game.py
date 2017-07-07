# There are N coins (Assume N is even) in a line.
# Two players take turns to take a coin from one of the ends of the line until there are no more coins left.
# The player with the larger amount of money wins. Assume that you go first.
# Write a program which computes the maximum amount of money you can win.

# assuming that there are i, i+1, .... , j coins
# if I take i, the opponent can take i+1 or j
# if I take j, the opponent can take i or j-1
# the opponent will do his/her best

def max_coin(coins):
    len_c = len(coins)
    
    def _maxc(i, j):
        if i == j:
            return coins[i]
        if i == j-1:
            return max(coins[i], coins[j])
        
        return max(coins[i] + min(_maxc(i+2,j), _maxc(i+1,j-1)), # if I take i th coin
                    coins[j] + min(_maxc(i, j-2), _maxc(i+1, j-1))) # if I take j th coin
    
    return _maxc(0, len_c-1)
                    
            
# [1, 2, 3, 4]
# _m(0, 3)
#  max(1 + 3 , 4 + 2 ) = 6
# --
# _m(2,3)
        

if __name__ == '__main__':
    coins1 = [1, 2, 3, 4] # 6
    coins2 = [8, 15, 3, 7] # 22
    
    print(max_coin(coins1))
    print(max_coin(coins2))
