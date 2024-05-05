'''
재귀 함수에서 중요한 부분은 Base Case를 설정하는 것이다.
재귀 호출이 무한으로 계속되지 않도록 중단 조건을 제공한다.
'''

def combinations(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        rest_arr = arr[i + 1:]
        for C in combinations(rest_arr, n - 1):
            result.append([elem] + C)
    
    return result

def permutations(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        rest_arr = arr[:i] + arr[i + 1:]
        for P in permutations(rest_arr, n - 1):
            result.append([elem] + P)
    
    return result

for combi in combinations(range(3), 4):
    print(combi)

def custom_combi(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        element = arr[i]
        rest_arr = arr[i+1:]
        for C in custom_combi(rest_arr, n-1):
            result.append([element] + C)
    
    return result

print(len(list(custom_combi(range(10), 3))))