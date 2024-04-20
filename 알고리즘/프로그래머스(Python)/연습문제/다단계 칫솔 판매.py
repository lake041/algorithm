from collections import defaultdict

def share_money(name, money, g):
    shares = {}
    now = name
    up = 1
    
    while up and now != "-":
        up = int(money * 0.1)
        shares[now] = money - up
        money = up
        now = g[now]
    
    return shares

def solution(enroll, referral, seller, amount):
    g = {}
    i = {}
    for index, name in enumerate(enroll):
        g[name] = referral[index]
        i[name] = index
        
    ans = [0]*len(enroll)
    for index, name in enumerate(seller):
        money = amount[index] * 100
        shares = share_money(name, money, g)
        
        for key in shares:
            if key == "-":
                continue
            ind = i[key]
            ans[ind] += shares[key]
        
    return ans