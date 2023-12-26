# regex 및 슬라이딩 윈도우

import re

N = int(input())
M = int(input())
S = input()

##  regex & look ahead assertion
##  서브태스크2 시간 초과
P = '(?=' + 'I' + 'OI' * N + ')'
print(len(re.findall(P, S)))

##  서브태스크2 시간 초과
# P = 'I' + 'OI' * N
# p_len = 2*N + 1
# ans = 0
# for i in range(M-p_len+1):
# 	if S[i:i+p_len] == P:
# 		ans += 1
# print(ans)

cursor, count, result = 0, 0, 0

# 슬라이딩 윈도우
while cursor < (M - 1):
    if S[cursor:cursor + 3] == 'IOI':
        count += 1
        cursor += 2
        if count == N:
            result += 1
            count -= 1
    else:
        cursor += 1
        count = 0

print(result)