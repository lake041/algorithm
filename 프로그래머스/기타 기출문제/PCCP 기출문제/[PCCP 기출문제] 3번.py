def sec_to_hhmmss(sec):
    H = str(int(sec//3600))
    M = str(int((sec//60)%60))
    S = str(sec%60)
    return H+':'+M+':'+S
    

def solution(h1, m1, s1, h2, m2, s2):
    hs, ms = [], [], []
    for i in range(60):
        ms.append(3600 * i / 59)
    ms.pop()
    
    for m in ms[:]:
        for i in range(1, 24):
            ms.append(i*3600 + m)

    for i in range(60 * 12):
        hs.append(360 * 120 * i / 719)
    hs.pop()
    
    for h in hs[:]:
        hs.append(12*3600 + h)
    
    hap = list(set(ms+hs))
    hap.sort()
    
    S = h1*3600 + m1*60 + s1
    E = h2*3600 + m2*60 + s2
    ans = 0
    for time in hap:
        if S<=time<=E:
            ans += 1    

    return ans