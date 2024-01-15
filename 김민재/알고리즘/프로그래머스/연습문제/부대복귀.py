from heapq import heappush, heappop
from sys import maxsize

def solution(N, roads, sources, destination):
    graph = [[] for _ in range(N+1)]
    for i, j in roads:
        graph[i].append(j)
        graph[j].append(i)

    def dijkstra(start):
        memo = [maxsize]*(N+1)
        memo[start] = 0

        q = []
        heappush(q, (memo[start], start))
        while q:
            acc_dist, stopover = heappop(q)
            if memo[stopover] < acc_dist:
                continue
            for next_dest in graph[stopover]:
                new_dist = acc_dist + 1
                if new_dist < memo[next_dest]:
                    memo[next_dest] = new_dist
                    heappush(q, (memo[next_dest], next_dest))
        
        memo = [num if num!=maxsize else -1 for num in memo]
        
        return memo
    
    memo = dijkstra(destination)
    result = []
    for end in sources:
        result.append(memo[end])
    
    return result