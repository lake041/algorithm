string = input()
target = []
temp = ''
for char in string:
    if char in ['-', '+']:
        target.append(int(temp))
        target.append(char)
        temp = ''
    else:
        temp += char
target.append(int(temp))

ans = 0
minus = False
for now in target:
    if now in ['-', '+']:
        if now == '-':
            minus = True
        continue
    if not minus:
        ans += now
    else:
        ans -= now
print(ans)
