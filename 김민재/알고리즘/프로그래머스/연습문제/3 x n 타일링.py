def solution(n):
    DP = {2: 3, 4: 11}
    SUM = {2: 3, 4: 14}
    
    for i in range(2, n+2, 2):
        if i in DP:
            continue
        DP[i] = ( DP[i-2]*3 + SUM[i-4]*2 + 2) % 1_000_000_007
        SUM[i] = ( SUM[i-2] + DP[i] ) % 1_000_000_007
    
    return DP[n] if n in DP else 0