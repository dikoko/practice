# Given two strings, return boolean True/False,
# if they are only one edit apart.
# Edit can be insert/delete/update of only one character in the string. Eg:
# -True
# xyz,xz
# xyz, xyk
# xy, xyz
#
# -False
# xyz, xyz
# xyz,xzy
# x, xyz

def edit_distance(str1, str2):
    if not str1 or not str2: return
    
    len1 = len(str1)
    len2 = len(str2)
    
    T = [[0]*(len2+1) for _ in range(len1+1)]
    for i in range(1, len1+1):
        T[i][0] = i
    for j in range(1, len2+1):
        T[0][j] = i
        
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if str1[i-1] == str2[j-1]:
                T[i][j] = T[i-1][j-1]
            else:
                T[i][j] = 1+ min(T[i-1][j], T[i][j-1], T[i-1][j-1])
    
    return T[len1][len2]
        
    
def check_distanceone(str1, str2):
    dist = edit_distance(str1, str2)
    if dist == 1:
        return True, dist
    else:
        return False, dist

if __name__ == '__main__':
    p1 = ('xyz', 'xz')
    p2 = ('xyz', 'xyk')
    p3 = ('xy', 'xyz')

    p4 = ('xyz', 'xyz')
    p5 = ('xyz', 'xzy')
    p6 = ('x', 'xyz')
    
    p7 = ('saturday', 'sunday')

    print(check_distanceone(*p1))
    print(check_distanceone(*p2))
    print(check_distanceone(*p3))
    print(check_distanceone(*p4))
    print(check_distanceone(*p5))
    print(check_distanceone(*p6))
    
    print(check_distanceone(*p7))
