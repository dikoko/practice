# There's a room with a TV and people are coming in and out to watch it.
# The TV is on only when there's at least a person in the room.
# For each person that comes in, we record the start and end time.
# We want to know for how long the TV has been on.
# In other words: Given a list of arrays of time intervals,
# write a function that calculates the total amount of time covered by the intervals.

def tv_time(times):
    
    len_t = len(times)
    on_time = 0
    current_on = 0
    current_off = 0
    
    times.sort() # sort with tiem start time
    
    for start, end in times:
        if start > current_off: # new time start
            on_time += current_off - current_on
            current_on = start
            current_off = end
        else: # extend the previous span
            if end > current_off:
                current_off = end
                
    on_time += current_off - current_on # DON'T FORGET THE REMAINS
    
    return on_time
            
if __name__ == '__main__':
    t1 = [(1,4), (2,3)] # 3
    t2 = [(4,6), (1,2)] # 3
    t3 = [(1,4), (6,8), (2,4), (7,9), (10, 15)] # 11
    print(tv_time(t1))
    print(tv_time(t2))
    print(tv_time(t3))        