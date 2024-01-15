# 1. 막풀이, 생각 안 나서 일단 마구잡이로 풀고 시간 초과.
'''
def solution(prices):
    L = len(prices)
    for i in range(L):
        prices[i] = [prices[i], 0, False]
    
    for i in range(L):
        current_price = prices[i][0]
        for j in range(i):
            if prices[j][2]:
                continue
            if prices[j][0] <= current_price:
                prices[j][1] += 1
            else:
                prices[j][1] += 1
                prices[j][2] = True
    answer = [prices[i][1] for i in range(L)]
    return answer
'''

# 2. 스택을 활용한 풀이
def solution(prices):
    stack = []
    L = len(prices)
    answer = [0]*L

    for i in range(L):
        if not stack:
            stack.append((prices[i], i))
            continue
        
        current_price = prices[i]
        while True:
            if not stack or stack[-1][0] <= current_price:
                break
            _, past_index = stack.pop()
            answer[past_index] = i - past_index
        stack.append((prices[i], i))
    
    for _, index in stack:
        answer[index] = L - index - 1
            
    return answer

