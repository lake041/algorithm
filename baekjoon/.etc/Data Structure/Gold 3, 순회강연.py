from heapq import heappush, heappop

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key = lambda x: x[1])

p_list = []
for i in lst:
    heappush(p_list, i[0])
    if(len(p_list) > i[1]):
        heappop(p_list)
print(sum(p_list))

'''
5
3 3
2 3
1 3
100 4
90 4
=> 195

7
20 1
2 1
10 3
100 2
8 2
5 20
50 10
=> 185
'''