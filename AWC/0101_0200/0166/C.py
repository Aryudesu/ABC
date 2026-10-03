from atcoder.dsu import DSU

N, M = map(int, input().split())
P = list(map(int, input().split()))
dsu = DSU(N)
for _ in range(M):
    u, v = map(int, input().split())
    dsu.merge(u-1, v-1)

nums = dict()
water = dict()
for n in range(N):
    l = dsu.leader(n)
    nums[l] = nums.get(l, 0) + 1
    water[l] = water.get(l, 0) + P[n]
maxWater = 0
minWater = 10 ** 18
for key in nums:
    n, w = nums[key], water[key]
    if w % n:
        maxWater = max(maxWater, w // n + 1)
    else:
        maxWater = max(maxWater, w // n)
    minWater = min(minWater, w // n)
print(maxWater - minWater)
