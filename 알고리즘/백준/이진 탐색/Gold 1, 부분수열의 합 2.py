from collections import defaultdict

N, S = map(int, input().split())
nums = list(map(int, input().split()))

mid = N // 2
nums1 = nums[:mid]
nums2 = nums[mid:]

dp1 = defaultdict(int)
dp2 = defaultdict(int)

def go(origin: list, now: list, store: dict, index: int, hap: int):
    if index == len(origin):
        if not now:
            return
        store[hap] += 1
        return
    
    go(origin, now, store, index+1, hap)
    go(origin, now+[origin[index]], store, index+1, hap+origin[index])

go(nums1, [], dp1, 0, 0)
go(nums2, [], dp2, 0, 0)

ans = dp1[S] + dp2[S]
for key in dp1.keys():
    ans += dp1[key] * dp2[S-key]
print(ans)