# 그러니까 제일 먼저 드는 생각은, 하나씩 다 해보면 안 되나?
# 모든 선수를 각각 1팀과 2팀에 보내서 총 2^20개의 경우의 수를 모두 구하고
# 각각의 경우에 대해서 선수의 수가 같은지 유효성을 검사하고
# 다시 그때의 팀 능력치 차이를 계산해서
# 최솟값을 갱신해나가는 방향으로 브루트 포스를 진행한다.

# 복잡하게, 그룹을 나누고 여기서 빠졌으니 이제 이건 뭐고, 저건 뭐다 식의
# 지나치게 논리적이고 구조화 된 사고방식은
# 컴퓨터 알고리즘 구현에 있어서 그렇게 효과적인 방법이 아닌 것 같다.
# 내가 여기서 습득해야 되는 것은, 그런 복잡한 구조의 논리를 구현하는 방법이 아니라
# 논리는 간단하되, 그 논리를 구현하는 재귀의 정확한 문법이다.

# index, 어느 팀으로 보낼지 결정하는 선수의 번호
# 1. index 선수를 우선 팀을 나누고
# 2. 그 팀이 유효한지 검사하고
# 3. global ans와 팀 간의 differ를 비교한다.

import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 2000000000

def go(index, x, y, first, second):
    global ans
    if index == n:
        ans = min(ans, abs(x-y))
        return
    go(index+1, x + sum(board[index][i] + board[i][index] for i in first), y, first+[index], second)
    go(index+1, x, y + sum(board[index][i] + board[i][index] for i in second), first, second+[index])

go(0, 0, 0, [], [])
print(ans)