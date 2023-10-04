from sys import stdin
input = stdin.readline

def cal(now, next):
    if now == 0:
        return 2

    diff = abs(now - next)
    if diff == 0:
        return 1
    elif diff == 2:
        return 4
    else:
        return 3

order = [int(x) for x in input().split() if x != '0']
memo = []
start = order[0]
memo.append({(start, 0): 2, (0, start): 2})
for i in range(1, len(order)):
    next = order[i]
    temp = {}
    for left, right in memo[i-1].keys():
        sum = memo[i-1][(left, right)]
        if (next, right) in temp:
            temp[(next, right)] = min(temp[(next, right)], sum+cal(left, next))
        else:
            temp[(next, right)] = sum+cal(left, next)

        if (left, next) in temp:
            temp[(left, next)] = min(temp[(left, next)], sum+cal(right, next))
        else:
            temp[(left, next)] = sum+cal(right, next)
    memo.append(temp)
print(min(memo[-1].values()))