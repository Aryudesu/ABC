N = int(input())
A = list(map(int, input().split()))
data = [a - 1 for a in A]
S = []
INF = 10 ** 18
m = INF
s = 0
result = -INF
for idx in range(N):
    m = min(m, s)
    s += data[idx]
    result = max(result, s-m)
print(result)
