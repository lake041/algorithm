def leftmost(seq, target):
    left, right = 0, len(seq)

    while left <= right:
        mid = (left + right) // 2
        if seq[mid] >= target:
            # result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return left

def rightmost(seq, target):
    left, right = 0, len(seq)

    while left <= right:
        mid = (left + right) // 2
        if seq[mid] <= target:
            # result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return left

seq = [1, 2, 3, 4, 5, 5, 5, 5, 5, 10]

print(rightmost(seq, 5))    # 8 최대한 오른쪽
print(leftmost(seq, 5))     # 4 최대한 왼쪽

print(rightmost(seq, 5.5))  # 8
print(leftmost(seq, 5.5))   # 9 들어갈 위치

print(rightmost(seq, 4.5))  # 3
print(leftmost(seq, 4.5))   # 4 들어갈 위치

# 무조건 left 반환
# leftmost는 들어갈 위치, 존재한다면 제일 왼쪽 인덱스
# rightmost는 들어갈 위치, 존재한다면 제일 오른쪽 인덱스 + 1

# right 반환하면, 존재한다면 그 인덱스를 반환한다.