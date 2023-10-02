import time
from itertools import product
N = 10000
x = [[0]*N for _ in range(N)]

# nested loop
s_time = time.process_time()
for i in range(N):
    for j in range(N):
        x[i][j] = i+j
e_time = time.process_time()
print(f"time elapsed : {int(round((e_time - s_time) * 1000))}ms")

# product
s_time = time.process_time()
for i, j in product(range(N), repeat=2):
    x[i][j] = i+j
e_time = time.process_time()
print(f"time elapsed : {int(round((e_time - s_time) * 1000))}ms")