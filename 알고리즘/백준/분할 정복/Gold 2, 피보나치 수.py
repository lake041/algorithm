from itertools import product

N = int(input())
I = [[1, 1], [1, 0]]

def mul(m1, m2):
    new = [[0, 0], [0, 0]]
    for row, col in product(range(2), range(2)):
        new[row][col] = (m1[row][0]*m2[0][col] + m1[row][1]*m2[1][col]) % 1_000_000_007
    return new

# matrix를 number 제곱한다.
def cal(matrix, number):
    global I
    if number == 1:
        return matrix
    if number % 2 == 0:
        temp = cal(matrix, number//2)
        return mul(temp, temp)
    else:
        temp = cal(matrix, number-1)
        return mul(temp, matrix)

print(cal(I, N)[0][1])