# 복습 필수
'''
다익스트라의 출발점을 한 번에 넣으면,
출발점들 중 하나에서 출발해서 해당 노드까지 도달하는 최단거리를 반환한다.
'''

from collections import defaultdict
from heapq import heappush, heappop
from sys import maxsize

def solution(n, paths, gates, summits):
    gates, summits = set(gates), set(summits)
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
    
    def dijkstra():
        pq = [] # (intensity, 현재 위치)
        memo = [maxsize]*(n+1)
        
        for g in gates:
            heappush(pq, (0, g))
            memo[g] = 0
        
        while pq:
            intensity, node = heappop(pq)
            if node in summits or intensity > memo[node]: # summit이거나 더 큰 intensity라면 이동하지 않음
                continue
            for next_node, next_dist in graph[node]:
                next_intensity = max(intensity, next_dist)
                if next_intensity < memo[next_node]:
                    memo[next_node] = next_intensity
                    heappush(pq, (next_intensity, next_node))
        
        return memo
        
    ans = (0, maxsize)
    memo = dijkstra()
    for s in summits:
        temp = [ans, (s, memo[s])]
        temp.sort(key = lambda x: (x[1], x[0]))
        ans = temp[0]
                
    return ans