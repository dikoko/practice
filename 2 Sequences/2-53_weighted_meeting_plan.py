# Given a series of meetings, how to schedule them.
# Cannot attend more than a meeting at the same time.
# Goal is to find maximum weight subset of mutually non-overlap meetings.

from operator import itemgetter

def weight_meetings(ms):
    
    len_m = len(ms)
    ms.sort(key=itemgetter(1)) # sort with end time
    
    def _max_weight(i, end_time):
        if i == len_m:
            return 0
        
        current_start, current_end, current_val = ms[i]
        
        picked_results = 0
        if current_start >= end_time: # can dispatch
            picked_results = current_val + _max_weight(i+1, current_end)
        unpicked_results = _max_weight(i+1, end_time)
        
        return max(picked_results, unpicked_results)
    
    return _max_weight(0, 0)
        
    

if __name__ == '__main__':
    ms = [(1,2,50), (3,5,20), (6,19,100), (2,100,200)]
    
    print(weight_meetings(ms))
    