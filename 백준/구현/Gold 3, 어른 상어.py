# https://www.acmicpc.net/problem/19237

from itertools import product
from sys import stdin
input = stdin.readline

N, M, FULLTIME = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(N)]
directions = [int(x)-1 for x in input().split()]
priorities = [[[int(x)-1 for x in input().split()] for _ in range(4)] for _ in range(M)]

# 상 하 좌 우
# 0 1 2 3
# 각 칸의 정보: 상어번호 / 상어방향 / 냄새번호 / 남은시간

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def shark_move(num, dir, odor, time, row, col):
    priority = priorities[num]
    found = False
    # 빈칸을 찾음, 상어랑 경쟁을 해야하니 일단 냄새는 남기지 않는다.
    for i in range(4):
        ny = row + dy[priority[dir][i]]
        nx = col + dx[priority[dir][i]]
        if 0<=ny<N and 0<=nx<N:
            # 냄새가 없는 칸 발견
            if bod[ny][nx][2] == -1:
                found = True
                # 상어가 있을 수도 없을 수도 하지만 아무튼 내가 이김
                if num < bod[ny][nx][0]:
                    bod[ny][nx] = [num, priority[dir][i], -1, FULLTIME]
                    bod[row][col] = [777, -1, odor, time]
                # 상어가 있는데 내가 져서 쫓겨남
                else:
                    bod[row][col] = [777, -1, odor, time]
                break
    # 길 찾았으니 return
    if found:
        return
    # 냄새가 없는 칸이 없네, 내 칸으로 돌아가야지
    for i in range(4):
        ny = row + dy[priority[dir][i]]
        nx = col + dx[priority[dir][i]]
        if 0<=ny<N and 0<=nx<N:
            # 자기 냄새인 칸 발견
            if bod[ny][nx][2] == odor:
                bod[ny][nx] = [num, priority[dir][i], odor, FULLTIME]
                bod[row][col] = [777, -1, odor, time]
                break

def odor_check():
    number_of_shark = 0
    for row, col in product(range(N), repeat=2):
        # 상어가 있다
        if 400 >= bod[row][col][0] >= 0:
            number_of_shark += 1
            bod[row][col] = [bod[row][col][0], bod[row][col][1], bod[row][col][0], FULLTIME]
        # 상어가 없다 근데 향기는 있다
        elif bod[row][col][2] >= 0:
            bod[row][col][3] -= 1
            # TIMEOUT
            if bod[row][col][3] == 0:
                bod[row][col] = [777, -1, -1, -1]
    return number_of_shark

for row, col in product(range(N), repeat=2):
    s = bod[row][col]
    # 빈칸
    if s == 0:
        bod[row][col] = [777, -1, -1, -1]
    else:
        bod[row][col] = [s-1, directions[s-1], s-1, FULLTIME]

# for row in bod:
#     print(row)
# print()

# 상어만 먼저 옮기기
# 겹친다면 숫자가 큰 쪽으로 덮어 씌우기
answer = 0
seq = 1
while True:
    seq += 1
    check = [False]*M
    for row, col in product(range(N), repeat=2):
        num, dir, odor, time = bod[row][col]
        if num == 777:
            continue
        if not check[num]:
            check[num] = True
            shark_move(num, dir, odor, time, row, col)
    number_of_shark = odor_check()

    answer += 1
    if number_of_shark == 1:
        print(answer)
        break
    if answer >= 1000:
        print(-1)
        break

    # print(f'number: {seq}')
    # for row in bod:
    #     print(row)
    # print()
    # if seq == 30:
    #     break

'''
5 4 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3
'''
# ans = 14

'''
5 8 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 6 0 7 0
0 0 5 0 8
4 4 3 1 4 2 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
4 1 2 3
1 3 4 2
2 4 3 1
1 2 4 3
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
'''
# ans = 30