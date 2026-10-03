from bisect import bisect_right

N, M, K = map(int, input().split())
S = list(map(int, input().split()))
G = list(map(int, input().split()))
G.sort()
nums = dict()
for g in G:
    nums[g] = K
result = 0
for s in S:
    idx = bisect_right(G, s)
    # print(G, s, idx)
    if idx == 0:
        continue
    g = G[idx-1]
    if nums[g] == 0:
        continue
    nums[g] -= 1
    result += 1
print(result)
