# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
#
# P.......A........H.......N
# ..A..P....L....S....I...I....G
# ....Y.........I........R
# And then read line by line: PAHNAPLSIIGYIR
# Write the code that will take a string and make this conversion given a number of rows:
#
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR" e.g.2 :
# ABCD, 2 can be written as
# A....C
# ...B....D
# and hence the answer would be ACBD.

def zigzag_convert(instr, K):
    if K < 1: return
    if K == 1: return instr  #########
    len_s = len(instr)
    
    text_queue = [[] for _ in range(K)]
    
    q_index = 0
    is_reverse = False
    for i in range(len_s):
        text_queue[q_index].append(instr[i])
        
        if q_index == K-1:
            is_reverse = True
        if q_index == 0:
            is_reverse = False
        
        if is_reverse:
            q_index -= 1
        else:
            q_index += 1

    out_list = []
    for k in range(K):
        for c in text_queue[k]:
            out_list.append(c)
    
    return "".join(out_list)
    


if __name__ == '__main__':
    instr1 = "ABCD" # 2 "ACBD"
    instr2 = "PAYPALISHIRING" # 3 "PAHNAPLSIIGYIR"

    print(zigzag_convert(instr1, 2))
    print(zigzag_convert(instr2, 3))    