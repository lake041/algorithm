from itertools import product

def solution(users, emoticons):
    L = len(emoticons)
    ans = [0, 0] # 가입자 수, 매출액
    for rates in product([10, 20, 30, 40], repeat=L):
        temp = [0, 0]
        for user_rate, user_max in users:
            user_sum = 0
            for i in range(L):
                if user_rate <= rates[i]:
                    user_sum += emoticons[i]*(100-rates[i])/100
            if user_max <= user_sum:
                temp[0] += 1
            else:
                temp[1] += user_sum
        ans = max(ans, temp)

    return ans