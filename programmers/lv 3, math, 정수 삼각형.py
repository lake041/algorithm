def solution(triangle):
    length = len(triangle)
    sums = [[0]*length for _ in range(length)]
    sums[0][0] = triangle[0][0]
    for i in range(1, length):
        sums[i][0] = sums[i-1][0] + triangle[i][0]
        sums[i][i] = sums[i-1][i-1] + triangle[i][i]
        for j in range(1, i):
            last_max = max(sums[i-1][j-1], sums[i-1][j])
            sums[i][j] = triangle[i][j] + last_max
    answer = max(sums[-1])
    # answer = sums
    return answer