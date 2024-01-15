# https://www.acmicpc.net/problem/10775

G = int(input())
P = int(input())

ports = list(range(G+1))
planes = [int(input()) for _ in range(P)]

def union(x, y): 
    x_root = find_root(x)
    y_root = find_root(y)

    if x_root < y_root:
        ports[y_root] = x_root
    if y_root < x_root:
        ports[x_root] = y_root

def find_root(plane):
    if ports[plane] == plane:
        return plane

    ports[plane] = find_root(ports[plane])
    return ports[plane]

ans = 0
for plane in planes:
    empty_port = find_root(plane)
    if not empty_port:
        break
    union(empty_port, empty_port-1)
    ans += 1
print(ans)