def solution(order):
    order = order[::-1]
    temp = []
    ans = 0

    end = len(order)
    for cur in range(1, end+1):
        if cur == order[-1]:
            ans += 1
            order.pop()
        else:
            temp.append(cur)
        
        while temp and temp[-1] == order[-1]:
            ans += 1
            temp.pop()
            order.pop()
    
    return ans