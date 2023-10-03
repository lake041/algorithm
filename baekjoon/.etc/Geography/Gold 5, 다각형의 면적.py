# https://velog.io/@sunkyuj/python-백준-2162-선분-그룹

N = int(input())
dot = [list(map(int, input().split())) for _ in range(N)]
dot.append(dot[0])

area = 0
for i in range(len(dot)-1):
    area += (dot[i][0]*dot[i+1][1] - dot[i][1]*dot[i+1][0])
area = abs(area)*0.5
print(area)