from collections import deque, defaultdict

def D(N):
    return (N*2) % 10000
def S(N):
    return (N-1) % 10000
def L(N):
    return (N*10 + N//1000) % 10000
def R(N):
    return ((N%10)*1000 + N//10) % 10000

df = [D, S, L, R]
ds = ["D", "S", "L", "R"]

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())

    q = deque([(A, "")])
    visited = defaultdict(bool)
    visited[A] = True

    while q:
        num, string = q.popleft()        
        if num == B:
            print(string)
            break

        for f, s in zip(df, ds):
            next = f(num)
            if not visited[next]:
                q.append((next, string+s))
                visited[next] = True