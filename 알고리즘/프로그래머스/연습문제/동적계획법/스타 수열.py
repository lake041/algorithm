def solution(a):
    L = len(a)
    memo = [[-1, 0] for _ in range(L)]
    for index, num in enumerate(a):
        if index == 0 and L >= 2 and a[index] != a[index+1]:
            memo[num][0] = index+1
            memo[num][1] += 2
        elif memo[num][0] + 1 == index and index + 1 < L and a[index] != a[index+1]:
            memo[num][0] = index + 1
            memo[num][1] += 2
        elif memo[num][0] + 1 < index:
            if a[index-1] != a[index]:
                memo[num][0] = index
                memo[num][1] += 2
            elif index + 1 < L and a[index] != a[index+1]: 
                memo[num][0] = index + 1
                memo[num][1] += 2

    return max(memo[num][1] for num in range(L))
