def solution(n, a, b):
    answer = 1
    A, B = A - 1, B - 1   
    while a // 2 != b // 2:        
        A //= 2        
        B //= 2        
        answer += 1
        
    return answer
