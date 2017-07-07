# Given a column title as appears in an Excel sheet, return its corresponding column number.
# e.g.:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
# BCSUS → 980089

def excel_number2(instr):
    inlist = list(instr)
    len_n = len(inlist)
    inlist = list(map(lambda x: ord(x) - ord('A'), inlist)) # make 0 based number list
    inlist.reverse()
    
    num = 0
    d = 0 # digit number
    for n in inlist:
        n += 1
        num += n*(26**d)
        d += 1
    
    return num
    
    

if __name__ == '__main__':
    s1 = 'A' # 1
    s2 = 'B' # 2
    s3 = 'Z' # 26
    s4 = 'AA' # 27
    s5 = 'AB' # 28
    s6 = 'BCSUS' # 980089
    
    print(excel_number2(s1))    
    print(excel_number2(s2))
    print(excel_number2(s3))    
    print(excel_number2(s4))
    print(excel_number2(s5))    
    print(excel_number2(s6))    