# https://www.acmicpc.net/problem/1486

'''
첫째 줄에 산의 세로크기 N과 가로크기 M 그리고, T와 D가 주어진다. N과 M은 25보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 지도가 주어진다. T는 52보다 작거나 같은 자연수이고, D는 1,000,000보다 작거나 같은 자연수이다.
'''

N, M, T, D = map(int, input().split())
bod = [list(input()) for _ in range(N)]

for row in bod:
    print(row)


'''
6 6 6 36
AABCDE
GJIHGF
MKLMNO
STSRQP
YUVWXY
edcbaZ
'''