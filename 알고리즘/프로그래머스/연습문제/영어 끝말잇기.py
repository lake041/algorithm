def solution(n, words):
    visited = set()
    last = words[0][0]
    
    for index, word in enumerate(words):
        if word[0] != last or word in visited:
            return [index%n + 1, index//n + 1]
        visited.add(word)
        last = word[-1]
    
    return [0, 0]