# Given predicted stock prices for next n days for a stock,
# find the maximum profit that can be made with K buy-sell transactions.

# a DP solution
def stock_gain(P, K):

    len_p = len(P)
    T = [[0]*len_p for _ in range(K+1)]
    
    for i in range(1, K+1):
        for j in range(1, len_p):
            for m in range(j):
                T[i][j] = max(T[i][j], T[i][j-1], (P[j]-P[m])+T[i-1][m])
                # T[i][j-1] : the case not selling j th day
                # P[j] - P(m) + T[i-1][m] : selling jth day and buying mth day 
                #    and minus one transaction at mth day
    
    for i in range(K+1):
        print(T[i])
    
    return T[K][len_p-1]
    


if __name__ == '__main__':
    P = [20, 50, 70, 10, 40, 30, 10, 30] # K = 3
    print(stock_gain(P, 3))