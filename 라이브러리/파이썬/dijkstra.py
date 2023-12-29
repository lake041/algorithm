from collections import defaultdict
from heapq import heappush, heappop
from sys import stdin, maxsize
input = stdin.readline

N, M, D, E = map(int, input().split())
hs = [0] + list(map(int, input().split()))
routes = defaultdict(dict)
for _ in range(M):
    a, b, n = map(int, input().split())
    routes[a].setdefault(b, n)
    routes[b].setdefault(a, n)
    # routes[a].update(b=n)
    # routes[b].update(a=n)
print(routes)

def dijkstra(graph, start):
    # distance: start로부터의 거리값
    distance = {node: maxsize for node in graph}
    # 시작 값은 자기 자신이므로 거리가 0임
    distance[start] = 0
    q = []
    # 가까운 거리부터 탐색하므로 거리 값이 먼저 옴
    heappush(q, (distance[start], start))
    
    while q:
        cur_dist, cur_dest = heappop(q)
        # 기존에 있는 거리보다 현재 거리가 더 길다면 볼 필요도 없음
        if distance[cur_dest] < cur_dist:
            continue
        for new_dest, new_dist in graph[cur_dest].items():
            # 해당 노드를 거쳐 new_dest까지 가는 거리
            dist = cur_dist + new_dist
            # 알고 있는 거리보다 작으면 갱신
            if dist < distance[new_dest]:
                distance[new_dest] = dist
                # 다음 인접 거리를 계산 하기 위해 큐에 삽입
                heappush(q, (dist, new_dest))
    return distance

print(dijkstra(routes, 1))