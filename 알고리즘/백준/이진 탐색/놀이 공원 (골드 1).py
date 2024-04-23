N, M = map(int, input().split())
rides = list(map(int, input().split()))

# 운행 시간이 k인 놀이기구가 t분 이전까지 태울 수 있는 승객 수 = (t-1)//k + 1
def prev_passengers(t):
    return sum((t-1)//ride + 1 for ride in rides)

def available_rides(t):
    return [index+1 for index, ride in enumerate(rides) if t % ride == 0]

# 범위를 충분히 크게 주지 않았다.
left, right = 0, 2_000_000_000_000
while left <= right:
    mid = (left + right) // 2
    available_index = available_rides(mid)
    prev_total = prev_passengers(mid)
    
    if prev_total < N and N <= prev_total + len(available_index):
        remain = N - prev_total
        print(available_index[remain-1])
        break    
    elif N <= prev_total:
        right = mid - 1
    elif prev_total + len(available_index) < N:
        left = mid + 1