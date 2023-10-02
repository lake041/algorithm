# Python3 => 시간초과
# PyPy3 => 384ms

import sys
import math

N = int(input())
DP = {0:0, 1:1}
for i in range(2, N+1):
    minValue = sys.maxsize
    for j in range(1, int(math.sqrt(i))+1):
        minValue = min(minValue, DP[i-j**2])
    DP[i] = 1 + minValue
print(DP[N])