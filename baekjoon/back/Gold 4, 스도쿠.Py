from itertools import product

bod = [list(map(int, list(input()))) for _ in range(9)]

row_nums = [[] for _ in range(9)]
col_nums = [[] for _ in range(9)]
box_nums = [[] for _ in range(9)]

def find_box(row, col):
    row //= 3
    col //= 3
    return row*3 + col

def find_next(row, col):
    if col == 8:
        return row+1, 0
    else:
        return row, col+1

for row, col in product(range(9), range(9)):
    num = bod[row][col]
    if num == 0:
        continue
    row_nums[row].append(num)
    col_nums[col].append(num)
    box_nums[find_box(row, col)].append(num)

def go(y, x, row_nums: list[list[int]], col_nums: list[list[int]], box_nums: list[list[int]]):
    if y == 9:
        for row in bod:
            print(''.join(map(str, row)))
        return True
    
    ny, nx = find_next(y, x)
    if bod[y][x] != 0:
        if go(ny, nx, row_nums, col_nums, box_nums):
            return True
    else:
        for num in range(1, 10):
            if (num not in row_nums[y]) and (num not in col_nums[x]) and (num not in box_nums[find_box(y,x)]):
                row_nums[y].append(num)
                col_nums[x].append(num)
                box_nums[find_box(y,x)].append(num)
                bod[y][x] = num
                if go(ny, nx, row_nums, col_nums, box_nums):
                    return True
                row_nums[y].remove(num)
                col_nums[x].remove(num)
                box_nums[find_box(y,x)].remove(num)
                bod[y][x] = 0

go(0, 0, row_nums, col_nums, box_nums)

'''
103000509
002109400
000704000
300502006
060000050
700803004
000401000
009205800
804000107

143628579
572139468
986754231
391542786
468917352
725863914
237481695
619275843
854396127

143628579
572139468
998754333
381592996
961977352
755863994
257491995
619275843
'''