N = int(input())
P = list(map(int, input().split()))

# 오래 고민하다가 결국 구글링했다.
# 코드는 간단했지만 직관적인 이해는 쉽지 않았다.
# 이 풀이가 성립하는 이유는, 같은 길이의 시퀀스를 추출할 때 min(left, right)가 항상 최대가 되는 최적의 루트로 나아가기 때문이다.

left, right = 0, N-1
MAX = 0
while left <= right:
    MAX = max(MAX, min(P[left], P[right]) * (right-left-1))
    if P[left] <= P[right]:
        left += 1
    else:
        right -= 1

print(MAX)