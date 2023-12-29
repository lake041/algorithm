def solution(m, n, startX, startY, balls):
    ans = []
    sx, sy = startX, startY

    for tx, ty in balls:

        l1 = (sx - tx) ** 2 + (n - sy + n - ty) ** 2        # 위쪽
        l2 = (m - sx + m - tx) ** 2 + (sy - ty) ** 2        # 오른쪽
        l3 = (sx - tx) ** 2 + (sy + ty) ** 2        # 아래쪽
        l4 = (sx + tx) ** 2 + (sy - ty) ** 2        # 왼쪽
        l = [l1, l2, l3, l4]

        if sx == tx and sy > ty:
            l.remove(l3)
        elif sx == tx and sy < ty:
            l.remove(l1)
        elif sy == ty and sx > tx:
            l.remove(l4)
        elif sy == ty and sx < tx:
            l.remove(l2)

        ans.append(min(l))

    return ans