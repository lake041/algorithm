from collections import Counter

counter = Counter("most common letter my test")
print(counter.most_common(1))

dp = {1:1, 5:2}
counter = Counter(dp)
print(counter)