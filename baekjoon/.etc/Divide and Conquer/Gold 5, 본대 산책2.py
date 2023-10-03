from itertools import product

# 정보과학관 0, 전산관 1, 미래관 2, 신양관 3, 한경직기념관 4, 진리관 5, 학생회관 6, 형남공학관 7
M = [[0]*8 for _ in range(8)]
M[0][1], M[0][2] = 1, 1
M[1][0], M[1][2], M[1][3] = 1, 1, 1
M[2][0], M[2][1], M[2][3], M[2][4] = 1, 1, 1, 1
M[3][1], M[3][2], M[3][4], M[3][5] = 1, 1, 1, 1
M[4][2], M[4][3], M[4][5], M[4][7] = 1, 1, 1, 1
M[5][3], M[5][4], M[5][6] = 1, 1, 1 
M[6][5], M[6][7] = 1, 1
M[7][4], M[7][6] = 1, 1

def mul(m1, m2):
    width = len(m1[0])
    height = len(m2)
    new = [[0]*width for _ in range(height)]
    for row, col in product(range(height), range(width)):
        for i in range(width):
            new[row][col] = (new[row][col] + m1[row][i] * m2[i][col]) % 1_000_000_007
    return new

def cal(matrix, cnt):
    global M
    if cnt == 1:
        return matrix
    if cnt % 2 == 0:
        next = cal(matrix, cnt//2)
        return mul(next, next)
    else:
        next = cal(matrix, cnt-1)
        return mul(next, M)

result = cal(M, int(input()))[0][0]
print(result)