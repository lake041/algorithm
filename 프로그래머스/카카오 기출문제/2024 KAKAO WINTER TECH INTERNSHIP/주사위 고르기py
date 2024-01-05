from itertools import combinations, product
from bisect import bisect_left

def solution(dices):
    dp = {}

    L = len(dices)
    for A_index_combi in combinations(range(L), L//2):
        B_index_combi = [i for i in range(L) if i not in A_index_combi]

        A, B = [], []
        for order_product in product(range(6), repeat=L//2):
            A.append(sum(dices[i][j] for i, j in zip(A_index_combi, order_product)))
            B.append(sum(dices[i][j] for i, j in zip(B_index_combi, order_product)))
        B.sort()

        wins = sum(bisect_left(B, num) for num in A)
        dp[wins] = list(A_index_combi)

    max_key = max(dp.keys())

    return [x+1 for x in dp[max_key]]