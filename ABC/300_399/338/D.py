# 終わった・・・
N, M = [int(l) for l in input().split()]
X = [int(l) - 1 for l in input().split()]
data = [0] * N
prev = X[0]
s = 0
for idx in range(1, M):
    tmp = abs(X[idx] - prev)
    a, b = min(X[idx], prev), max(X[idx], prev)
    if N - tmp < tmp:
        data[0] += tmp - (N - tmp)
        if a + 1 < N:
            data[a + 1] -= tmp - (N - tmp)
        data[b] += tmp - (N - tmp)
        s += N - tmp
    else:
        data[a] += (N - tmp) + tmp
        if b + 1 < N:
            data[b + 1] -= (N - tmp) + tmp
        s += tmp
    prev = X[idx]
t = 0
result = 10*10
for idx in range(N):
    t += data[idx]
    if result > t:
        result = t
print(s + result)
