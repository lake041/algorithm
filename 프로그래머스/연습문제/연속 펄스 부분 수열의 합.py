def solution(seq):
    asp = []
    for index, num in enumerate(seq):
        if index%2 == 0:
            asp.append(asp[-1]+num if asp else num)
        else:
            asp.append(asp[-1]-num if asp else -num)
            
    ans = max(
        max(asp),
        -min(asp),
        +max(asp)-min(asp),
        -min(asp)+max(asp)
    )
        
    return ans