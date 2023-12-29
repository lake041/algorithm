from collections import deque

def convert(num):
    memo = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    return str(num) if num <= 9 else memo[num]

def new_jeans(num, n):
    string = deque()
    
    while True:
        string.appendleft(convert(num%n))
        num //= n
        if num == 0:
            break
            
    return ''.join(list(string))

def solution(n, t, m, p):
    string = ''
    length = 0
    i = 0

    while length < t*m:
        string += new_jeans(i, n)
        length = len(string)
        i += 1

    return ''.join([string[j*m+p-1] for j in range(t)])