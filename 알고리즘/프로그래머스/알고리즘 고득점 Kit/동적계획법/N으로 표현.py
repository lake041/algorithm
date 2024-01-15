def solution(N, number):
    dp = {1:[N, -N]}
    
    index = 2
    while True:
        if index == 9:
            break
        dp[index] = set()
        
        for num in dp[index-1]:
            dp[index].add(int(str(N)*index))
            dp[index].add(num+N)
            dp[index].add(num-N)
            dp[index].add(N-num)
            dp[index].add(num*N)
            dp[index].add(num//N)
            if num != 0:
                dp[index].add(N//num)

        
        for i in range(1, index):
            for x in dp[i]:
                for y in dp[index-i]:
                    dp[index].add(x+y)
                    dp[index].add(x-y)
                    dp[index].add(y-x)
                    dp[index].add(x*y)
                    if x != 0:
                        dp[index].add(y//x)
                    if y != 0:
                        dp[index].add(x//y)
                    
        index += 1
    
    for index in range(1, 9):
        if number in dp[index]:
            return index
    return -1