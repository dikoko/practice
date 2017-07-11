def find_pivot(words):
    if not words: return
    
    len_words = len(words)
    
    def _findp(low, high):
        if low > high:
            return 0
            
        mid = low + (high-low)//2
        
        if mid > low and words[mid-1] > words[mid]:
            return mid
        elif mid < high and words[mid] > words[mid+1]:
            return mid+1
        
        if words[low] <= words[mid]: # pivot is at right
            return _findp(mid+1, high)
        else:
            return _findp(low, mid-1)
    
    pindex = _findp(0, len_words-1)
    return words[pindex]
    

if __name__ == '__main__':
    words = [ "ptolemaic", 
    "retrograde", 
    "supplant", 
    "undulate", 
    "xenoepist", 
    "asymptote", 
    "babka", 
    "banoffee", 
    "engender", 
    "karpatka", 
    "othellolagkage" ]
    
    print(find_pivot(words))