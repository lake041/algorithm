def solution(scores):
    ta, tb = scores[0]
    ts = ta + tb

    scores.sort(key = lambda x: (-x[0], x[1]))
    
    rank = 1
    max_b = 0
    for a, b in scores:
        if ta < a and tb < b:
            return -1
        
        if max_b <= b:
            max_b = b
            if a + b > ts:
                rank += 1
            
    return rank