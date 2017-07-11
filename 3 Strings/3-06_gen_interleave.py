# Given two strings, print all the interleavings of the strings.
# e.g. AB,XY ⇒ ABXY, AXBY, AXYB, XABY, XAYB, XYAB

def gen_interleaved(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    
    def _gen_str(i, j):
        if i == len1 and j == len2:
            return [[]]
        
        picked1_results = []
        picked2_results = []
        
        if i < len1:
            picked1 = s1[i]
            picked1_results = _gen_str(i+1, j)
            for item in picked1_results:
                item.append(picked1)
        
        if j < len2:
            picked2 = s2[j]
            picked2_results = _gen_str(i, j+1)
            for item in picked2_results:
                item.append(picked2)
        
        return picked1_results + picked2_results
    
    results = _gen_str(0,0)
    return ["".join(reversed(item)) for item in results]
        


if __name__ == '__main__':
    s1 = 'AB'
    s2 = 'XY'
    
    s3 = 'xyz'
    s4 = 'abcd'
    print(gen_interleaved(s1,s2))
    print(gen_interleaved(s3,s4))
