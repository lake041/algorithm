from collections import defaultdict

def solution(cacheSize, cities):
    recent = defaultdict(int)
    cities = [city.lower() for city in cities]
    cache = []
    ans = 0
    
    for city in cities:
        for c in cache:
            recent[c] += 1
        if city in cache:
            ans += 1
            recent[city] = 0
        else:
            ans += 5
            if len(cache) < cacheSize:
                cache.append(city)
                recent[city] = 0
            elif cacheSize:
                used_cnt = [(recent[c], c) for c in cache]
                used_cnt.sort(reverse = True)
                out = used_cnt[0][1]
                recent[out] = 0
                cache.remove(out)
                cache.append(city)
                recent[city] = 0
    
    return ans