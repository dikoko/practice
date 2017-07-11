# Write a basic Regex engine implementing the "." (any character) and "*" (previous rule, 0 to many).
# The function receives a string (letters only, no need for escaping) and a string pattern.
# It returns a bool whether the string matches the pattern.
# For example, the pattern "AB.*E" should match both "ABCDE" and "ABEEE".

def wildcard(pattern, instr):
    
    len_pattern = len(pattern)
    len_in = len(instr)
    
    _wtable = [[False]*(len_pattern+1) for _ in range(len_in+1)]
    _wtable[0][0] = True
    
    for j in range(1, len_pattern+1):
        _wtable[0][j] = _wtable[0][j-1] if pattern[j-1]=='*' else False
    
    for i in range(1, len_in+1):
        for j in range(1, len_pattern+1):
            if instr[i-1] == pattern[j-1] or pattern[j-1] == '.':
                _wtable[i][j] = _wtable[i-1][j-1]
            elif pattern[j-1] == '*':
                _wtable[i][j] = _wtable[i-1][j] or _wtable[i][j-1]
            else:
                _wtable[i][j] = False
    
    for i in range(len_in+1):
        print(_wtable[i])
    
    return _wtable[len_in][len_pattern]


def regex(pattern, instr):
    
    len_pattern = len(pattern)
    len_in = len(instr)
    
    _wtable = [[False]*(len_pattern+1) for _ in range(len_in+1)]
    _wtable[0][0] = True
    
    for j in range(1, len_pattern+1):
        _wtable[0][j] = _wtable[0][j-2] if pattern[j-1]=='*' else False
    
    for i in range(1, len_in+1):
        for j in range(1, len_pattern+1):
            if instr[i-1] == pattern[j-1] or pattern[j-1] == '.':
                _wtable[i][j] = _wtable[i-1][j-1]
            elif pattern[j-1] == '*':
                if instr[i-1] == pattern[j-2] or pattern[j-2] == '.':
                    _wtable[i][j] = _wtable[i-1][j]
                _wtable[i][j] = _wtable[i][j] or _wtable[i][j-2]
            else:
                _wtable[i][j] = False
    
    for i in range(len_in+1):
        print(_wtable[i])
    
    return _wtable[len_in][len_pattern]


if __name__ == '__main__':
    p1 = 'AB.*E'
    str1 = 'ABCDE'
    str2 = 'ABEEE'
    # p2 = 'x.y*z'
    # str3 = 'xaylmz'
    # str4 = 'xaylmsl'
    
    print(wildcard(p1, str1))
    print(wildcard(p1, str2))
    # print(wildcard(p2, str3))
    # print(wildcard(p2, str4))
    
    print(regex(p1, str1))
    print(regex(p1, str2))