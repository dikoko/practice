# Given a task sequence tasks such as ABBABBC, and an integer k,
# which is the cool down time between two same tasks. Assume the execution for each individual task is 1 unit.
# Rearrange the task sequence such that the execution time is minimal.

from collections import defaultdict

class WaitingQueue(object):
    def __init__(self, K):
        self.K = K
        self.wqueue = []
    
    def add_queue(self, task):
        self.wqueue.append(task)
        if len(self.wqueue) > self.K:
            return self.wqueue.pop(0)
        else:
            return None

def min_task_sequence(tasks, K):
    
    counter = defaultdict(int)
    for t in tasks:
        counter[t] += 1
    
    out_list = []
    num_tasks = len(tasks)
    wqueue = WaitingQueue(K)
    
    while num_tasks > 0:
        for t in counter.keys():
            if counter[t] > 0:
                out_list.append(t)
                counter[t] -= 1
                counter[t] *= -1
                num_tasks -= 1
                new_available = wqueue.add_queue(t)
                if new_available:
                    counter[new_available] *= -1
                break ###########
        else:
            out_list.append('_')
            new_available = wqueue.add_queue(None)
            if new_available:
                counter[new_available] *= -1
    
    return len(out_list), "".join(out_list)
    

if __name__ == '__main__':
    t1 = 'AAABBBCCC' # K=3, ABC_ABC_ABC
    t2 = 'AAABC' # K=2 , ABCA__A
    t3 = 'AAADBBCC' # k=2, ABCABCDA
    
    print(min_task_sequence(t1, 3))
    print(min_task_sequence(t2, 2))
    print(min_task_sequence(t3, 2))
    