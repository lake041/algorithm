from itertools import combinations, product
# from bisect import bisect_left

def solution(dices):
    dp = {}
    L = len(dices)
    for A_index_combi in combinations(range(L), L//2):
        B_index_combi = [i for i in range(L) if i not in A_index_combi]
        A, B = [], []
        
        for order_product in product(range(6), repeat=L//2):
            for i, j in zip(A_index_combi, order_product):
                A.append(dices[i][j])
            for i, j in zip(B_index_combi, order_product):
                B.append(dices[i][j])        
        B.sort()

        wins = 0
        # for num in A:
        #     wins += bisect_left(B, num)

        # for num in A:
        #     left, right = 0, L//2-1
        #     while left <= right:
        #         mid = (left + right)//2
        #         if num <= B[mid]:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     wins += left

        dp[wins] = list(A_index_combi)
    
    max_key = max(dp.keys())

    return dp[max_key]