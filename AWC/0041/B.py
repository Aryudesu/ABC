N, M = map(int, input().split())
W = list(map(int, input().split()))
B = list(map(int, input().split()))
Bdata = []
for i in range(N):
    Bdata.append((B[i], i))
Bdata.sort()
# print(Bdata)
data = [None] * N
idx = 0
for n in range(N):
    while idx < M-1 and Bdata[n][0] >= W[idx]:
        idx += 1
    data[n] = (Bdata[n][1], idx + 1)
data.sort()
for b, n in data:
    print(n)
