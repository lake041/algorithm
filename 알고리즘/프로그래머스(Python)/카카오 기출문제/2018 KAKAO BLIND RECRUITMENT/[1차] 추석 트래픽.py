def solution(lines):
    for index, line in enumerate(lines):
        _, end, work = line.split()
        H, M, S, MS = map(int, [end[0:2], end[3:5], end[6:8], end[9:12]])
        work = int(float(work[:-1])*1000)
        end = H*3600*1000 + M*60*1000 + S*1000 + MS
        start = max(end - work + 1, 0)
        lines[index] = [start, end]

    sections = []
    ans = 0
    for S, E in lines:
        sections.append([S, S+999, 0])
        sections.append([E, E+999, 0])

    for S, E in lines:
        for section in sections:
            L, R, _ = section
            if L<=S<=R or L<=E<=R or S<=L<=E or S<=R<=E:
                section[2] += 1
            ans = max(ans, section[2])

    return ans