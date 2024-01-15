def find_group(index, cards):
    group = [index]
    while cards[index]>=0 and cards[index] not in group:
        index = cards[index]
        group.append(index)
    
    for member in group:
        cards[member] = -1

    return group, cards

def solution(cards):
    cards = [x-1 for x in cards]
    groups = []
    
    for index in cards:
        if index == -1:
            continue
        group, cards = find_group(index, cards)
        groups.append(group)
    
    groups.sort(key = lambda x: -len(x))
    
    return len(groups[0]) * len(groups[1]) if len(groups) != 1 else 0