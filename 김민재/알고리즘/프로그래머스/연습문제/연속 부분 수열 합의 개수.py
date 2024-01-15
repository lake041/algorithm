def solution(elements):
    len_ = len(elements)
    elements += elements

    hap = set()
    memo = [[0]*(len_*2+1) for _ in range(len_+1)]
    for index in range(0, len_):
        hap.add(elements[index])
        memo[index][index+1] = elements[index]

    for start in range(0, len_):
        for length in range(2, len_+1):
            end = start + length
            hap.add(memo[start][end-1] + elements[end-1])
            memo[start][end] = memo[start][end-1] + elements[end-1]
            
    return len(hap)