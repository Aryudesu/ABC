import bisect

W, H = [int(l) for l in input().split()]
N = int(input())
# X, Y
PQ = [[int(l) for l in input().split()] for _ in range(N)]
# X
A = int(input())
AA = [int(l) for l in input().split()]
# Y
B = int(input())
BA = [int(l) for l in input().split()]

data = dict()
max_res = 0
for pq in PQ:
    # X
    tmpx = bisect.bisect_left(AA, pq[0])
    # Y
    tmpy = bisect.bisect_left(BA, pq[1])
    tmp = data.get((tmpx, tmpy), 0)
    data[(tmpx, tmpy)] = tmp + 1
    if tmp + 1 > max_res:
        max_res = tmp + 1
if len(data) < (A + 1) * (B + 1):
    min_res = 0
else:
    min_res = N + 1
    for i in data:
        if min_res > data[i]:
            min_res = data[i]
print(min_res, max_res)
