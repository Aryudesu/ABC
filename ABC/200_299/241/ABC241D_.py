import bisect

Q = int(input())
L = 0
data = []
res = []
idx = 0
max = -1
for q in range(Q):
    query = [int(l) for l in input().split()]
    x = query[1]
    if query[0] == 1:
        if max > x:
            bisect.insort(data, x)
        else:
            max = x
            data.append(x)
        L += 1
    elif query[0] == 2:
        k = query[2]
        # xの中で一番左のやつ
        idx = bisect.bisect_right(data, x) - 1
        if idx + 1 >= k:
            print(data[idx - k + 1])
        else:
            print(-1)
    else:
        k = query[2]
        # xの中で一番右のやつ
        idx = bisect.bisect_left(data, x)
        if L > idx + k - 1:
            print(data[idx + k - 1])
        else:
            print(-1)
