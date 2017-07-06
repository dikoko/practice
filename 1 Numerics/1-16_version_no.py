# Compare two version numbers version1 and version2.
# If version1 > version2 return 1,
# If version1 < version2 return -1,
# otherwise return 0.
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# e.g.
# 0.1 < 1.1 < 1.2 < 1.13 < 1.13.4
# 1.0 == 1

def comp_versions(v1, v2):
    v1s = list(map(int, v1.split('.')))
    v2s = list(map(int, v2.split('.')))
    
    while v1s and v2s:
        v1 = v1s.pop(0)
        v2 = v2s.pop(0)
        
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1

    if not v1s and not v2s:
        return 0
    elif v1s: # v2s is over
        for v in v1s:
            if v > 0:
                return 1
        else:
            return 0
    else: # v1 is over
        for v in v2s:
            if v > 0:
                return -1
        else:
            return 0


if __name__ == '__main__':
    v1 = '1.1'
    v2 = '1.1.13'
    v3 = '1.13.4'

    v4 = '1'
    v5 = '1.0.0'
    
    print(comp_versions(v1, v2)) # -1
    print(comp_versions(v1, v3)) # -1
    print(comp_versions(v2, v3)) # -1
    print(comp_versions(v3, v2)) # 1
    print(comp_versions(v4, v5)) # 0
