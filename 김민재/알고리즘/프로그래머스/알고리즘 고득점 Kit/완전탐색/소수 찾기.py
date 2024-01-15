from math import floor
from itertools import permutations

def is_prime(num):
    if num in (0, 1):
        return False
    for i in range(2, floor(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    prime = set()
    
    for l in range(1, len(numbers)+1):
        for k in permutations(numbers, l):
            k = int(''.join(k))
            if is_prime(k):
                prime.add(k)
    
    return len(prime)