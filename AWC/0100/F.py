from bisect import bisect_right

N, K = map(int, input().split())
V = list(map(int, input().split()))
ruiseki = []
s = 0
for v in V:
    s += v
    ruiseki.append(s)
result = 0
for r in range(N):
    num = ruiseki[r] - K
    if num >= 0:
        left = bisect_right(ruiseki, num)
        result += left + 1
        # print(r, num, left + 1, ruiseki)
print(result)
