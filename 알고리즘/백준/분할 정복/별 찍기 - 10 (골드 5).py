N = int(input())

def recur(N):
    if N == 1:
        return ["*"]

    prev = recur(N//3)
    return [row*3 for row in prev] + [row + " "*len(prev) + row for row in prev] + [row*3 for row in prev]

bod = recur(N)
for row in bod:
    print(row)