from bisect import bisect_left

N = int(input())
S = []
SC = []
for n in range(N):
    s, c = map(int, input().split())
    S.append(s)
    SC.append((s, c))
S.sort()
result = 0
for s, c in SC:
    if c <= s:
        continue
    l = bisect_left(S, s)
    r = bisect_left(S, c)
    # print(l, r)
    result += r - l - 1
print(result)
