# O(N^2 / 2)

def solution(numbers):
    answer = [-1] * len(numbers)
    for idx, num in enumerate(numbers):
        for next_idx in range(idx+1, len(numbers)):
            if num < numbers[next_idx]:
                answer[idx] = numbers[next_idx]
                break
    return answer
