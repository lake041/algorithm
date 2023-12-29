from collections import defaultdict

def convert(num):
    return bin(num)[2:]

def solution(numbers):
    ans = []
    for num in numbers:
        binary = convert(num)

        cnt = 0
        len_ = len(binary)
        while len_ >= 1:
            len_ /= 2
            cnt += 1
        # 문자열 전체 길이 2**cnt - 1 
        L = 2**cnt - 1
        binary = binary.zfill(L)
        
        check = [0]*L
        for level in range(1, cnt+1):
            interval = 2**(level-1)
            start = -1 + interval
            for i in range(start, L, interval):
                check[i] = level
        
        dp = defaultdict(list)
        for index, level in enumerate(check):
            dp[level].append(index)
        
        impossible = False
        for level in range(1, cnt):
            for i in range(0, len(dp[level]), 2):
                child1_index, child2_index = dp[level][i], dp[level][i+1]
                child1, child2 = map(int, (binary[child1_index], binary[child2_index]))
                parent_index = dp[level+1][i//2]
                parent = int(binary[parent_index])
                if (child1 or child2) and (not parent):
                    impossible = True
                    break
            if impossible:
                break
        if num == 5:
            return child1, child2, parent
        
        ans.append(0 if impossible else 1)
        
        
    return ans