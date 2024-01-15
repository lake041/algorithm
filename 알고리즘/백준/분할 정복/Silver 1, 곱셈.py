from sys import stdin
input = stdin.readline

def func(A, B):
    if B == 1:
        return A % C
    if B % 2 == 1:
        return func(A, (B//2))**2 * A % C
    if B % 2 == 0:
        return func(A, (B//2))**2 % C

A, B, C = map(int, input().split())
print(func(A, B))