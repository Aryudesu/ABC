N = int(input())
A = [int(l) for l in input().split()]
data = dict()
stNum = A[0]
for i in range(N):
    prev = None
    aft = None
    if i > 0:
        prev = A[i-1]
    if i < N - 1:
        aft = A[i + 1]
    data[A[i]] = (prev, aft)
Q = int(input())
for _ in range(Q):
    # print(data)
    n, *q = [int(l) for l in input().split()]
    if n == 1:
        x, y = q
        tmp = data[x]
        aftNum = tmp[1]
        if not aftNum is None:
            adata = data[aftNum]
            data[aftNum] = (y, adata[1])
        data[y] = (x, aftNum)
        data[x] = (tmp[0], y)
    else:
        x = q[0]
        tmp = data[x]
        prev, aft = tmp
        if not prev is None:
            ptmp = data[prev]
            data[prev] = (ptmp[0], aft)
        else:
            stNum = aft
        if not aft is None:
            atmp = data[aft]
            data[aft] = (prev, atmp[1])
        data[x] = None
result = []
num = stNum
while not num is None:
    result.append(num)
    tmp = data[num]
    num = tmp[1]
print(*result)
