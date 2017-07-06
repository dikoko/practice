# Given both positive integer M and N (M < N), find all stepping numbers in range M to N.
# A number is called a stepping number if the adjacent digits have a only one difference.
# e.g. 234 or 232 is a stepping number but 346 is not a stepping number.

def step_number(M, N):
    if M < 0 or N < 0 or M > N: return []
    
    out_list = []
    def _gen_stepn(seed):
        wqueue = [seed]
        while wqueue:
            node = wqueue.pop(0)
            
            if node >= M and node <= N:
                out_list.append(node)
            
            if node == 0 or node > N:
                continue
            
            last_digit = node % 10
            pass_high = node*10 + (last_digit+1) # for 234 -> 2340 + (4+1) = 2345
            pass_low = node*10 + (last_digit-1) # for 234 -> 2340 + (4-1) = 2343
            
            if last_digit == 9:
                wqueue.append(pass_low)
            elif last_digit == 0:
                wqueue.append(pass_high)
            else:
                wqueue.append(pass_low)
                wqueue.append(pass_high)
                
    for i in range(10):
        _gen_stepn(i)
    
    return out_list



if __name__ == '__main__':
    M = 10
    N = 20 # [10, 12]
    print(step_number(M, N))
