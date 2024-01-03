arr = [
    [0,0,1], 
    [0,1,0], 
    [1,1,1], 
    [1,0,0]
    ]

print('1. 시계방향')
for row in list(map(list, zip(*(arr)[::-1]))):
    print(row)
print()

print('2. 반시계방향')
for row in list(map(list, zip(*(arr))))[::-1]:
    print(row)
print()

print('3. 180도 회전')
for row in [row[::-1] for row in arr][::-1]:
    print(row)
print()

print('4. y = -x 대칭이동')
for row in list(map(list, zip(*(arr)))):
    print(row)
print()

print('5. y = x 대칭이동')
for row in list(map(list, zip(*(arr[::-1]))))[::-1]:
    print(row)