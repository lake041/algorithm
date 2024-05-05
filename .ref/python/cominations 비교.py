from time import time
from itertools import combinations

N = 40
R = 5

def custom_combi(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        element = arr[i]
        rest_arr = arr[i+2:]
        for rest_combi in custom_combi(rest_arr, n-1):
            result.append([element] + rest_combi)
    
    return result

start_time = time()
cnt = 0
for combi in combinations(range(N), R):
    if all(combi[i+1] - combi[i] > 1 for i in range(len(combi)-1)):
        cnt += 1
end_time = time()
print(cnt)
print("첫 번째 코드 실행 시간:", end_time - start_time, "초")

start_time = time()
print(len(custom_combi(range(N), R)))
end_time = time()
print("두 번째 코드 실행 시간:", end_time - start_time, "초")

start_time = time()
print(len(list(combinations(range(26), 5))))
end_time = time()
print("세 번째 코드 실행 시간:", end_time - start_time, "초")

# def combinations2(iterable, r):
#     pool = tuple(iterable)
#     n = len(pool)
#     if r > n:
#         return
#     indices = list(range(r))
#     yield tuple(pool[i] for i in indices)
#     while True:
#         for i in reversed(range(r)):
#             if indices[i] != i + n - r:
#                 break
#         else:
#             return
#         indices[i] += 1
#         for j in range(i+1, r):
#             indices[j] = indices[j-1] + 1
#         yield tuple(pool[i] for i in indices)

# start_time = time()
# print(len(list(combinations2(range(26), 5))))
# end_time = time()
# print("네 번째 코드 실행 시간:", end_time - start_time, "초")