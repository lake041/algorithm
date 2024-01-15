from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    min_heap, max_heap = [], []
    exist = [False] * (K+1)

    for i in range(K):
        order, N = input().split()
        N = int(N)
        if order == 'I':
            heappush(min_heap, (N, i))
            heappush(max_heap, (-N, i))
            exist[i] = True
        elif N == 1:
            while max_heap and not exist[max_heap[0][1]]:
                heappop(max_heap)
            if max_heap:
                exist[max_heap[0][1]] = False
                heappop(max_heap)
        elif N == -1:
            while min_heap and not exist[min_heap[0][1]]:
                heappop(min_heap)
            if min_heap:
                exist[min_heap[0][1]] = False
                heappop(min_heap)

    while max_heap and not exist[max_heap[0][1]]:
        heappop(max_heap)
    while min_heap and not exist[min_heap[0][1]]:
        heappop(min_heap)
    
    if not min_heap:
        print('EMPTY')
    else:
        print(-heappop(max_heap)[0], heappop(min_heap)[0])