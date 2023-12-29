def solution(citations):
    citations.sort()
    memo = []
    
    L = len(citations)
    for i in range(L):
        memo.append(min(L-i, citations[i]))
    
    return max(memo)