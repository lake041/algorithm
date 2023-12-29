from math import gcd
from functools import reduce

def find_gcd(array):
    return reduce(gcd, array)
    
def cannot_divide(array, divisor):
    return all(dividend % divisor != 0 for dividend in array)

def solution(arrayA, arrayB):
    GCD_A = find_gcd(arrayA)
    GCD_B = find_gcd(arrayB)

    ans = []
    if cannot_divide(arrayB, GCD_A):
        ans.append(GCD_A)
    if cannot_divide(arrayA, GCD_B):
        ans.append(GCD_B)
        
    return max(ans) if ans else 0