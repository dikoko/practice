# Give an infinite supply of coins of N different denominations (values), (V1, V2, … , VN).
# Find the minimum number of coins that sum up to a number S.

import math

# a DP solution
def min_coins(coins, S):
    
    len_c = len(coins)
    T = [[math.inf]*(S+1) for _ in range(len_c)]
    
    for i in range(len_c):
        T[i][0] = 0
        
    for j in range(S+1):
        if j % coins[0] == 0:
            T[0][j] = j // coins[0]
    
    for i in range(1, len_c):
        for j in range(1, S+1):
            T[i][j] = min(1+T[i][j-coins[i]], T[i-1][j])
            
    return T[len_c-1][S]
        
if __name__ == '__main__':
    c1 = [1, 2, 5, 10, 20, 50] # S=65 → 3 (50+10+5)
    c2 = [1, 2, 5, 10, 12, 20, 50] # S=65 → 3 (50+10+5)
    c3 = [1, 5, 6, 9] # S=11 → 2 (6+5)
    
    print(min_coins(c1, 65))
    print(min_coins(c2, 65))
    print(min_coins(c3, 11))        