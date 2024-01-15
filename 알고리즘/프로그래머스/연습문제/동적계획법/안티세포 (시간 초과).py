from sys import setrecursionlimit
setrecursionlimit(10**8)

def solution(a, s):
    start = 0
    ans = []
    for length in s:
        b = a[start:start+length]
        start = start+length
        
        L = len(b)
        # [leftmost, sum]
        dp = [[index, num] for index, num in enumerate(b)]
        c = 0
        
        def go(index):
            nonlocal c
            if index == L:
                c += 1
                return
            
            X = dp[index]
            if dp[index][0] > 0:
                Y = dp[dp[index][0]-1]
                if X[1] == Y[1]:
                    [a, b] = dp[index]
                    X[0] = Y[0]
                    X[1] += Y[1]
                    go(index)
                    dp[index] = [a, b]
            go(index+1)
        
        go(0)
        ans.append(c)

    return ans