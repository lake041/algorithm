N, R, C = map(int, input().split())

MAP = { (0, 0): 0, (0, 1): 1, (1, 0): 2, (1, 1): 3 }

def recur(start, N, R, C):
    if not N:
        print(start)
        return
    half_side, quater_block = 2**(N-1), 4**(N-1)
    plus = MAP[(R//half_side, C//half_side)] * quater_block
    recur(start + plus, N - 1, R % half_side, C % half_side)

recur(0, N, R, C)