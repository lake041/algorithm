def solution(n):
    return len([k for k in range(1, n+1) if (n-k*(k-1)/2)>=1 and (n-k*(k-1)/2)%k==0])