def solution(n, left, right):
    return [max(num//n, num%n)+1 for num in range(left, right+1)]
