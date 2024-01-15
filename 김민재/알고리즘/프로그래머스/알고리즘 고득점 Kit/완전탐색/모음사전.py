def solution(word):
    M = ['A', 'E', 'I', 'O', 'U', '']
    words = set()
    
    for i1 in range(6):
        for i2 in range(6):
            for i3 in range(6):
                for i4 in range(6):
                    for i5 in range(6):
                        words.add(''.join([M[i1], M[i2], M[i3], M[i4], M[i5]]))

    # "" 제거하지 않음
    words = list(words)
    words.sort()

    return words.index(word)