# https://www.acmicpc.net/problem/2448

def star():
    print("  *  ")
    print(" * * ")
    print("*****")

N = int(input())
temp = N / 3
k = 0
while True:
    if temp == 1:
        break
    temp /= 2
    k += 1

star = []
for i in range(k+1):
    if i == 0:
        star.append([
            "  *  ",
            " * * ",
            "*****"
        ])
        continue
    length = 3 * 2**i
    half_length = int(length / 2)
    star.append([""]*length)
    for j in range(half_length):
        star[i][j] += " " * half_length
        star[i][j] += star[i-1][j]
        star[i][j] += " " * half_length
    for j in range(half_length, length):
        star[i][j] += star[i-1][j-half_length]
        star[i][j] += " "
        star[i][j] += star[i-1][j-half_length]

for row in star[-1]:
    print(row)