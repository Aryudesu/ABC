from bisect import bisect_left, bisect_right

N, M, Q = map(int, input().split())
B = list(map(int, input().split()))
B.sort()
imos = [0] * (M + 1)
for _ in range(Q):
    l, r = map(int, input().split())
    lidx = bisect_left(B, l)
    ridx = bisect_right(B, r)
    imos[lidx] += 1
    imos[ridx] -= 1
s = 0
result = 0
for idx in range(M):
    s = (s + imos[idx]) % 2
    if s:
        result += 1
print(result)
