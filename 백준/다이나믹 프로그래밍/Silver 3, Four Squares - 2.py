# Python3 => 시간초과
# PyPy3 => 252ms

from copy import deepcopy

D = {}

# cnt == 1
i = 1
while True:
    j = i ** 2
    if j > 50_000:
        break
    if j not in D:
        D[j] = 1
    i += 1

# else
for cnt in [2, 3, 4]:
    i = 1
    key_list = deepcopy(list(D.keys()))
    while True:
        j = i ** 2
        if j > 50_000:
            break
        for key in key_list:
            if key + j > 50_000:
                continue
            if key + j not in D:
                D[key + j] = cnt
        i += 1

print(D[int(input())])