T = int(input())

def is_shortest(diff, k):
    if k % 2 == 0:
        left = (1 + ((k-1)//2 + 1)) * ((k-1)//2 + 1) - ((k-1)//2 + 1)
        right = (1 + k//2) * k//2
    else:
        left = (1 + (k-1)//2) * (k-1)//2
        right = (1 + (k//2 + 1)) * (k//2 + 1) - (k//2 + 1)
    
    if diff <= left:
        return -1
    elif left < diff <= right:
        return 0
    elif right < diff:
        return 1

for _ in range(T):
    x, y = map(int, input().split())
    diff = y - x

    left, right = 0, 2**31
    while left <= right:
        mid = (left + right) // 2
        result = is_shortest(diff, mid)

        if result == -1:
            right = mid - 1
        elif result == 0:
            break
        elif result == 1:
            left = mid + 1
    
    print(mid) 