def solution(clothes):
    answer = 0
    dic = {}
    temp = []
    for cloth in clothes:
        if cloth[1] in dic:
            dic[cloth[1]] += 1
        else:
            dic[cloth[1]] = 1
            temp.append(cloth[1])
    answer = 1
    for x in temp:
        answer *= (dic[x]+1)
    answer -= 1
    return answer