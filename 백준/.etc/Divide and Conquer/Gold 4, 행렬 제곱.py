from itertools import product

N, B = map(int, input().split())
M = [list(map(lambda x: int(x) % 1000, input().split())) for _ in range(N)]

def multiply_matrix(A, B):
    if B <= 1:
        return A
    elif B%2 == 0:
        temp = multiply_matrix(A, B//2)
        return mul(temp, temp)
    else:
        return mul(A, multiply_matrix(A, B-1))

def mul(A, B):
    result = [[0]*N for _ in range(N)]
    for i, j in product(range(N), range(N)):
        sum_ = 0
        for k in range(N):
            sum_ += (A[i][k] * B[k][j]) % 1000
        result[i][j] = sum_%1000 
    return result

result_matrix = multiply_matrix(M, B)

for row in result_matrix:
    print(*row)
