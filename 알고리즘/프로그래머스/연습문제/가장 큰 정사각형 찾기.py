def solution(bod):
    bod = [row + [0] for row in bod]
    H = [0]*len(bod[0])
    nemo = []
    
    for row in bod:
        H = [prev + 1 if now else 0 for prev, now in zip(H, row)]
        stack = [(-1, 0)]
        for index, height in enumerate(H):
            while height < stack[-1][1]:
                h = stack.pop()[1]
                w = index - stack[-1][0] - 1
                nemo.append(min(h, w) ** 2)
            stack.append((index, height))
    
    return max(nemo) if nemo else 0


