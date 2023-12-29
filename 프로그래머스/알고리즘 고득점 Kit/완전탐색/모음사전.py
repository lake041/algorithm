from itertools import product

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U', '']
    words = set()    
    for a, b, c, d, e  in product(vowels, repeat=5):
        words.add(''.join([a, b, c, d, e]))
    words = sorted(list(words))

    return words.index(word)