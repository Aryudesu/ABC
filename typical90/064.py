N, Q = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
data = [0] * N
for _ in range(Q):
    l, r, v = [int(l) for l in input().split()]
    data[l-1] += v
    if r < N:
        data[r] -= v
print(data)
