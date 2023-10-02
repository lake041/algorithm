# https://www.acmicpc.net/problem/14890

from itertools import product
from sys import stdin
input = stdin.readline

N, L = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(N)]
answer = 0

def pre_row(row):
    for i in range(N-1):
        if abs(bod[row][i]-bod[row][i+1]) >= 2:
            return 'impossible'
    return 'possible'
        
def pre_col(col):
    for i in range(N-1):
        if abs(bod[i][col]-bod[i+1][col]) >= 2:
            return 'impossible'
    return 'possible'

def yes():
    global answer
    for row in range(N):
        if pre_row(row) == 'impossible':
            continue
        current_level = bod[row][0]
        check = [False]*N
        possible = True
        # if bod[row] == [1,1,1,2,2,3]:
        #     print(0)
        for col in range(1, N):
            # 높이가 같거나 or 경사로가 설치되어 있거나
            if current_level == bod[row][col] or check[col]==True:
                continue

            # 내리막길 경사로 설치
            if current_level > bod[row][col]:
                for i in range(L):
                    if col+i>=N or bod[row][col+i]!=current_level-1 or check[col+i]==True:
                        possible = False
                        break
                if possible:
                    for i in range(L):
                        check[col+i] = True
                else:
                    break

            # 오르막길 경사로 설치
            if current_level < bod[row][col]:
                for i in range(L):
                    if col-i-1<0 or bod[row][col-i-1]!=current_level or check[col-i-1]==True:
                        possible= False
                        break
                if possible:
                    for i in range(L):
                        check[col-i-1] = True
                else:
                    break
            current_level = bod[row][col]
        if possible:
            answer += 1
            # print(bod[row])

yes()
bod = list(map(list, zip(*bod[::-1])))
yes()
print(answer)