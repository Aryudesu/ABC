N, K, T, C = map(int, input().split())
A = list(map(int, input().split()))
imos = [0] * N
s = 0
result = 0
for i in range(N):
    s += imos[i]
    if A[i] + s < T:
        t = T - (A[i] + s)
        if t > 0:
            if i + K < N:
                imos[i + K] -= t
            s += t
            result += t
    # print(imos)
print(result * C)
