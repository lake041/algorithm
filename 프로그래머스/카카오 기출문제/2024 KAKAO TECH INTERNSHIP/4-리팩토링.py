from collections import deque

def solution(coin, cards):
    N = len(cards)
    my_cards = set(cards[:N//3])
    not_yet = deque(cards[N//3:])
    possible = set()
    round = 0
    round_end = False

    def update_possible() -> bool:
        '''
        not_yet이 비어있다면 모든 라운드가 끝났다는 의미에서 True를 반환하고,
        not_yet이 존재한다면 아직 끝나지 않았다는 의미에서 False를 반환합니다.
        '''
        if not_yet:
            possible.add(not_yet.popleft())
            possible.add(not_yet.popleft())
            return False
        else:
            return True

    def remove_pair(source: set, target: set) -> bool:
        '''
        source에서 숫자 하나를 고르고, 그 숫자에 맞는 쌍을 target에서 찾습니다.
        찾는 데 성공했다면 True를 반환하고, 실패했다면 False를 반환합니다.
        '''
        nonlocal coin, round, round_end
        for x in list(source):
            if N+1-x in target:
                source.remove(x)
                target.remove(N+1-x)
                round_end = update_possible()
                round += 1 if not round_end else 0
                return True
        return False

    while coin and not round_end:
        if remove_pair(my_cards, my_cards):
            continue

        if coin >= 1 and remove_pair(my_cards, possible):
            continue

        if coin >= 2 and remove_pair(possible, possible):
            continue
        else:
            break

    return round