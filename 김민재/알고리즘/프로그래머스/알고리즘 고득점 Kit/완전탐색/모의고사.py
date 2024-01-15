def solution(answers):
    answer = []
    one, two, three = 0, 0, 0
    
    o1 = {0:1, 1:2, 2:3, 3:4, 4:5}
    o2 = {0:2, 1:1, 2:2, 3:3, 4:2, 5:4, 6:2, 7:5}
    o3 = {0:3, 1:3, 2:1, 3:1, 4:2, 5:2, 6:4, 7:4, 8:5, 9:5}
    
    for i in range(len(answers)):
        one += 1 if o1[i%5]==answers[i] else 0
        two += 1 if o2[i%8]==answers[i] else 0
        three += 1 if o3[i%10]==answers[i] else 0
    
    max_value = max(one, two, three)
    if one==max_value:
        answer.append(1)
    if two==max_value:
        answer.append(2)    
    if three==max_value:
        answer.append(3)    
    
    return answer