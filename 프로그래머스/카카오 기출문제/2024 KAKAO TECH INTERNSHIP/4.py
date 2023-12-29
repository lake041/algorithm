from collections import deque

def solution(coin, cards):
    N = len(cards)
    my = set(cards[:N//3])
    not_yet = cards[N//3:]
    not_yet = deque(not_yet)
    possible = set()
    if not_yet:
        possible.add(not_yet.popleft())
        possible.add(not_yet.popleft())
    round = 0

    for x in list(my):
        if N+1-x in my:
            my.remove(x)
            my.remove(N+1-x)
            if not_yet:
                possible.add(not_yet.popleft())
                possible.add(not_yet.popleft())
            round += 1
    
    cnt = 0
    end = False
    while coin and not end:
        # cnt += 1
        # if cnt ==3:
        #     return round, list(my), list(possible), list(not_yet)

        ok = False
        for x in list(my):
            if N+1-x in possible:
                my.remove(x)
                possible.remove(N+1-x)
                coin -= 1
                if not_yet:
                    possible.add(not_yet.popleft())
                    possible.add(not_yet.popleft())
                else:
                    end = True
                round += 1
                ok = True
                break
        if ok:
            continue
        
        if coin < 2:
            break

        for x in possible:
            if N+1-x in possible:
                possible.remove(x)
                possible.remove(N+1-x)
                coin -= 2
                if not_yet:
                    possible.add(not_yet.popleft())
                    possible.add(not_yet.popleft())
                else:
                    end = True
                round += 1
                ok = True
                break
        if ok:
            continue
        else:
            break



    # return list(my), list(possible), list(not_yet)

    return round+1