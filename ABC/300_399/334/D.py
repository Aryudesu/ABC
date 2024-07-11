import bisect

N, Q = [int(l) for l in input().split()]
R = [int(l) for l in input().split()]
data = []
R.sort()
s = 0
for r in R:
    s += r
    data.append(s)
result = []
for q in range(Q):
    X = int(input())
    tmp = bisect.bisect_right(data, X)
    result.append(tmp)
for res in result:
    print(res)
