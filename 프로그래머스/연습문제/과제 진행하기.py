from collections import deque

def solution(input_plans):
    plans = []
    for plan in input_plans:
        hour, minute = int(plan[1][0:2]), int(plan[1][3:5])
        plans.append([plan[0], 60*hour+minute, int(plan[2])])
    plans.sort(key = lambda x: x[1])
    plans = deque(plans)

    answer = []
    stops = []
    
    time = 0
    while True:
        if not plans and not stops:
            break
        
        if not plans:
            done = stops.pop()
            answer.append(done[0])
            continue
        
        next_new_time = plans[0][1]
        if time < next_new_time:
            if stops:
                item = stops.pop()
                item[2] -= 1
                if item[2] == 0:
                    answer.append(item[0])
                else:
                    stops.append(item)
        
        if time == next_new_time:
            item = plans.popleft()
            item[2] -= 1
            if item[2] == 0:
                answer.append(item[0])
            else:
                stops.append(item)
        
        time += 1
    
    return answer