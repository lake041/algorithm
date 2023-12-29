from itertools import combinations, product

def combi_to_str(index_combination):
    return ' '.join(list(map(str, index_combination)))

def solution(dices):
    dp = {}
    L = len(dices)
    for index_combination in combinations(range(L), L//2):
        dp[combi_to_str(index_combination)] = 0
    
    combi_list = list(combinations(range(L), L//2))

    for roll_product in product(range(6), repeat=L):
        for index_combination in combi_list:
            hap1 = sum(dices[i][roll_product[i]] for i in index_combination)
            hap2 = sum(dices[j][roll_product[j]] for j in range(L) if j not in index_combination)
            if hap1 > hap2:
                dp[combi_to_str(index_combination)] += 1
    
    dp = list(dp.items())
    dp.sort(key = lambda x: -x[1])
    ans = list(map(lambda x: int(x)+1, dp[0][0].split()))

    return ans