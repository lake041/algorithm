'''
dp[N][T] => onboard[N]까지 만족하면서 온도 T인 최소 전력
dp[N][T] = min(
    dp[N-1][T-1] + plus_cost,
    dp[N-1][T] + maintain_cost,
    dp[N-1][T+1] + minus_cost)
'''

from sys import maxsize

def solution(temperature, t1, t2, a, b, onboard):
    temperature += 10
    t1 += 10
    t2 += 10

    plus_cost = a if temperature < t1 else 0
    minus_cost = 0 if temperature < t1 else a

    dp = [[maxsize]*51 for _ in range(1000)]
    dp[0][temperature] = 0
    
    # temp_min = min(temperature, t1, t2)
    # temp_max = max(temperature, t1, t2)
    
    for i in range(1, len(onboard)):
        client = onboard[i]
        for temp in range(51):
            if client and temp in range(t1, t2+1):
                dp[i][temp] = min(
                    dp[i-1][temp-1] + plus_cost if temp-1 >= 0 else maxsize,
                    dp[i-1][temp]+b if temp!=temperature else dp[i-1][temp],
                    dp[i-1][temp+1] + minus_cost if temp+1 <= 50 else maxsize
                )
            if client and temp not in range(t1, t2+1):
                dp[i][temp] = maxsize
            if not client:
                dp[i][temp] = min(
                    dp[i-1][temp-1] + plus_cost if temp-1 >= 0 else maxsize,
                    dp[i-1][temp]+b if temp!=temperature else dp[i-1][temp],
                    dp[i-1][temp+1] + minus_cost if temp+1 <= 50 else maxsize
                )
    
    answer = 0
    last_index = len(onboard)-1
    if onboard[-1]:
        answer = min([dp[last_index][temp] for temp in range(t1, t2+1)])
    else:
        answer = min([dp[last_index][temp] for temp in range(51)])
    
    return answer