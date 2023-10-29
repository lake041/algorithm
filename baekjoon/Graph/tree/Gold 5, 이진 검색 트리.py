# https://www.acmicpc.net/problem/5639
# 전위 순회: 루트 노드보다 큰 원소가 나오는 지점이 왼쪽 서브 트리와 오른쪽 서브 트리를 나누는 지점
# 후위 순회: 마지막 원소 지점이 루트 노드
# 0: 50 // 30 24 5 28 45 // 98 52 60
# 1: 30 // 24 5 28 // 45
# 2: 24 // 5 // 28
# 1: 98 // 52 60
# 트리 순회 시리즈는 가슴으로 와닿을 때까지 그냥 외우자

from sys import stdin
input = stdin.readline

pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break

def post(start, end):
    if start > end:
        return
    # * mid가 end + 1이어야하는 이유
    mid = end
    for i in range(start + 1, end + 1):
        if pre[i] > pre[start]:
            mid = i
            break
    
    # 후위 순회: left -> right -> print
    post(start + 1, mid - 1)
    post(mid, end) # * => 여기서 무한 재귀
    print(pre[start])

post(0, len(pre) - 1)

'''
50
30
24
5
28
45
98
52
60
STOP
'''