from collections import deque

def solution(coin, cards):
    N = len(cards)
    initial = set(cards[:N//3])
    not_yet = deque(cards[N//3:])
    possible = set()

    def update_possible():
        if not_yet:
            possible.add(not_yet.popleft())
            possible.add(not_yet.popleft())

    # source에서 숫자 하나를 고르고, 그 숫자에 맞는 쌍을 target에서 찾습니다.
    # 찾는 데 성공했다면 True를 반환하고, 실패했다면 False를 반환합니다.
    def remove_pair(source: set, target: set) -> bool:
        nonlocal coin, round
        for x in list(source):
            if N+1-x in target:
                source.remove(x)
                target.remove(N+1-x)
                return True
        return False

    round = 0
    while coin or not_yet:
        update_possible()
        if remove_pair(initial, initial):
            round += 1
        elif coin >= 1 and remove_pair(initial, possible):
            coin -= 1
            round += 1
        elif coin >= 2 and remove_pair(possible, possible):
            coin -= 2
            round += 1
        else:
            break

    return round

print(solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]))