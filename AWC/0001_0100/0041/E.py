N, Q = map(int, input().split())
H = list(map(int, input().split()))
INF = 10000000000
lStack = [(INF, 0)]
rStack = [(INF, N+1)]

lData = [None] * (N+1)
rData = [None] * N
lData[0] = 0
rData[-1] = N+1
for i in range(1,N):
    r = H[-i-1]
    while rStack[-1][0] <= r:
        rStack.pop()
    rIdx = rStack[-1][1]
    rStack.append((r, N-i-1))
    rData[-i-1] = rIdx+1

    l = H[i]
    while lStack[-1][0] <= l:
        lStack.pop()
    lIdx = rStack[-1][1]
    lStack.append((l, i))
    lData[i] = lIdx+1

data = []
for i in range(N):
    data.append(rData[i]-lData[i]-1)
print(lData)
print(rData)
print(data)
for _ in range(Q):
    x = int(input())
