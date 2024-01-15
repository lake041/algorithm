from functools import reduce
from heapq import heappop, heappush

string = "abcba"
print(f'팰린드롬 판단:\t', string == string[::-1])

a, b = 1, 2
a, b = b, a
print(f'메모리 스왑:\t', a, b)

factorial = lambda N: reduce(lambda x, y: x * y, range(1, N + 1), 1)
print(f'팩토리얼 계산:\t', factorial(10))

fib = lambda x: x if x <= 1 else fib(x - 1) + fib(x - 2)
print(f'피보나치 계산:\t', fib(10))

bod = [[0, 1], [2, 3]]
print(f'2차원 최댓값:\t', max(max(row) for row in bod))

c = [0, 1, 2, 3, 4]
print(f'제너레이터 표현식 응용', sum(heappush(c, x := heappop(c) + heappop(c)) or x for _ in c[1:]))
