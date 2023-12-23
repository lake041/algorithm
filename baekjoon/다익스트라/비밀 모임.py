from sys import stdin, maxsize
from heapq import heappop, heappush
input = stdin.readline

def dijkstra(start, graph, N):
    distance = [maxsize]*(N+1)
    distance[start] = 0

    q = []
    heappush(q, (distance[start], start))
    while q:
        acc_dist, stopover = heappop(q)
        if distance[stopover] < acc_dist:
            continue
        for next_node, plus_dist in graph[stopover]:
            new_dist = acc_dist + plus_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(q, (distance[next_node], next_node))

    return distance

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    _ = int(input())
    friends = list(map(int, input().split()))

    min_dist, room = maxsize, maxsize
    for start in range(1, N+1):
        distance = dijkstra(start, graph, N)
        dist_sum = sum([distance[end] for end in friends])
        if dist_sum < min_dist:
            min_dist = dist_sum
            room = start
        if dist_sum == min_dist:
            room = min(room, start)

    print(room)