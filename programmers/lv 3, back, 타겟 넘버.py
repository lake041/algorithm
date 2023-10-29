def solution(numbers, target):
    answer = 0
    def back(index, now):
        nonlocal answer
        nonlocal target
        if index==len(numbers):
            if now==target:
                answer += 1
            return
        back(index+1, now-numbers[index])
        back(index+1, now+numbers[index])
    
    back(1, numbers[0])
    back(1, -numbers[0])
    
    return answer