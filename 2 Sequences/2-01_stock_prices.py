# Given predicted stock prices for next n days for a stock,
# find the maximum profit that can be made with a single buy-sell transaction.
# If no profit can be made return 0.
# e.g
# [20, 40, 52, 15, 30, 50, 10, 25] -> 35 / buying at 15 and selling at 50 gives maximum profit.

import math

def stock_gain(P):
    len_p = len(P)
    
    max_gain = -math.inf
    max_buy = -1
    max_sell = -1
    current_buy = 0
    
    for i in range(1, len_p):
        # assuming selling at i th day
        gain = P[i] - P[current_buy]
        if gain > max_gain:
            max_gain = gain
            max_buy = current_buy
            max_sell = i
        
        if P[i] < P[current_buy]:
            current_buy = i
            
    if max_gain < 0:
        return 0
        
    return max_gain, P[max_buy], P[max_sell] 
            

if __name__ == '__main__':
    P = [20, 40, 52, 15, 30, 50, 10, 25] # 35 / 15,50
    print(stock_gain(P))