# 어렵다...
# 복습 및 주입식 마인드셋 장착 필요

# 탐색의 대상이 되는 변수를 어떤 것으로 둘 것인가
# 비정상적으로 큰 범위 => 어라? 의심해보자
# 바위 사이의 간격을 변수로 둔다면,
# 최소 간격이 1,000,000,000이 되도록 모두 제거 => 50,000번
# 최소 간격이 500,000,000이 되도록 모두 제거 => 50,000번

# 2^30 ~= 1,000,000,000
# 30 x 50,000 = 1,500,000
# 시간복잡도 가능

def solution(distance, rocks, n):
    rocks.sort()
    rocks += [distance]
    
    ans = 0
    left, right = 1, distance
    while left <= right:
        mid = (left + right)//2
        
        # 각 바위 사이의 거리가 mid 이상이 되도록
        cnt = 0
        prev = 0
        for now in rocks:
            if now - prev < mid:
                cnt += 1
            else:
                prev = now
        
        # 간격이 너무 넓음, 좁혀야됨
        if cnt > n:
            right = mid - 1
        # 간격이 좁거나, 적절함. 더 넓혀볼 여지가 있음.
        else:
            ans = mid
            left = mid + 1
    return ans