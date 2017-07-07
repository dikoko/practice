# Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

def diagonal(matrix):
    N = len(matrix[0])

    out_list = []
    for i in range(N):
        group = []
        for j in range(i+1):
            group.append(matrix[j][i-j])
        out_list.append(group)
    
    for i in range(N-1):
        group = []
        for j in range(N-1-i):
            group.append(matrix[i+j+1][N-1-j])
        out_list.append(group)
    
    return out_list
    

# i = 0, 1, 2
# j = 0, i
# i = 0 (0,0)
# i = 1 (0,1), (1,0)
# i = 2 (0,2), (1,1), (2,0)
#
#
# i = 0 (1,2), (2,1) j=N-1-i, 0, 1  (i+j+1,len-1  -j
# i = 1 (2,2)        j = 0
#
# 1  2  3  4
# 5  6  7  8
# 9  10 11 12
# 13 14 15 16
#
# i = 0 (1,3) (2,2), (3,1) j=0,1,2
# i = 1 (2,3) (3,2)  j=0,1
# i = 2 (3,3)    j=0

if __name__ == '__main__':
    m1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    
    m2 = [[1, 2], 
            [3, 4]]
            
    m3 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]
            
    print(diagonal(m1))
    print(diagonal(m2))
    print(diagonal(m3))        