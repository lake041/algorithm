S = list(input())
T = list(input())

for _ in range(len(T)-len(S)):
    if T[-1] == "A":
        T.pop()
    elif T[-1] == "B":
        T.pop()
        T.reverse()

print(1 if S==T else 0)