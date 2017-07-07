# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA 26+1
#     28 -> AB 26+2

def excel_number(N):
    out_list = []
    while N > 0:
        N -= 1 # make each 0 based
        digit = N % 26
        out_list.append(digit)
        N //=26
    
    out_list.reverse()
    return "".join(map(lambda x: chr(ord('A')+x), out_list))
        

if __name__ == '__main__':
    n1 = 26 # Z
    n2 = 27 # AA
    n3 = 28 # AB
    n4 = 980089 # BCSUS
    
    print(excel_number(n1))
    print(excel_number(n2))
    print(excel_number(n3))
    print(excel_number(n4))