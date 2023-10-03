# [start, end] 미사일을 격추했다면, start와 end 사이에 있는 모든 미사일은 격추했다는 의미 => 약간 다름
# 앞에서부터 격추하기 위해 정렬부터 한다

def solution(targets):
    answer = 0
    done = 0
    
    for start, end in sorted(targets):
        if start < done: # 이미 격추된 상태
            # 이전에 격추한 미사일 안에 다른 미사일이 통째로 포함되어 있다면
            # 포함된 미사일 내부를 격추해야하므로
            # done을 그 포함된 미사일 내부로 설정한다
            # 다음에 나올 start가 이전에 격추했던 start, end 사이에 있더라도, 이렇게 되면 새로 격추해야 한다
            done = min(done, end)
        else: # done < start - end 새로운 격추 필요
            done = end
            answer += 1
    
    return answer