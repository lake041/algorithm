from sys import stdin, maxsize
input = stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = maxsize

def go(index, x, y, first, second):
    global ans
    if index == n:
        ans = min(ans, abs(x-y))
        return
    go(index+1, x + sum(board[index][i] + board[i][index] for i in first), y, first+[index], second)
    go(index+1, x, y + sum(board[index][i] + board[i][index] for i in second), first, second+[index])

go(0, 0, 0, [], [])
print(ans)