# 회문 by 파이썬 문자열 슬라이싱

phrase.find(phrase[::-1])

# 메모리 스왑

a, b = b, a

# 인덱스 9번까지 값 더하기 by 문자열 슬라이싱

sum(list[:9])

# Factorial 생성

reduce(lambda x, y: x \* y, range(1, n+1))

# Fibonacci 생성

lambda x: x if x<=1 else fib(x-1) + fib(x-2)

# 파일 읽기

[line.strip() for line in open(file_name)]

# 주어진 리스트에서 엘리먼트의 값이 -10인 인덱스 반환 하기

list = [1, 2, 3, ... ]

[i for i in range(len(list)) if list [i] == -10]

# 정수 값을 받았을 때, 팰린드롬이 맞는지 bool값으로 확인하는 코드

class Solution:
def isPalindrome(self, x: int) -> bool:
return True if (x >= 0 and str(x) == str(x)[::-1]) else False

# 2차원 리스트에서 최댓값 구하기

ans = max([max(row) for row in list])
