from sys import maxsize

def solution(routes):
    routes.sort(key = lambda x: x[1])
    cnt = 0
    
    done = -maxsize
    for start, end in routes:
        if start <= done:
            continue
        else:
            done = end
            cnt += 1

    return cnt