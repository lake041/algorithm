from itertools import product

def solution(N, wires):
    if N == 2:
        return 0
    
    ans = N
    for sub in [wires[:i] + wires[i+1:] for i in range(len(wires))]:
        s = set(sub[0])
        [s.update(edge) for _, edge in product(sub, sub) if set(edge) & s]
        ans = min(ans, abs(N-len(s)*2))
    return ans