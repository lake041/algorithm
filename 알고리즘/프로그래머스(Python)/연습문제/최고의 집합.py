def solution(n, s):
    if s < n:
        return [-1]
    
    quo, rem = divmod(s, n)
    ans = [quo] * (n - rem) + [quo + 1] * rem
    
    return ans