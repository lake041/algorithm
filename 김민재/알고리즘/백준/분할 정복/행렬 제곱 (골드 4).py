N, B = map(int, input().split())
matrix = [list(map(lambda x: int(x) % 1000, input().split())) for _ in range(N)]

def multiply(X, Y):
    Y = list(map(list, zip(*Y)))
    return [[sum(a * b for a, b in zip(X_row, Y_col)) % 1000 for Y_col in Y] for X_row in X]

def power(A, B):
    if B == 1:
        return A
    elif B % 2 == 0:
        half = power(A, B//2)
        return multiply(half, half)
    else:
        return multiply(power(A, B-1), A)

result = power(matrix, B)
for row in result:
    print(*row)