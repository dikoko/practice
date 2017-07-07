# Find out if the given string forms a valid lottery number.
# A valid lottery number contains 7 unique digits between 1 and 59.
# e.g.
# 4938532894754 (True) -> 49 38 53 28 9 47 54
# 1634616512 (True) -> 1 6 34 6 16 51 2
# 1122334 (False)

# 7 unique and 1-59 number
def lottery_number(lstr):
    
    len_l = len(lstr)
    
    def _lottery(i, k, picks):
        if i == len_l and k == 0:
            return [picks]
        if i == len_l or k == 0:
            return []
        
        # pick 1 digit
        one_results = []
        one_pick = int(lstr[i])
        if one_pick >= 1 and one_pick <= 9 and one_pick not in picks:
            forward_one = picks[:]
            forward_one.append(one_pick)
            one_results = _lottery(i+1, k-1, forward_one)
        
        two_results = []
        if i < len_l -1:
            two_pick = int(lstr[i:i+2])
            if two_pick >= 10 and two_pick <= 59 and two_pick not in picks:
                forward_two = picks[:]
                forward_two.append(two_pick)
                two_results = _lottery(i+2, k-1, forward_two)
        
        return one_results + two_results
    
    return _lottery(0, 7, [])
        

if __name__ == '__main__':
    l1 = '4938532894754'
    l2 = '1634616512'
    l3 = '1122334'
    
    print(lottery_number(l1))
    print(lottery_number(l2))
    print(lottery_number(l3))        