N, W, K = map(int, input().split())
data = [0] * N
for k in range(K):
    l = int(input())
    data[l-1] += 1
    if l-1+W < N:
        data[l-1 + W] -= 1
s = 0
for idx in range(N):
    s += data[idx]
    data[idx] = s
print(*data)
