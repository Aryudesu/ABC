from bisect import bisect_right

N = int(input())
C = [int(l) for l in input().split()]
C.sort()
data = []
s = 0
for c in C:
    s += c
    data.append(s)
Q = int(input())
result = []
for q in range(Q):
    X = int(input())
    result.append(bisect_right(data, X))
for r in result:
    print(r)
