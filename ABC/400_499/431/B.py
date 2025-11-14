X = int(input())
N = int(input())
W = list(map(int, input().split()))
result = X
res = []
parts = set()
Q = int(input())
for _ in range(Q):
    P = int(input())
    if P in parts:
        result -= W[P-1]
        parts.discard(P)
    else:
        result += W[P-1]
        parts.add(P)
    res.append(result)
for r in res:
    print(r)
