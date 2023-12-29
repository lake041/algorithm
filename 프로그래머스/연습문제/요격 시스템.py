# [start, end] 미사일을 격추했다면, start와 end 사이에 있는 모든 미사일은 격추했다는 의미
# 앞에서부터 격추하기 위해 정렬부터 한다

def solution(targets):
    answer = 0
    done = 0
    
    for start, end in sorted(targets):
        if start < done: # 이미 격추된 상태
            done = min(done, end)
        else: # done < start - end 새로운 격추 필요
            done = end
            answer += 1
    
    return answer